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
h_file += `//pick if you want to use floats or doubles\n`
h_file += `#define ${schema.config.name}_FLOAT_DEF float\n\n`
let float =`${schema.config.name}_FLOAT_DEF`
cpp_file +=
`#include <stdint.h>
#include "${schema.config.name}.h"\n\n`

h_file +=
`#include <stdint.h>
#include <string.h>
#include <math.h>\n\n`


h_file += `namespace  ${schema.config.name}{`
cpp_file += `namespace  ${schema.config.name}{`

//generate enums
for (let key in schema.enums) {
    let enumerator = schema.enums[key]
    h_file += `enum struct ${enumerator.name}: ${enumerator.nativeType}_t {\n`
    for (let index in enumerator.entries) {
        h_file += `    ${index} = ${enumerator.entries[index]},\n`
    }
    h_file += "};\n"
}

//hand written functions to encode / decode
h_file +=
`template <typename T>
void scaledFloat_to_uint(${float} value, ${float} scale, T* out) {
    *out = value * scale;
}

template <typename T>
void uint_to_scaledFloat(T value, ${float} scale, ${float}* out ) {
    *out = value / scale;
}

template <typename T>
void packedFloat_to_uint(${float}* value, ${float} minValue, ${float} maxValue, T* out){
    T intMax = ~0;
    if(value < minValue) {
      *out = 0;
      return;
    }
    if(value > maxValue) {
      *out = intMax;
      return;
    }
    ${float} ratio = (value - minValue) / (maxValue - minValue)
    return 1 + ((intMax - 2)) * ratio
}
  
template <typename T>
void uint_to_packedFloat(T value, ${float} minValue, ${float} maxValue, ${float}* out){
    T intMax = ~0;
    if(value <= 0) {
      *out = minValue - 1.0;
      return;
    }
    if(value >= intMax) {
      *out = maxValue + 1.0;
      return;
    }
    ${float} ratio = (value - 1) / (intMax - 2);
    *out = ratio * (maxValue - minValue) + minValue;
}

`

