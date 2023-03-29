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
let c_file = warning
h_file += `#ifndef _${schema.config.name}_H\n`
h_file += `#define _${schema.config.name}_H\n`

h_file += `//if you want to use floats or doubles\n`
h_file += `#define ${schema.config.name}_FLOAT_DEF float\n\n`
let float =`${schema.config.name}_FLOAT_DEF`

h_file +=
`#include <stdint.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>\n\n`

c_file +=
`#include <stdint.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

#include "${schema.config.name}.h"\n\n`

//generate enums
for (let key in schema.enums) {
    let enumerator = schema.enums[key]
    h_file += `enum ${enumerator.name}{\n`
    for (let index in enumerator.entries) {
        h_file += `    ${schema.config.name}_${enumerator.name}_${index} = ${enumerator.entries[index]},\n`
    }
    h_file += "};\n"
}

//generate IDs
for (let key in schema.messages) {
    let msg = schema.messages[key];
    h_file += `#define ${schema.config.name}_id_${msg.name} ${msg.id}\n`
}

//generate lengths
for (let key in schema.messages) {
    let msg = schema.messages[key];
    h_file += `#define ${schema.config.name}_len_${msg.name} ${msg.totalSize}\n`
}

//generate structs
for (let key in schema.messages) {
    let msg = schema.messages[key];
    
    h_file += `struct ${schema.config.name}_${msg.name} {\n`
    if (msg.bitField) {
        h_file += `${msg.bitFieldNativeType}_t bit_field;\n`
    }
    for (let field of msg.fields) {
        switch (field.type) {
            case "float":
            case "packedFloat":
            case "scaledFloat":
                h_file += `${float} ${field.name}`
                break
            case "fixedBytes":
                h_file += `uint8_t *${field.name}`
                break;
            default:
                h_file += `${field.nativeType}_t ${field.name}`
                break;
        }
        h_file += ";\n"
    }
    h_file += `};\n`
}

//hand written functions to encode / decode
h_file +=
`#define scaledFloat_to_uint(value, scale, out)\
    out = value * scale;\


#define uint_to_scaledFloat(value, scale, out)\
    value / scale;\

#define packedFloat_to_uint(value, minValue, maxValue, out){\
    uint64_t intMax = 1 << ((sizeof(out) * 8) - 1);\
    if(value < minValue) {\
        out = 0;\
    }\
    else if(value > maxValue) {\
        out = intMax;\
    }\
    else {\
        ${float} ratio = (value - minValue) / (maxValue - minValue);\
        out = 1 + ((intMax - 2)) * ratio;\
    }\
}
  
#define uint_to_packedFloat(value, minValue, maxValue, out) {\
    uint64_t intMax = 1 << ((sizeof(out) * 8) - 1);\
    if(value <= 0) {\
        out = minValue - 1.0;\
    }\
    else if(value >= intMax) {\
        out = maxValue + 1.0;\
    } else {\
        ${float} ratio = (value - 1) / (intMax - 2);\
        out = ratio * (maxValue - minValue) + minValue;\
    }\
}
`

//generate functions
for (let key in schema.messages) {
    let msg = schema.messages[key]

    //generate builder
    h_file += `void ${schema.config.name}_build_${msg.name}(uint8_t* buf, struct ${schema.config.name}_${msg.name} data);`
    c_file += `void ${schema.config.name}_build_${msg.name}(uint8_t* buf, struct ${schema.config.name}_${msg.name} data) {\n`
    let index = 0 
    if (msg.bitField) {
        c_file += `memcpy(buf, &bit_field, ${msg.biFieldSize});`
        index += msg.biFieldSize
    }
    for (let field of msg.fields) {
        switch (field.type) {
            case "int":
            case "uint":
            case "enum":
            case "float":
                c_file += `memcpy(buf + ${index}, &data.${field.name}, ${field.size});\n`
                break
            case "fixedBytes":
                c_file += `memcpy(buf + ${index}, data.${field.name}, ${field.size});\n`
                break;
            case "packedFloat":
                c_file += `${field.nativeType}_t temp_${field.name};\n` +
                `packedFloat_to_uint(data.${field.name}, ${field.min}, ${field.max}, temp_${field.name});\n` +
                `memcpy(buf + ${index}, &temp_${field.name}, ${field.size});\n`
                break;
            case "scaledFloat":
                c_file += `${field.nativeType}_t temp_${field.name};\n` +
                `scaledFloat_to_uint(data.${field.name}, ${field.scale}, temp_${field.name}\n);` +
                `memcpy(buf + ${index}, &temp_${field.name}, ${field.size});\n`
                break;                
        }
        index += field.size
    }
    c_file += "}\n"

    //generate RX
    h_file += `void ${schema.config.name}_rx_${msg.name}(struct ${schema.config.name}_${msg.name} data);\n`
    c_file += `void __attribute__((weak)) ${schema.config.name}_rx_${msg.name}(struct ${schema.config.name}_${msg.name} data) {}\n`
}


