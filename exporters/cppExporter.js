"use strict";
console.log(process.cwd())
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

//generate enums
let enum_out = warning 
for (let name in schema.enums) {
    enum_out += `enum struct ${name}: ${schema.enums[name].nativeType} {\n`
    for (let value in schema.enums[name].entries) {
        enum_out += `    ${value.toUpperCase()} = ${schema.enums[name].entries[value]},\n`
    }
    enum_out += "};\n"
}
fs.writeFileSync(`${baseName}_enums.h`, enum_out)


//generate flags
let flags_out = warning
for (let datatype in schema.datatypes) {
    if (!schema.datatypes[datatype].bitField) {
        continue
    }
    let index = 0
    for (let bit of schema.datatypes[datatype].bitField) {
        flags_out += `#define ${datatype.toUpperCase()}_${bit.toUpperCase()} (1<<${index++})\n`
    }
    flags_out += "\n"
}
fs.writeFileSync(`${baseName}_flags.h`, flags_out)


//generate structs
let structs_out = warning
structs_out += "#include <stdint.h>\n"
structs_out += `#include "${schema.config.name}_enums.h"\n\n`
for (let datatype in schema.datatypes) {
    structs_out += `struct __attribute__((packed)) struct_${datatype} {\n`
    if (schema.datatypes[datatype].bitField) {
        structs_out += `    ${schema.datatypes[datatype].bitFieldNativeType} bitField;\n`
    }
    if (!schema.datatypes[datatype].fields) {
        continue
    }
    for (let field of schema.datatypes[datatype].fields) {
        switch (field.type) {
            case "enum":
                structs_out += `    enum ${field.enumName} ${field.name};\n`
                break;
            default:
                structs_out += `    ${field.nativeType} ${field.name};\n`
        }
    }
    structs_out += "}; \n"
}
fs.writeFileSync(`${baseName}_structs.h`, structs_out)


//generate classes
let classes_out = warning;
classes_out += `#include "${schema.config.name}_structs.h"\n`;
classes_out += `#include "${schema.config.name}_functions.h"\n`;
for (let msg in schema.messages) {
    let datatype = schema.messages[msg].datatype
    classes_out += 
    `class ${schema.messages[msg].source}_${schema.datatypes[datatype].name} {\n` +
    `public:\n` +
    `struct struct_${schema.datatypes[datatype].name}* storage;\n` +
    `uint8_t size = sizeof(*storage);\n` +
    `uint64_t id = ${schema.messages[msg].id};\n` +
    `uint8_t get_size() {return size;}\n` +
    `void set_bytes(uint8_t* pointer) {\n` +
    `storage = (struct_${schema.datatypes[datatype].name}*) pointer;\n` +
    `}\n`
    if (schema.datatypes[datatype].bitField) {
        classes_out += `${schema.datatypes[datatype].bitFieldNativeType} get_bitfield() {return storage->bitField;}`
    }
    //getters
    for (let field of schema.datatypes[datatype].fields) {
        classes_out += `\n`
        switch(field.type) {
            case "packedFloat":
                classes_out += 
                `double get_${field.name}() {\n` +
                `double out;\n` +
                `uint_to_packedFloat(storage->${field.name}, ${field.min}, ${field.max}, &out);\n` +
                `return out;\n` +
                `}\n`
                break;
            case "scaledFloat":
                classes_out += 
                `double get_${field.name}() {\n` +
                `double out;\n` +
                `uint_to_scaledFloat(storage->${field.name}, ${field.scale}, &out);\n` +
                `return out;\n` +
                `}\n`
                break;
            case "enum":
                classes_out += 
                `enum ${field.enumName} get_${field.name}() {\n` +
                `return storage->${field.name};\n`+
                `}\n`
                break;
            default:
                classes_out += 
                `${field.nativeType} get_${field.name}() {\n` +
                `return storage->${field.name};\n`+
                `}\n`
        }
        //setters
        switch(field.type) {
            case "packedFloat":
                classes_out += 
                `void set_${field.name}(double value) {\n` +
                `packedFloat_to_uint(value, ${field.min}, ${field.max}, &storage->${field.name});\n` +
                `}\n`
                break;
            case "scaledFloat":
                classes_out += 
                `void set_${field.name}(double value) {\n` +
                `scaledFloat_to_uint(value, ${field.scale}, &storage->${field.name});\n` +
                `}\n`
                break;
            case "enum":
                classes_out += 
                `void set_${field.name}(enum ${field.enumName} value) {\n` +
                `storage->${field.name} = value;\n`+
                `}\n`
                break;
            default:
                classes_out += 
                `void set_${field.name}(${field.nativeType} value) {\n` +
                `storage->${field.name} = value;\n`+
                `}\n`
                break;
        }
    }
    classes_out += "};\n\n\n"
}
fs.writeFileSync(`${baseName}_classes.h`, classes_out)