//generate senders
for (let key in schema.messages) {
    let msg = schema.messages[key]
    //class definition
    h_file +=
    `class ${msg.name}_from_${msg.source}_to_${msg.target} {\n` +
    `public:\n`
    //create fields
    for (let field of msg.fields) {
        if (field.type == "enum") {
            h_file += `enum ${field.enumName} ${field.name};\n`
            h_file += `static_assert((sizeof(${field.name}) == ${field.size}), "invalid size");\n`
            continue
        }
        if (field.type == "fixedString") {
            h_file += `char ${field.name}[${field.size}];\n`
            h_file += `static_assert((sizeof(${field.name}) == ${field.size}), "invalid size");\n`
            continue
        }
        h_file += `${field.nativeType}_t ${field.name};\n`
        h_file += `static_assert((sizeof(${field.name}) == ${field.size}), "invalid size");\n`
    }

    //create 
    if (msg.bitField) {
        h_file += `${msg.bitFieldNativeType}_t bit_field = 0;\n`
        h_file += `static_assert((sizeof(bit_field) == ${msg.bitFieldSize}), "invalid size");\n`
        for (let i = 0; i < msg.bitField.length; i++) {
            h_file += `void set_${msg.bitField[i]}(bool value) {\n` +
                `bit_field = value * (bit_field | (1 << ${i})) + !value * (bit_field & ~(1 << ${i}));\n` +
            `}\n`
            h_file += `bool get_${msg.bitField[i]}() {\n` +
                `return bit_field & (1 << ${i});\n` +
            `}\n`
        }
    }

    //know fields and getters
    h_file +=
    `uint8_t size = ${msg.totalSize};\n` +
    `enum messages message = messages::${msg.name};\n` +
    `enum units source = units::${msg.source};\n` +
    `enum units target = units::${msg.target};\n` +
    `uint8_t get_size() {return size;}\n` +
    `enum units get_source() {return source;}\n` +
    `enum units get_target() {return target;}\n` +
    `${schema.config.idNativeType}_t id = ${msg.id};\n` +
    `${schema.config.idNativeType}_t get_id() {return id;}\n`
    for (let field of msg.fields) {
        //setters
        switch(field.type) {
            case "packedFloat":
                h_file += 
                `void set_${field.name}(${schema.config.name}_FLOAT_DEF value) {\n` +
                `packedFloat_to_uint(value, ${field.min}, ${field.max}, &${field.name});\n` +
                `}\n`
                break;
            case "scaledFloat":
                h_file += 
                `void set_${field.name}(${schema.config.name}_FLOAT_DEF value) {\n` +
                `scaledFloat_to_uint(value, ${field.scale}, &${field.name});\n` +
                `}\n`
                break;
            case "enum":
                h_file += 
                `void set_${field.name}(enum ${field.enumName} value) {\n` +
                `${field.name} = value;\n`+
                `}\n`
                break;
            case "fixedString":
                h_file += 
                `void set_${field.name}(char* value) {\n` +
                `memcpy(${field.name}, value, sizeof(*${field.name}));\n`+
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
    //getters
    for (let field of msg.fields) {
        switch(field.type) {
            case "packedFloat":
                h_file += 
                `${schema.config.name}_FLOAT_DEF get_${field.name}() {\n` +
                `${schema.config.name}_FLOAT_DEF out;\n` +
                `uint_to_packedFloat(${field.name}, ${field.min}, ${field.max}, &out);\n` +
                `return out\n;`
                `}\n`
                break;
            case "scaledFloat":
                h_file += 
                `${schema.config.name}_FLOAT_DEF get_${field.name}() {\n` +
                `${schema.config.name}_FLOAT_DEF out;\n` +
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
            
            case "fixedString":
                h_file += 
                `char* get_${field.name}() {\n` +
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
    //build buf
    h_file += `void build_buf(uint8_t* buf, uint8_t* index) {\n` 
    if (msg.bitField) {
        h_file += `memcpy(buf + *index, &bit_field, sizeof(bit_field));\n`
        h_file += `*index += sizeof(bit_field);\n`
    }
    for (let field of msg.fields) {
        h_file += `memcpy(buf + *index, &${field.name}, sizeof(${field.name}));\n` 
        h_file += `*index += sizeof(${field.name});\n`  
    }

    h_file += `}\n`
    //parse buf
    h_file += `void parse_buf(uint8_t* buf) {\n`
    if (msg.fields.length || msg.bitField) {
        h_file += `uint8_t index = 0;\n` 
        if (msg.bitField) {
            h_file += `memcpy(&bit_field, buf +  index, sizeof(bit_field));\n`
            h_file += `index += sizeof(bit_field);\n`
        }
        for (let field of msg.fields) {
            h_file += `memcpy(&${field.name}, buf + index, sizeof(${field.name}));\n` 
            h_file += `index += sizeof(${field.name});\n`  
        }
    }
    h_file += `}\n`
    h_file += "};\n\n\n"
}

//generate receiving functions
for (let key in schema.messages) {
    let msg = schema.messages[key]
    cpp_file += `__attribute__((weak))\n`
    h_file += `void rx(${msg.name}_from_${msg.source}_to_${msg.target} msg);\n`
    cpp_file += `void rx(${msg.name}_from_${msg.source}_to_${msg.target} msg){}\n`
}

//generate parse function
h_file += `void parse_message(${schema.config.idNativeType}_t id, uint8_t* buf);`
cpp_file +=
`void parse_message(${schema.config.idNativeType}_t id, uint8_t* buf) {
    switch(id) { \n`
for (let key in schema.messages) {
    let msg = schema.messages[key]
    cpp_file += `    case ${msg.id}: {\n` +
    `        ${msg.name}_from_${msg.source}_to_${msg.target} __message;\n` +
    `        __message.parse_buf(buf);\n` +
    `        rx(__message);\n` +
    `        break;}\n`
}
cpp_file += "}\n"
cpp_file += "}\n\n"
//generate is_valid_id function
h_file += `bool is_valid_id(${schema.config.idNativeType}_t id);`
cpp_file += 
`bool is_valid_id(${schema.config.idNativeType}_t id){
switch(id) {\n`
for (let key in schema.messages) {
    let msg = schema.messages[key]
    cpp_file += `    case ${msg.id}:\n` +
    `        return true;\n` +
    `        break;\n`
}
cpp_file += `    default:`
cpp_file += `        return false;`
cpp_file += "}\n}\n\n"

//generate length function
h_file += `uint8_t id_to_len(${schema.config.idNativeType}_t id);`
cpp_file += 
`uint8_t id_to_len(${schema.config.idNativeType}_t id){
switch(id) {\n`
for (let key in schema.messages) {
    let msg = schema.messages[key]
    cpp_file += `    case ${msg.id}:\n` +
    `        return ${msg.totalSize};\n` +
    `        break;\n`
}
cpp_file += "default: return 0;"
cpp_file += "}\n}\n\n"

//generate source funtion
h_file += `enum units id_to_source(${schema.config.idNativeType}_t id);`
cpp_file += 
`enum units id_to_source(${schema.config.idNativeType}_t id){
switch(id) {\n`
for (let key in schema.messages) {
    let msg = schema.messages[key]
    cpp_file += `    case ${msg.id}:\n` +
    `        return units::${msg.source};\n` +
    `        break;\n`
}
cpp_file += "}\n}\n\n"


//generate target funtion
h_file += `enum units id_to_target(${schema.config.idNativeType}_t id);`
cpp_file += 
`enum units id_to_target(${schema.config.idNativeType}_t id){
switch(id) {\n`
for (let key in schema.messages) {
    let msg = schema.messages[key]
    cpp_file += `    case ${msg.id}:\n` +
    `        return units::${msg.target};\n` +
    `        break;\n`
}
cpp_file += "}\n}\n\n"


h_file += `}` // close namespace
cpp_file += `}` // close namespace

fs.writeFileSync(`${baseName}.h`, h_file)
fs.writeFileSync(`${baseName}.cpp`, cpp_file)
exec(`clang-format --style="LLVM" -i ${baseName}.cpp ${baseName}.h `, ((error) => {
    if (error)
        console.log("install clang-format in PATH to format the output", error)
}))