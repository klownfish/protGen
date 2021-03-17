"use strict";
const { exec } = require("child_process");
let fs = require('fs');

if (process.argv.length < 4) {
    console.log(`usage: node INPUT_FILE OUTPUT_DIR`)
    return
}
let input = process.argv[2]
let output = process.argv[3]
let raw = fs.readFileSync(input).toString()
let schema = JSON.parse(raw);
let baseName = output + `/${schema.config.name}`

let warning = 
`/*****************************
GENERATED FILE DO NOT EDIT
******************************/\n\n`
let h_file = warning 
h_file +=
`#include <stdint.h>\n\n`
//generate flags
for (let datatype in schema.datatypes) {
    if (!schema.datatypes[datatype].bitField) {
        continue
    }
    let index = 0
    for (let bit of schema.datatypes[datatype].bitField) {
        h_file += `#define ${datatype.toUpperCase()}_${bit.toUpperCase()} (1<<${index++})\n`
    }
    h_file += "\n"
}

//generate enums
for (let name in schema.enums) {
    h_file += `enum struct ${name}: ${schema.enums[name].nativeType} {\n`
    for (let value in schema.enums[name].entries) {
        h_file += `    ${value} = ${schema.enums[name].entries[value]},\n`
    }
    h_file += "};\n"
}

h_file +=
`
auto scaledFloat_to_uint(double value, double scale) {
    return value * scale;
}

template <typename T>
double uint_to_scaledFloat(T value, double scale) {
    return value / scale;
}

template <typename T>
T packedFloat_to_uint(double value, double min, double max) {
    T max_value = ~0;
    double difference = max - min;
    return (value - min) / difference * max_value;
}

template <typename T>
double uint_to_packedFloat(T value, double min, double max) {
    T max_value = ~0;
    double difference = max - min;
    return difference * max_value / value;
}\n\n`

//generate structs
for (let datatype in schema.datatypes) {
    if (schema.datatypes[datatype].totalSize == 0) {
        continue;
    }
    h_file += `struct __attribute__((__packed__)) struct_${datatype} {\n`
    if (schema.datatypes[datatype].bitField) {
        h_file += `    ${schema.datatypes[datatype].bitFieldNativeType} bitField;\n`
    }
    if (!schema.datatypes[datatype].fields) {
        continue
    }
    for (let field of schema.datatypes[datatype].fields) {
        switch (field.type) {
            case "enum":
                h_file += `    enum ${field.enumName} ${field.name};\n`
                break;
            default:
                h_file += `    ${field.nativeType} ${field.name};\n`
        }
    }
    h_file += "}; \n"
    h_file += `static_assert((sizeof(struct_${datatype}) == ${schema.datatypes[datatype].totalSize}), "sizeof is not equal to the calculated size!");\n\n`
}

//generate receiving classes
for (let msg in schema.messages) {
    let datatype = schema.messages[msg].datatype
    h_file += 
    `class ${schema.datatypes[datatype].name} {\n` +
    `public:\n`
    if (schema.datatypes[datatype].totalSize != 0) {
        h_file += `struct struct_${schema.datatypes[datatype].name}* storage;\n` +
        `uint8_t size = sizeof(*storage);\n` +
        `uint8_t get_size() {return size;}\n` +
        `void set_bytes(uint8_t* pointer) {\n` +
        `storage = (struct_${schema.datatypes[datatype].name}*) pointer;\n` +
        `}\n`
    } else {
        h_file += `void set_bytes(uint8_t* pointer) {}`
        h_file += `uint8_t get_size() {return 0;}`
    }
    h_file +=
    `uint64_t id = ${schema.messages[msg].id};\n` +
    `uint64_t get_id() {return id;}\n` +
    `enum units source;` +
    `enum units target;` +
    `enum units get_source() {return source;}` +
    `enum units get_target() {return target;}` +
    `void set_source(enum units value) {source = value;}` +
    `void set_target(enum units value) {target = value;}`
    

    if (schema.datatypes[datatype].bitField) {
        h_file += `${schema.datatypes[datatype].bitFieldNativeType} get_bit_field() {return storage->bitField;}`
    }
    //getters
    for (let field of schema.datatypes[datatype].fields) {
        switch(field.type) {
            case "packedFloat":
                h_file += 
                `double get_${field.name}() {\n` +
                `return uint_to_packedFloat(storage->${field.name}, ${field.min}, ${field.max});\n` +
                `}\n`
                break;
            case "scaledFloat":
                h_file += 
                `double get_${field.name}() {\n` +
                `return uint_to_scaledFloat(storage->${field.name}, ${field.scale});\n` +
                `}\n`
                break;
            case "enum":
                h_file += 
                `enum ${field.enumName} get_${field.name}() {\n` +
                `return storage->${field.name};\n`+
                `}\n`
                break;
            default:
                h_file += 
                `${field.nativeType} get_${field.name}() {\n` +
                `return storage->${field.name};\n`+
                `}\n`
        }
    }
    h_file += "};\n\n\n"
}

