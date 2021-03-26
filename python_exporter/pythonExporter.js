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
    let message = schema.messages[key]
    let datatype = schema.datatypes[message.datatype]
    file += write_line(0, `class ${message.datatype}_from_${message.source}_to_${message.target}:`)
    file += write_line(1, `def __init__(self):`)
    file += write_line(2, `self._source = units.${message.source}`)
    file += write_line(2, `self._target = units.${message.target}`)
    file += write_line(2, `self._datatype = datatypes.${message.datatype}`)
    file += write_line(2, `self._id = ${message.id}`)
    file += write_line(2, `self._size = ${datatype.totalSize}`)
    //create fields
    if (datatype.bitField) {
        file += write_line(2, `self._bit_field = 0`)
    }
    for (let field of datatype.fields) {
        file += write_line(2, `self._${field.name} = 0`)
    }
    //create known getters
    file += write_line(1, "def get_source(self):")
    file += write_line(2, "return self._source")
    file += write_line(1, "def get_target(self):")
    file += write_line(2, "return self._target")
    file += write_line(1, "def get_datatype(self):")
    file += write_line(2, "return self._datatype")
    file += write_line(1, "def get_id(self):")
    file += write_line(2, "return self._id")
    file += write_line(1, "def get_size(self):")
    file += write_line(2, "return self._size")
    //create setters for bits
    if (datatype.bitField) {
        for (let index in datatype.bitField) {
            file += write_line(1, `def set_${datatype.bitField[index]}(self, value):`)
            file += write_line(2, `self._bit_field =  value * (self._bit_field | (1 << ${index})) + (not value) * (self._bit_field & ~(1 << ${index}))`)
        }
    }
    //create setter for byte fields
    for (let field of datatype.fields) {
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
    file += write_line(1, `def get_buf(self):`)
    file += write_line(2, `buf = b""`)
    if (datatype.bitField) {
        let bitType = structType[datatype.bitFieldNativeType];
        file += write_line(2, `buf += struct.pack("<${bitType}", self._bit_field)`)
    }
    for (let field of datatype.fields) {
        let type = structType[field.nativeType]
        file += write_line(2, `buf += struct.pack("<${type}", self._${field.name})`)
    }
    file += write_line(2, `return buf`)
}


//generate receivers
for(let key in schema.messages) {
    let message = schema.messages[key]
    let datatype = schema.datatypes[message.datatype]
    file += write_line(0, `class ${message.datatype}:`)
    file += write_line(1, `def __init__(self):`)
    file += write_line(2, `self._source = 0`)
    file += write_line(2, `self._target = 0`)
    file += write_line(2, `self._datatype = 0`)
    file += write_line(2, `self._id = 0`)
    file += write_line(2, `self._size = ${datatype.totalSize}`)
    //create fields
    if (datatype.bitField) {
        file += write_line(2, `self._bit_field = 0`)
    }
    for (let field of datatype.fields) {
        file += write_line(2, `self._${field.name} = 0`)
    }
    //setters
    file += write_line(1, "def set_source(self, value):")
    file += write_line(2, "self._source = value")
    file += write_line(1, "def set_target(self, value):")
    file += write_line(2, "self._target = value")
    file += write_line(1, "def set_datatype(self, value):")
    file += write_line(2, "self._datatype = value")
    file += write_line(1, "def set_id(self, value):")
    file += write_line(2, "self._id = value")
    //getters
    file += write_line(1, "def get_source(self):")
    file += write_line(2, "return self._source")
    file += write_line(1, "def get_target(self):")
    file += write_line(2, "return self._target")
    file += write_line(1, "def get_datatype(self):")
    file += write_line(2, "return self._datatype")
    file += write_line(1, "def get_size(self):")
    file += write_line(2, "return self._size")
    file += write_line(1, "def get_id(self):")
    file += write_line(2, "return self._id")
    if (datatype.bitField) {
        for (let index in datatype.bitField) {
            file += write_line(1, `def get_${datatype.bitField[index]}(self):`)
            file += write_line(2, `return self._bit_field & (1 << ${index})`)
        }
    }
    for (let field of datatype.fields) {
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
    if (datatype.bitField) {
        for (let field of datatype.bitField) {
            file += write_line(2, `data.append((fields.${field}, self.get_${field}()))`)
        }
    }
    for (let field of datatype.fields) {
        file += write_line(2, `data.append((fields.${field.name}, self.get_${field.name}()))`)
    }
    file += write_line(2, `return data`)
    //parse buf
    file += write_line(1, `def parse_buf(self, buf):`)
    file += write_line(2, `index = 0`)
    if (datatype.bitField) {
        let bitType = structType[datatype.bitFieldNativeType];
        file += write_line(2, `self._bit_field = struct.unpack_from("<${bitType}", buf, index)[0]`)
        file += write_line(2, `index += ${datatype.bitFieldSize}`)
    }
    for (let field of datatype.fields) {
        let type = structType[field.nativeType]
        file += write_line(2, `self._${field.name} = struct.unpack_from("<${type}", buf, index)[0]`)
        file += write_line(2, `index += ${field.size}`)
    }
    file += write_line(2, "return")
}

file += write_line(0, "def id_to_receiver(id):")
for(let key in schema.messages) {
    let message = schema.messages[key]
    file += write_line(1, `if id == ${message.id}:`)
    file += write_line(2, `receiver = ${message.datatype}()`)
    file += write_line(2, `receiver.set_id(${message.id})`)
    file += write_line(2, `receiver.set_target(units.${message.target})`)
    file += write_line(2, `receiver.set_source(units.${message.source})`)
    file += write_line(2, `receiver.set_datatype(datatypes.${message.datatype})`)
    file += write_line(2, `return receiver`)
}

fs.writeFileSync(baseName + ".py", file)