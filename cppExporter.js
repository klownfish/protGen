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
let cpp_file = warning
cpp_file +=
`#include <stdint.h>
#include "${schema.config.name}.h"\n\n`

h_file +=
`#include <stdint.h>
#include <string.h>
#include <math.h>\n\n`

h_file += `namespace  ${schema.config.name}{`

//generate enums
for (let name in schema.enums) {
    h_file += `enum struct ${name}: ${schema.enums[name].nativeType}_t {\n`
    for (let value in schema.enums[name].entries) {
        h_file += `    ${value} = ${schema.enums[name].entries[value]},\n`
    }
    h_file += "};\n"
}

h_file +=
`template <typename T>
void scaledFloat_to_uint(double value, double scale, T* out) {
    *out = value * scale;
}

template <typename T>
void uint_to_scaledFloat(T value, double scale, double* out ) {
    *out = value / scale;
}

template <typename T>
void packedFloat_to_uint(double value, double min, double max, T* out) {
    T max_value = ~0;
    double difference = max - min;
    *out = (value - min) / difference * max_value;
}

template <typename T>
void uint_to_packedFloat(T value, double min, double max, double* out) {
    T max_value = ~0;
    double difference = max - min;
    *out = difference * value / max_value;
}\n\n`

//generate receiving classes
for (let key in schema.datatypes) {
    let datatype = schema.datatypes[key]
    //create class definition
    h_file += 
    `class ${datatype.name} {\n` +
    `public:\n`
    //generate fields
    for (let field of datatype.fields) {
        h_file += `${field.nativeType}_t ${field.name};\n`
        h_file += `static_assert((sizeof(${field.name}) == ${field.size}), "invalid size");\n`
    }
    if (datatype.bitField) {
        h_file += `${datatype.bitFieldNativeType}_t bit_field;\n`
        h_file += `static_assert((sizeof(bit_field) == ${datatype.bitFieldSize}), "invalid size");\n`
        for (let i = 0; i < datatype.bitField.length; i++) {
            h_file += `bool get_${datatype.bitField[i]}() {return bit_field & (1 << ${i});}`
        }
    }
    h_file +=
    `uint8_t size = ${datatype.totalSize};\n` +
    `uint8_t get_size() {return size;}\n` +
    `enum units source;\n` +
    `enum units target;\n` +
    `enum units get_source() {return source;}\n` +
    `enum units get_target() {return target;}\n` +
    `void set_source(enum units value) {source = value;}\n` +
    `void set_target(enum units value) {target = value;}\n`+
    //parse buf
    `void parse_buf(uint8_t* buf) {\n`
    if (datatype.fields.length || datatype.bitField) {
        h_file += `uint8_t index = 0;\n` 
        if (datatype.bitField) {
            h_file += `memcpy(&bit_field, buf +  index, sizeof(bit_field));\n`
            h_file += `index += sizeof(bit_field);\n`
        }
        for (let field of datatype.fields) {
            h_file += `memcpy(&${field.name}, buf + index, sizeof(${field.name}));\n` 
            h_file += `index += sizeof(${field.name});\n`  
        }
    }
    h_file += `}`
    //getters
    for (let field of datatype.fields) {
        switch(field.type) {
            case "packedFloat":
                h_file += 
                `double get_${field.name}() {\n` +
                `double out;\n` +
                `uint_to_packedFloat(${field.name}, ${field.min}, ${field.max}, &out);\n` +
                `return out\n;`
                `}\n`
                break;
            case "scaledFloat":
                h_file += 
                `double get_${field.name}() {\n` +
                `double out;\n` +
                `uint_to_scaledFloat(${field.name}, ${field.scale}, &out);\n` +
                `return out;\n` +
                `}\n`
                break;
            case "enum":
                h_file += 
                `enum ${field.enumName} get_${field.name}() {\n` +
                `return ${field.name};\n`+
                `}\n`
                break;
            default:
                h_file += 
                `${field.nativeType}_t get_${field.name}() {\n` +
                `return ${field.name};\n`+
                `}\n`
        }
    }
    h_file += "};\n\n\n"
}