//generate functions
let functions_out = warning +
`template <typename T>
void scaledFloat_to_uint(double value, double scale, T* target) {
    *target = value * scale;
}

template <typename T>
void uint_to_scaledFloat(T value, double scale, double* target) {
    *target = value / scale;
}

template <typename T>
void packedFloat_to_uint(double value, double min, double max, T* target) {
    T max_value = ~0;
    double difference = max - min;
    *target = (value - min) / difference * max_value;
}

template <typename T>
void uint_to_packedFloat(T value, double min, double max, double* target) {
    T max_value = ~0;
    double difference = max - min;
    *target = difference * max_value / value;
}\n\n`

//generate length macro
functions_out += 
`#define ID_TO_LEN(id, length) \\
switch(id) { \\\n `
for (let msg in schema.messages) {
    functions_out += `    case ${schema.messages[msg].id}:\\\n` +
    `        length = ${schema.datatypes[schema.messages[msg].datatype].totalSize};\\\n` +
    `        break;\\\n`
}
functions_out += "}\n\n"

//generate parse macro
functions_out +=
`#define PARSE_MESSAGE(id, buf) \\
switch(id) { \\\n `
for (let msg in schema.messages) {
    functions_out += `    case ${schema.messages[msg].id}:\\\n` +
    `        ${schema.messages[msg].source}_${schema.messages[msg].datatype} __message;\\\n` +
    `        __message.set_bytes(buf);\\\n` +
    `        ${schema.config.name}_rx(__message);\\\n` +
    `        break;\\\n`
}
functions_out += "}\n\n"

//generate id to source macro
functions_out +=
`#define ID_TO_SOURCE(id, source) \\
switch(id) { \\\n `
for (let msg in schema.messages) {
    functions_out += `    case ${schema.messages[msg].id}:\\\n` +
    `        source = units::${schema.messages[msg].source.toUpperCase()};\\\n` +
    `        break;\\\n`
}
functions_out += "}\n\n"

//generate id to target macro
functions_out +=
`#define ID_TO_TARGET(id, source) \\
switch(id) { \\\n `
for (let msg in schema.messages) {
    functions_out += `    case ${schema.messages[msg].id}:\\\n` +
    `        source = units::${schema.messages[msg].target.toUpperCase()};\\\n` +
    `        break;\\\n`
}
functions_out += "}\n\n"

//create function constructor
for (let msg in schema.messages) {
    functions_out += `void ${schema.config.name}_rx(${schema.messages[msg].source}_${schema.messages[msg].datatype} __message);\n` 
}

fs.writeFileSync(`${baseName}_functions.h`, functions_out)

//generate the FINAL ULTIMATE COMBINING FILE
let protocol_out = warning +
`#include "${schema.config.name}_flags.h"\n` +
`#include "${schema.config.name}_classes.h"\n`
fs.writeFileSync(`${baseName}.h`, protocol_out)

exec(`clang-format --style="LLVM" -i ${baseName}*`, ((error) => {
    if (error)
        console.log("install clang-format in PATH to format the output")
}))