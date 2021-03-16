"use strict";
const { exec } = require("child_process");
let fs = require('fs');

let raw = fs.readFileSync("./out/json/protocol.json").toString()
let schema = JSON.parse(raw);

let warning = 
`/*****************************
GENERATED FILE DO NOT EDIT
******************************/\n\n`


//generate enums
let enum_out = warning 
for (let name in schema.enums) {
    enum_out += `enum ${name}: ${schema.enums[name].nativeType} {\n`
    for (let value in schema.enums[name].entries) {
        enum_out += `    ${value} = ${schema.enums[name].entries[value]},\n`
    }
    enum_out += "};\n"
}
fs.writeFileSync("./out/cpp/protocol_enums.h", enum_out)


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
fs.writeFileSync("./out/cpp/protocol_flags.h", flags_out)


//generate structs
let structs_out = warning
structs_out += "#include <stdint.h>\n"
structs_out += `#include "protocol_enums.h"\n\n`
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
fs.writeFileSync("./out/cpp/protocol_structs.h", structs_out)


//generate classes
let classes_out = warning;
classes_out += `#include "protocol_structs.h"\n`;
classes_out += `#include "protocol_functions.h"\n`;
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
        //classes_out += `\n`
    }
    classes_out += "};\n\n\n"
}
fs.writeFileSync("./out/cpp/protocol_classes.h", classes_out)


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
`#define PARSE_MESSAGE(id, callback, buf) \\
switch(id) { \\\n `
for (let msg in schema.messages) {
    functions_out += `    case ${schema.messages[msg].id}:\\\n` +
    `        ${schema.messages[msg].source}_${schema.messages[msg].datatype} __message;\\\n` +
    `        __message_struct.set_bytes(__message);\\\n` +
    `        callback(__message);\\\n` +
    `        break;\\\n`
}
functions_out += "}\n\n"
fs.writeFileSync("./out/cpp/protocol_functions.h", functions_out)

//generate the FINAL ULTIMATE COMBINING FILE
let protocol_out = warning +
`#include "protocol_flags.h"\n` +
`#include "protocol_classes.h"\n`
fs.writeFileSync("./out/cpp/protocol.h", protocol_out)

exec(`clang-format --style="LLVM" -i ./out/cpp/*`, ((error) => {
    if (error)
        console.log("install clang-format in PATH to format the output")
}))