//generate senders
for (let key in schema.messages) {
    let msg = schema.messages[key]
    let datatype = schema.datatypes[msg.datatype]
    h_file +=
    `class ${datatype.name}_from_${msg.source}_to_${msg.target} {\n` +
    `public:\n`
    for (let field of datatype.fields) {
        h_file += `${field.nativeType}_t ${field.name};\n`
        h_file += `static_assert((sizeof(${field.name}) == ${field.size}), "invalid size");\n`
    }
    if (datatype.bitField) {
        h_file += `${datatype.bitFieldNativeType}_t bit_field = 0;\n`
        h_file += `static_assert((sizeof(bit_field) == ${datatype.bitFieldSize}), "invalid size");\n`
        for (let i = 0; i < datatype.bitField.length; i++) {
            h_file += `void set_${datatype.bitField[i]}(bool value) {\n` +
                `bit_field = value * (bit_field | (1 << ${i})) + !value * (bit_field & ~(1 << ${i}));\n` +
            `}`
        }
    }
    h_file +=
    `uint8_t size = ${datatype.totalSize};\n` +
    `uint8_t get_size() {return size;}\n` +
    `${schema.config.idNativeType}_t id = ${msg.id};\n` +
    `${schema.config.idNativeType}_t get_id() {return id;}\n` +
    `enum units source;\n` +
    `enum units target;\n` +
    `enum units get_source() {return source;}\n` +
    `enum units get_target() {return target;}\n` +
    `void set_source(enum units value) {source = value;}\n` +
    `void set_target(enum units value) {target = value;}\n`+
    //build buf
    `void build_buf(uint8_t* buf, uint8_t* index) {\n` 
    if (datatype.bitField) {
        h_file += `memcpy(buf + *index, &bit_field, sizeof(bit_field));\n`
        h_file += `*index += sizeof(bit_field);\n`
    }
    for (let field of datatype.fields) {
        h_file += `memcpy(buf + *index, &${field.name}, sizeof(${field.name}));\n` 
        h_file += `*index += sizeof(${field.name});\n`  
    }
    h_file += `}\n`
    for (let field of datatype.fields) {
        //setters
        switch(field.type) {
            case "packedFloat":
                h_file += 
                `void set_${field.name}(double value) {\n` +
                `packedFloat_to_uint(value, ${field.min}, ${field.max}, &${field.name});\n` +
                `}\n`
                break;
            case "scaledFloat":
                h_file += 
                `void set_${field.name}(double value) {\n` +
                `scaledFloat_to_uint(value, ${field.scale}, &${field.name});\n` +
                `}\n`
                break;
            case "enum":
                h_file += 
                `void set_${field.name}(enum ${field.enumName} value) {\n` +
                `${field.name} = value;\n`+
                `}\n`
                break;
            default:
                h_file += 
                `void set_${field.name}(${field.nativeType}_t value) {\n` +
                `${field.name} = value;\n`+
                `}\n`
                break;
        }
    }
    h_file += "};\n\n\n"
}

//generate parse macro
h_file +=
`#define ${schema.config.name.toUpperCase()}_PARSE_MESSAGE(id, buf) \\
switch(id) { \\\n `
for (let msg in schema.messages) {
    h_file += `    case ${schema.messages[msg].id}: {\\\n` +
    `        ${schema.config.name}::${schema.messages[msg].datatype} __message;\\\n` +
    `        __message.parse_buf(buf);\\\n` +
    `        __message.set_source(${schema.config.name}::units::${schema.messages[msg].source});\\\n` +
    `        __message.set_target(${schema.config.name}::units::${schema.messages[msg].target});\\\n` +
    `        ${schema.config.name}_rx(__message);\\\n` +
    `        break;}\\\n`
}
h_file += "}\n\n"

//generate length function
h_file += `uint8_t id_to_len(size_t id);`
cpp_file += 
`uint8_t ${schema.config.name}::id_to_len(size_t id){
switch(id) {\n`
for (let msg in schema.messages) {
    cpp_file += `    case ${schema.messages[msg].id}:\n` +
    `        return ${schema.datatypes[schema.messages[msg].datatype].totalSize};\n` +
    `        break;\n`
}
cpp_file += "}\n}\n\n"

//generate source funtion
h_file += `enum units id_to_source(size_t id);`
cpp_file += 
`enum ${schema.config.name}::units ${schema.config.name}::id_to_source(size_t id){
switch(id) {\n`
for (let msg in schema.messages) {
    cpp_file += `    case ${schema.messages[msg].id}:\n` +
    `        return units::${schema.messages[msg].source};\n` +
    `        break;\n`
}
cpp_file += "}\n}\n\n"


//generate target funtion
h_file += `enum units id_to_target(size_t id);`
cpp_file += 
`enum ${schema.config.name}::units ${schema.config.name}::id_to_target(size_t id){
switch(id) {\n`
for (let msg in schema.messages) {
    cpp_file += `    case ${schema.messages[msg].id}:\n` +
    `        return units::${schema.messages[msg].target};\n` +
    `        break;\n`
}
cpp_file += "}\n}\n\n"

h_file += `}` // close namespace

fs.writeFileSync(`${baseName}.h`, h_file)
fs.writeFileSync(`${baseName}.cpp`, cpp_file)
exec(`clang-format --style="LLVM" -i ${baseName}*`, ((error) => {
    if (error)
        console.log("install clang-format in PATH to format the output")
}))