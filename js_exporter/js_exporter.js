"use strict";
const { exec } = require("child_process");
let fs = require('fs');

function write_line(indent, str) {
    let out = ""
    for (let i = 0; i < indent; i++) {
        out += "    " //4spaces
    }
    out += str + "\n"
    return out
}

let structType = {
    "int8": "b",
    "uint8": "B",
    "int16": "h",
    "uint16": "H",
    "int32": "l",
    "uint32": "L",
    "int64": "q",
    "uint64": "Q",
    "float": "f",
    "double": "d"
}

function field_to_struct(field) {
    let type
    if (field.nativeType == "fixedString") {
        type = field.size + "s"  
    } else {
        type = structType[field.nativeType]
    }
    return type
}

if (process.argv.length < 4) {
    console.log(`usage: node INPUT_FILE OUTPUT_DIR`)
    return;
}
let input = process.argv[2]
let output = process.argv[3]
let raw = fs.readFileSync(input).toString()
let schema = JSON.parse(raw);
let baseName = output + `/${schema.config.name}`

let warning = 
`/********************************
* GENERATED FILE DO NOT EDIT
********************************/\n\n`
let file = warning

file += `import struct from "./structjs/struct.mjs";\n\n`
//hand written functions to decode
file +=
`function scaledFloat_to_uint(value, scale) {
    return value * scale
}

function uint_to_scaledFloat(value, scale) {
    return value / scale
}

function packedFloat_to_uint(value, minValue, maxValue, size) {
    let intMax = (1 << size * 8) - 1
    if(value < minValue)
      return 0
    if(value > maxValue)
      return intMax
    let ratio = (value - minValue) / (maxValue - minValue)
    return 1 + ((intMax - 2)) * ratio
}
  
function uint_to_packedFloat(value, minValue, maxValue, size) {
    let intMax = (1 << size * 8) - 1
    if(value <= 0)
      return minValue - 1.0
    if(value >= intMax)
      return maxValue + 1.0
    let ratio = (value - 1) / (intMax - 2)
    return ratio * (maxValue - minValue) + minValue
}

`

//generate enums
for (let key in schema.enums) {
    let enumerator = schema.enums[key]
    file += write_line(0, `export const ${enumerator.name} = {`)
    for (let index in enumerator.entries) {
        file += write_line(1, `${index}: ${enumerator.entries[index]},`)
    }
    file += write_line(0, "}")
}