//generate senders
for (let msg in schema.messages) {
    let datatype = schema.messages[msg].datatype
    h_file +=
    `class ${datatype}_to_${schema.messages[msg].target} {\n` +
    `public:\n`
    if (schema.datatypes[datatype].totalSize != 0) {
        h_file += `struct struct_${schema.datatypes[datatype].name}* storage;\n` +
        `uint8_t size = sizeof(*storage);\n` +
        `uint8_t get_size() {return size;}\n` +
        `void set_bytes(uint8_t* pointer) {\n` +
        `storage = (struct_${schema.datatypes[datatype].name}*) pointer;\n` +
        `}\n`
    } else {
        h_file += `void set_bytes(uint8_t* pointer) {}`
        h_file += `uint8_t get_size() {return 0;}`
    }
    h_file += 
    `uint64_t id = ${schema.messages[msg].id};\n` +
    `uint64_t get_id() {return id;}\n`
    if (schema.datatypes[datatype].bitField) {
        h_file += `void set_bit_field(${schema.datatypes[datatype].bitFieldNativeType} value) {storage->bitField = value;}`
    }
    for (let field of schema.datatypes[datatype].fields) {
        h_file += '\n'
        //setters
        switch(field.type) {
            case "packedFloat":
                h_file += 
                `void set_${field.name}(double value) {\n` +
                `storage->${field.name} = packedFloat_to_uint(value, ${field.min}, ${field.max});\n` +
                `}\n`
                break;
            case "scaledFloat":
                h_file += 
                `void set_${field.name}(double value) {\n` +
                `storage->${field.name} = scaledFloat_to_uint(value, ${field.scale});\n` +
                `}\n`
                break;
            case "enum":
                h_file += 
                `void set_${field.name}(enum ${field.enumName} value) {\n` +
                `storage->${field.name} = value;\n`+
                `}\n`
                break;
            default:
                h_file += 
                `void set_${field.name}(${field.nativeType} value) {\n` +
                `storage->${field.name} = value;\n`+
                `}\n`
                break;
        }
    }
    h_file += "};\n\n\n"
}

//generate length macro
h_file += 
`#define ID_TO_LEN(id, length) \\
switch(id) { \\\n `
for (let msg in schema.messages) {
    h_file += `    case ${schema.messages[msg].id}:\\\n` +
    `        length = ${schema.datatypes[schema.messages[msg].datatype].totalSize};\\\n` +
    `        break;\\\n`
}
h_file += "}\n\n"

//generate parse macro
h_file +=
`#define PARSE_MESSAGE(id, buf) \\
switch(id) { \\\n `
for (let msg in schema.messages) {
    h_file += `    case ${schema.messages[msg].id}: {\\\n` +
    `        ${schema.messages[msg].datatype} __message;\\\n` +
    `        __message.set_bytes(buf);\\\n` +
    `        __message.set_source(units::${schema.messages[msg].source});\\\n` +
    `        __message.set_target(units::${schema.messages[msg].target});\\\n` +
    `        ${schema.config.name}_rx(__message);\\\n` +
    `        break;}\\\n`
}
h_file += "}\n\n"

//generate id to source macro
h_file +=
`#define ID_TO_SOURCE(id, source) \\
switch(id) { \\\n `
for (let msg in schema.messages) {
    h_file += `    case ${schema.messages[msg].id}:\\\n` +
    `        source = units::${schema.messages[msg].source};\\\n` +
    `        break;\\\n`
}
h_file += "}\n\n"

//generate id to target macro
h_file +=
`#define ID_TO_TARGET(id, source) \\
switch(id) { \\\n `
for (let msg in schema.messages) {
    h_file += `    case ${schema.messages[msg].id}:\\\n` +
    `        source = units::${schema.messages[msg].target};\\\n` +
    `        break;\\\n`
}
h_file += "}\n\n"

fs.writeFileSync(`${baseName}.h`, h_file)
exec(`clang-format --style="LLVM" -i ${baseName}*`, ((error) => {
    if (error)
        console.log("install clang-format in PATH to format the output")
}))