//generate parse
h_file += `void ${schema.config.name}_parse(${schema.config.idNativeType}_t id, uint8_t *buf);`
c_file += `void ${schema.config.name}_parse(${schema.config.idNativeType}_t id, uint8_t *buf) {\n`
for (let key in schema.messages) {
    let msg = schema.messages[key]
    let index = 0;
    c_file += `if (id == ${msg.id}) {`
    c_file += `struct ${schema.config.name}_${msg.name} data;`

    if (msg.bitField) {
        c_file += `memcpy(&data.bit_field, buf, ${msg.biFieldSize});`
        index += msg.biFieldSize
    }

    for (let field of msg.fields) {
        switch (field.type) {
            case "int":
            case "uint":
            case "enum":
            case "float":
                c_file += `memcpy(&data.${field.name}, buf + ${index}, ${field.size});\n`
                break
            case "fixedBytes":
                c_file += `data.${field.name} = buf + ${index};\n`
                break;
            case "packedFloat":
                c_file += `${float} temp_${field.name};\n` +
                `memcpy(&temp_${field.name}, buf + ${index}, ${field.size});\n`+
                `uint_to_packedFloat(temp_${field.name}, ${field.min}, ${field.max}, data.${field.name});\n`
                break;
            case "scaledFloat":
                c_file += `${float} temp_${field.name};\n` +
                `memcpy(&temp_${field.name}, buf + ${index}, ${field.size});\n` +
                `scaledFloat_to_uint(temp_${field.name}, ${field.scale}, data.${field.name}\n);`
                break;                
        }
        index += field.size
    }
    c_file += `${schema.config.name}_rx_${msg.name}(data);\n`
    c_file += "}\n"
}
c_file += "}\n"

//generate is_valid_id function
c_file += 
`bool ${schema.config.name}_is_valid_id(${schema.config.idNativeType}_t id){
switch(id) {\n`
for (let key in schema.messages) {
    let msg = schema.messages[key]
    if (msg.duplicate) continue;
    c_file += `    case ${msg.id}:\n` +
    `        return true;\n` +
    `        break;\n`
}
c_file += `    default:\n`
c_file += `        return false;\n`
c_file += "}\n}\n\n"

//generate length functio
h_file += `uintmax_t ${schema.config.name}_id_to_len(${schema.config.idNativeType}_t id);`
c_file += 
`uintmax_t ${schema.config.name}_id_to_len(${schema.config.idNativeType}_t id){
switch(id) {\n`
for (let key in schema.messages) {
    let msg = schema.messages[key]
    if (msg.duplicate) continue;
    c_file += `    case ${msg.id}:\n` +
    `        return ${msg.totalSize};\n` +
    `        break;\n`
}
c_file += "default: return 0;"
c_file += "}\n}\n\n"


h_file += `#endif\n`

fs.writeFileSync(`${baseName}.h`, h_file)
fs.writeFileSync(`${baseName}.c`, c_file)

exec(`clang-format --style="LLVM" -i ${baseName}.c ${baseName}.h `, ((error) => {
    if (error)
        console.log("install clang-format in PATH to format the output", error)
}))