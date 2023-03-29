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
h_file += `#ifndef _${schema.config.name}_H\n`
h_file += `#define _${schema.config.name}_H\n`

h_file += `//if you want to use floats or doubles\n`
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
void packedFloat_to_uint(${float} value, ${float} minValue, ${float} maxValue, T* out){
    T intMax = ~0;
    if(value < minValue) {
      *out = 0;
      return;
    }
    if(value > maxValue) {
      *out = intMax;
      return;
    }
    ${float} ratio = (value - minValue) / (maxValue - minValue);
    *out = 1 + ((intMax - 2)) * ratio;
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


class MessageBase {
    public:
        virtual void build_buf(uint8_t *buf, uint8_t *index){}
        virtual void parse_buf(uint8_t *buf){}
        virtual ${schema.config.idNativeType}_t get_id(){}
        virtual enum categories get_category(){}
        virtual enum nodes get_receiver(){}
        virtual enum nodes get_sender(){}
        virtual uint8_t get_size(){}
};
`

//generate senders
for (let key in schema.messages) {
    let msg = schema.messages[key]
    //class definition
    h_file +=
    `class ${msg.name}_from_${msg.sender}_to_${msg.receiver}: public MessageBase {\n` +
    `public:\n`
    //create fields
    for (let field of msg.fields) {
        if (field.type == "enum") {
            h_file += `enum ${field.enumName} ${field.name};\n`
            h_file += `static_assert((sizeof(${field.name}) == ${field.size}), "invalid size");\n`
            continue
        }
        if (field.type == "fixedBytes") {
            h_file += `uint8_t ${field.name}[${field.size}];\n`
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
    `enum ${schema.config.name}::messages message = ${schema.config.name}::messages::${msg.name};\n` +
    `enum ${schema.config.name}::nodes sender = ${schema.config.name}::nodes::${msg.sender};\n` +
    `enum ${schema.config.name}::nodes receiver = ${schema.config.name}::nodes::${msg.receiver};\n` +
    `enum ${schema.config.name}::categories category = ${schema.config.name}::categories::${msg.category};\n` +
    `${schema.config.idNativeType}_t id = ${msg.id};\n` +

    `enum categories get_category() override { return category;}\n` +
    `uint8_t get_size() override { return size; }\n` +
    `enum nodes get_sender() override { return sender; }\n` +
    `enum nodes get_receiver() override { return receiver; }\n` +
    `${schema.config.idNativeType}_t get_id() override { return id; }\n`

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
            case "fixedBytes":
                h_file +=
                `void set_${field.name}(uint8_t* value) {\n` +
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
                `return out\n;` +
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
            case "fixedBytes":
                h_file +=
                `void get_${field.name}(uint8_t *buf) {\n` +
                `memcpy(buf, ${field.name}, sizeof(${field.name});\n`+
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
    h_file += `void build_buf(uint8_t* buf, uint8_t* index) override {\n`
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
    h_file += `void parse_buf(uint8_t* buf) override {\n`
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

//generate callback functions
for (let key in schema.messages) {
    let msg = schema.messages[key]
    if (msg.duplicate) continue;
    cpp_file += `__attribute__((weak))\n`
    h_file += `void rx(${msg.name}_from_${msg.sender}_to_${msg.receiver} msg);\n`
    cpp_file += `void rx(${msg.name}_from_${msg.sender}_to_${msg.receiver} msg){}\n`

    cpp_file += `__attribute__((weak))\n`
    h_file += `void rx(${msg.name}_from_${msg.sender}_to_${msg.receiver} msg, void* misc);\n`
    cpp_file += `void rx(${msg.name}_from_${msg.sender}_to_${msg.receiver} msg, void* misc){}\n`
}

//generate parse function
h_file += `void parse_message(${schema.config.idNativeType}_t id, uint8_t* buf);`
cpp_file +=
`void parse_message(${schema.config.idNativeType}_t id, uint8_t* buf) {
    switch(id) { \n`
for (let key in schema.messages) {
    let msg = schema.messages[key]
    if (msg.duplicate) continue;
    cpp_file += `    case ${msg.id}: {\n` +
    `        ${msg.name}_from_${msg.sender}_to_${msg.receiver} __message;\n` +
    `        __message.parse_buf(buf);\n` +
    `        rx(__message);\n` +
    `        break;}\n`
}
cpp_file += "}\n"
cpp_file += "}\n\n"

//generate parse function with void pointer
h_file += `void parse_message(${schema.config.idNativeType}_t id, uint8_t* buf, void* misc);`
cpp_file +=
`void parse_message(${schema.config.idNativeType}_t id, uint8_t* buf, void* misc) {
    switch(id) { \n`
for (let key in schema.messages) {
    let msg = schema.messages[key]
    if (msg.duplicate) continue;
    cpp_file += `    case ${msg.id}: {\n` +
    `        ${msg.name}_from_${msg.sender}_to_${msg.receiver} __message;\n` +
    `        __message.parse_buf(buf);\n` +
    `        rx(__message, misc);\n` +
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
    if (msg.duplicate) continue;
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
    if (msg.duplicate) continue;
    cpp_file += `    case ${msg.id}:\n` +
    `        return ${msg.totalSize};\n` +
    `        break;\n`
}
cpp_file += "default: return 0;"
cpp_file += "}\n}\n\n"

//generate sender funtion
h_file += `enum nodes id_to_sender(${schema.config.idNativeType}_t id);`
cpp_file +=
`enum nodes id_to_sender(${schema.config.idNativeType}_t id){
switch(id) {\n`
for (let key in schema.messages) {
    let msg = schema.messages[key]
    if (msg.duplicate) continue;
    cpp_file += `    case ${msg.id}:\n` +
    `        return nodes::${msg.sender};\n` +
    `        break;\n`
}
cpp_file += "}\n}\n\n"


//generate receiver funtion
h_file += `enum nodes id_to_receiver(${schema.config.idNativeType}_t id);`
cpp_file +=
`enum nodes id_to_receiver(${schema.config.idNativeType}_t id){
switch(id) {\n`
for (let key in schema.messages) {
    let msg = schema.messages[key]
    if (msg.duplicate) continue;
    cpp_file += `    case ${msg.id}:\n` +
    `        return nodes::${msg.receiver};\n` +
    `        break;\n`
}
cpp_file += "}\n}\n\n"

//generate category funtion
h_file += `enum categories id_to_category(${schema.config.idNativeType}_t id);`
cpp_file +=
`enum categories id_to_category(${schema.config.idNativeType}_t id){
switch(id) {\n`
for (let key in schema.messages) {
    let msg = schema.messages[key]
    if (msg.duplicate) continue;
    cpp_file += `    case ${msg.id}:\n` +
    `        return categories::${msg.category};\n` +
    `        break;\n`
}
cpp_file += "}\n}\n\n"

h_file += `}` // close namespace
cpp_file += `}` // close namespace
h_file += `#endif\n`


fs.writeFileSync(`${baseName}.h`, h_file)
fs.writeFileSync(`${baseName}.cpp`, cpp_file)
exec(`clang-format --style="LLVM" -i ${baseName}.cpp ${baseName}.h `, ((error) => {
    if (error)
        console.log("install clang-format in PATH to format the output", error)
}))