//generate senders
for(let key in schema.messages) {
    let msg = schema.messages[key]
    file += write_line(0, `export class ${msg.name}_from_${msg.sender}_to_${msg.receiver} {`)
    file += write_line(1, `constructor() {`)
    file += write_line(2, `this._sender = nodes.${msg.sender}`)
    file += write_line(2, `this._receiver = nodes.${msg.receiver}`)
    file += write_line(2, `this._message = messages.${msg.name}`)
    file += write_line(2, `this._category = categories.${msg.category}`)
    
    file += write_line(2, `this._id = ${msg.id}`)
    file += write_line(2, `this._size = ${msg.totalSize}`)
    //create fields
    if (msg.bitField) {
        file += write_line(2, `this._bit_field = 0`)
    }
    for (let field of msg.fields) {
        file += write_line(2, `this._${field.name} = 0`)
    }
    file += write_line(1,"}")
    //create known getters
    file += write_line(1, "get_sender() { return this._sender }")
    file += write_line(1, "get_receiver() { return this._receiver }")
    file += write_line(1, "get_message() { return this._message }")
    file += write_line(1, "get_id() { return this._id }")
    file += write_line(1, "get_size() { return this._size }")
    file += write_line(1, "get_category() { return this._category }")

    //create setters for bits
    if (msg.bitField) {
        for (let index in msg.bitField) {
            file += write_line(1, `set_${msg.bitField[index]}(value)`)
            file += write_line(2, `this._bit_field =  value * (this._bit_field | (1 << ${index})) + (not value) * (this._bit_field & ~(1 << ${index}))`)
        }
    }
    //create setter for byte fields
    for (let field of msg.fields) {
        file += write_line(1, `set_${field.name}(value) {`)
        switch (field.type) {
            case "scaledFloat":
                file += write_line(2, `this._${field.name} = scaledFloat_to_uint(value, ${field.scale})`)
                break;
            case "packedFloat":
                file += write_line(2, `this._${field.name} = packedFloat_to_uint(value, ${field.min}, ${field.max}, ${field.size})`)
                break;
            case "enum":
                file += write_line(2, `this._${field.name} = value.value`)
                break;
            default:
                file += write_line(2, `this._${field.name} = value`)
        }
        file += write_line(1, `}`)
    }

    //generate buf
    file += write_line(1, `build_buf() {`)
    file += write_line(3, `let buf = new ArrayBuffer(${msg.totalSize})`)
    file += write_line(3, `let index = 0`)
    if (msg.bitField) {
        let bitType = structType[msg.bitFieldNativeType];
        file += write_line(2, `struct("<${bitType}").pack_into(buf, index, this._bit_field)`)
        file += write_line(2, `index += ${msg.bitFieldSize}`)
    }
    for (let field of msg.fields) {
        let type = field_to_struct(field)
        file += write_line(2, `tmp += struct("<${type}").pack_into(buf, index, this._${field.name})`)
        file += write_line(2, `index += ${field.size}`)
    }
    file += write_line(2, `return buf`)
    file += write_line(1, `}`)

    //getters
    if (msg.bitField) {
        for (let index in msg.bitField) {
            file += write_line(1, `get_${msg.bitField[index]}() {`)
            file += write_line(2, `return this._bit_field & (1 << ${index})`)
            file += write_line(1, `}`)
        }
    }
    for (let field of msg.fields) {
        file += write_line(1, `get_${field.name}() {`)
        switch (field.type) {
            case "scaledFloat":
                file += write_line(2, `return uint_to_scaledFloat(this._${field.name}, ${field.scale})`)
                break;
            case "packedFloat":
                file += write_line(2, `return uint_to_scaledFloat(this._${field.name}, ${field.min}, ${field.max}, ${field.size})`)
                break;
            case "enum":
                file += write_line(2, `return ${field.enumName}(this._${field.name})`)
                break;
            default:
                file += write_line(2, `return this._${field.name}`)
        }
        file += write_line(1, `}`)
    }

    //get all data
    file += write_line(1, `get_all_data() {`)
    file += write_line(2, `data = []`)
    if (msg.bitField) {
        for (let field of msg.bitField) {
            file += write_line(2, `data.push({field: fields.${field}, value: this.get_${field}()})`)
        }
    }
    for (let field of msg.fields) {
        file += write_line(2, `data.push({field: fields.${field.name}, value: this.get_${field.name}()})`)
    }
    file += write_line(2, `return data`)
    file += write_line(1, `}`)

    //parse buf
    file += write_line(1, `parse_buf(buf) {`)
    file += write_line(2, `index = 0`)
    if (msg.bitField) {
        let bitType = structType[msg.bitFieldNativeType];
        file += write_line(2, `this._bit_field = struct("<${bitType}").unpack_from(buf, index)[0]`)
        file += write_line(2, `index += ${msg.bitFieldSize}`)
    }
    for (let field of msg.fields) {
        let type = field_to_struct(field)
        file += write_line(2, `this._${field.name} = struct("<${type}").unpack_from(buf, index)[0]`)
        file += write_line(2, `index += ${field.size}`)
    }
    file += write_line(2, "return")
    file += write_line(1, `}`)
    file += write_line(0, `}`)
}

file += write_line(0, "export function id_to_message_class(id) {")
for(let key in schema.messages) {
    let message = schema.messages[key]
    file += write_line(1, `if (id == ${message.id}) {`)
    file += write_line(2, `receiver = ${message.name}_from_${message.sender}_to_${message.receiver}()`)
    file += write_line(2, `return receiver`)
    file += write_line(1, `}`)
}
file += write_line(0, `}`)

fs.writeFileSync(baseName + ".js", file)

try {
    fs.mkdirSync(output + "/structjs/")
} catch {}
fs.copyFileSync(__dirname + "/structjs/struct.mjs", output + "/structjs/struct.mjs")
fs.copyFileSync(__dirname + "/structjs/struct.mjs", output + "/structjs/LICENSE")