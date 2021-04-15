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
`################################
#GENERATED FILE DO NOT EDIT
################################`
let file = warning
file += write_line(0, "")
file += write_line(0, "")
file += write_line(0, "from enum import Enum")
file += write_line(0, "import struct")
file += write_line(0,"")

//hand written functions to decode
file +=
`def scaledFloat_to_uint(value, scale):
    return value * scale

def uint_to_scaledFloat(value, scale):
    return value / scale

def packedFloat_to_uint(value, min, max, size):
    max_value = (1 << size * 8) - 1
    difference = max - min
    return (value - min) / difference * max_value

def uint_to_packedFloat(value, min, max, size):
    max_value = (1 << size * 8) - 1
    difference = max - min
    return difference * value / max_value\n\n`

//generate enums
for (let key in schema.enums) {
    let enumerator = schema.enums[key]
    file += write_line(0, `class ${enumerator.name}(Enum):`)
    for (let index in enumerator.entries) {
        file += write_line(1, `${index} = ${enumerator.entries[index]}`)
    }
}

//generate senders
for(let key in schema.messages) {
    let msg = schema.messages[key]
    file += write_line(0, `class ${msg.name}_from_${msg.source}_to_${msg.target}:`)
    file += write_line(1, `def __init__(self):`)
    file += write_line(2, `self._source = units.${msg.source}`)
    file += write_line(2, `self._target = units.${msg.target}`)
    file += write_line(2, `self._message = messages.${msg.name}`)
    file += write_line(2, `self._id = ${msg.id}`)
    file += write_line(2, `self._size = ${msg.totalSize}`)
    //create fields
    if (msg.bitField) {
        file += write_line(2, `self._bit_field = 0`)
    }
    for (let field of msg.fields) {
        file += write_line(2, `self._${field.name} = 0`)
    }
    //create known getters
    file += write_line(1, "def get_source(self):")
    file += write_line(2, "return self._source")
    file += write_line(1, "def get_target(self):")
    file += write_line(2, "return self._target")
    file += write_line(1, "def get_message(self):")
    file += write_line(2, "return self._message")
    file += write_line(1, "def get_id(self):")
    file += write_line(2, "return self._id")
    file += write_line(1, "def get_size(self):")
    file += write_line(2, "return self._size")

    //create setters for bits
    if (msg.bitField) {
        for (let index in msg.bitField) {
            file += write_line(1, `def set_${msg.bitField[index]}(self, value):`)
            file += write_line(2, `self._bit_field =  value * (self._bit_field | (1 << ${index})) + (not value) * (self._bit_field & ~(1 << ${index}))`)
        }
    }
    //create setter for byte fields
    for (let field of msg.fields) {
        file += write_line(1, `def set_${field.name}(self, value):`)
        switch (field.type) {
            case "scaledFloat":
                file += write_line(2, `self._${field.name} = scaledFloat_to_uint(value, ${field.scale})`)
                break;
            case "packedFloat":
                file += write_line(2, `self._${field.name} = packedFloat_to_uint(value, ${field.min}, ${field.max}, ${field.size})`)
                break;
            case "enum":
                file += write_line(2, `self._${field.name} = value.value`)
                break;
            default:
                file += write_line(2, `self._${field.name} = value`)
        }
    }
    //generate buf
    file += write_line(1, `def build_buf(self):`)
    file += write_line(2, `buf = b""`)
    if (msg.bitField) {
        let bitType = structType[msg.bitFieldNativeType];
        file += write_line(2, `buf += struct.pack("<${bitType}", self._bit_field)`)
    }
    for (let field of msg.fields) {
        let type = field_to_struct(field)
        file += write_line(2, `buf += struct.pack("<${type}", self._${field.name})`)
    }
    file += write_line(2, `return buf`)

    if (msg.bitField) {
        for (let index in msg.bitField) {
            file += write_line(1, `def get_${msg.bitField[index]}(self):`)
            file += write_line(2, `return self._bit_field & (1 << ${index})`)
        }
    }
    for (let field of msg.fields) {
        file += write_line(1, `def get_${field.name}(self):`)
        switch (field.type) {
            case "scaledFloat":
                file += write_line(2, `return uint_to_scaledFloat(self._${field.name}, ${field.scale})`)
                break;
            case "packedFloat":
                file += write_line(2, `return uint_to_scaledFloat(self._${field.name}, ${field.min}, ${field.max}, ${field.size})`)
                break;
            case "enum":
                file += write_line(2, `return ${field.enumName}(self._${field.name})`)
                break;
            default:
                file += write_line(2, `return self._${field.name}`)
        }
    }

    //get all data
    file += write_line(1, `def get_all_data(self):`)
    file += write_line(2, `data = []`)
    if (msg.bitField) {
        for (let field of msg.bitField) {
            file += write_line(2, `data.append((fields.${field}, self.get_${field}()))`)
        }
    }
    for (let field of msg.fields) {
        file += write_line(2, `data.append((fields.${field.name}, self.get_${field.name}()))`)
    }
    file += write_line(2, `return data`)

    //parse buf
    file += write_line(1, `def parse_buf(self, buf):`)
    file += write_line(2, `index = 0`)
    if (msg.bitField) {
        let bitType = structType[msg.bitFieldNativeType];
        file += write_line(2, `self._bit_field = struct.unpack_from("<${bitType}", buf, index)[0]`)
        file += write_line(2, `index += ${msg.bitFieldSize}`)
    }
    for (let field of msg.fields) {
        let type = field_to_struct(field)
        file += write_line(2, `self._${field.name} = struct.unpack_from("<${type}", buf, index)[0]`)
        file += write_line(2, `index += ${field.size}`)
    }
    file += write_line(2, "return")
}

file += write_line(0, "def id_to_receiver(id):")
for(let key in schema.messages) {
    let message = schema.messages[key]
    file += write_line(1, `if id == ${message.id}:`)
    file += write_line(2, `receiver = ${message.name}_from_${message.source}_to_${message.target}()`)
    file += write_line(2, `return receiver`)
}

fs.writeFileSync(baseName + ".py", file)