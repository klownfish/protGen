"use strict";

//required classes
//
//schema() - contains the protocol
/*******
 * datatypes
 ***********
 * double() -- native IEEE double
 * float() -- native IEEE float
 * int(size)
 * uint(size)
 * packedNum(size, min, max)
 * scaledNum(size, scale)
 * enum(name) - the name of the enum
 ********/

/********
 * modifiers
 ******
 * $variableLength(size) - read and int and the size of the next field will be 
 *                        overwritten with that int
 * source(size, enum) - prepend the string of the enum to the tree pos
 * position(size, enum) - append the string of the enum to the tree pos
 * index(size, max_len) - append the read index to the next field name
 */

class Schema {
    constructor() {
        this.enums = {};
        this.datatypes = {};
        this.messages = {};

        this.sourceDatatypeCombinations = []
    }

    decodeMsg(msg) {
        for (let key in msg.fields) {
            if (String(Number(key)) == key) {
                throw `Field names must not be or have the same structure as integers: ${key}`
            }
        }
        if (this.datatypes[msg.datatype] && (msg.fields || msg.bitField)) {
            throw `Redeclaration of datatype: ${msg.datatype}`;
        }
        let combined = msg.source + msg.datatype
        if (this.sourceDatatypeCombinations.indexOf(combined) != -1) {
            throw `Reused source + name combination: ${msg.source} and ${msg.datatype}`
        }
        if (!msg.datatype) {
            throw `Message has no datatype: id ${msg.id}`
        }
        if (!msg.source) {
            throw `Message has no source: id ${msg.id}`
        }
        this.sourceDatatypeCombinations.push(combined)

        let outDatatype = {};
        outDatatype = {}
        outDatatype["name"] = msg.datatype;
        if (msg.datatype.match(/[^A-Za-z0-9\-_]/)) {
            throw "only a-z, A-Z and '_' can be used in datatype names"
        }
        //extract fields
        outDatatype["fields"] = [];
        for (let key in msg.fields) {
            if (key.match(/[^A-Za-z0-9\-_]/)) {
                throw "only a-z, A-Z and '_' can be used in field names"
            }
            msg["fields"][key].name = key;
            outDatatype["fields"].push(msg["fields"][key]);
        }
        delete msg.fields;

        this.datatypes[outDatatype.name] = outDatatype
        //extracts bitField
        if (msg.bitField) {
            for (let bit of msg.bitField) {
                if (bit.match(/[^A-Za-z0-9\-_]/)) {
                    throw "only a-z, A-Z and '_' can be used in bit field names"
                }
            }
            outDatatype.bitField = msg.bitField;
            outDatatype.bitFieldSize = this.actualSizeToUintSize(Math.ceil(msg.bitField.length / 8))
            outDatatype.bitFieldNativeType = this.sizeToUint(outDatatype.bitFieldSize)
            delete msg.bitField;
        }

        //get total size of datatype
        let totalSize = 0;
        if (outDatatype.fields) {
            for (let v of outDatatype.fields) {
                totalSize += v.size
            }
        }
        if (outDatatype.bitField) {
            totalSize += outDatatype.bitFieldSize;
        }
        outDatatype.totalSize = totalSize
        return msg;
    }

    addMsg(msg) {
        msg = this.decodeMsg(msg)
        this.messages[msg.id] = msg;
    }

    addEnum(name, enumerator) {
        if (this.enums[name]) {
            throw `Duplicate enum name: ${name}`
        }

        let reversed = {};
        for (let v in enumerator) {
            let key = enumerator[v];
            reversed[key] = Number(v);
        } 
        enumerator = reversed;

        let obj = {}
        let enumSize = Object.entries(enumerator).length
        obj.name = name
        obj.entries = enumerator
        obj.size = Math.ceil(Math.log2(enumSize) / 8)
        obj.nativeType = this.sizeToUint(obj.size)
        this.enums[name] = obj;
    }

    getObject() {
        let obj = {
            enums: this.enums,
            messages: this.messages,
            datatypes: this.datatypes,
        };
        return obj;
    }

    createJson() {
        let obj = this.getObject()
        let raw = JSON.stringify(obj)
        let fs = require('fs');
        fs.writeFileSync('./out/json/protocol.json', raw)
    }

    verifyIntSize(size) {
        return size == this.actualSizeToUintSize(size)
    }
    
    actualSizeToUintSize(size) {
        if (size <= 0)
            return 0
        else if (size <= 1)
            return 1
        else if (size <= 2)
            return 2;
        else if (size <= 4)
            return 4;
        else if (size <= 8)
            return 8;
        else if (size <= 16)
            return 16;
    }
    
    sizeToUint(size) {
        if (size <= 0)
            return "void"
        else if (size <= 1)
            return "uint8_t"
        else if (size <= 2)
            return "uint16_t";
        else if (size <= 4)
            return "uint32_t";
        else if (size <= 8)
            return "uint64_t";
        else if (size <= 16)
            return "uint128_t";
    }
    
    double() {
        let obj = {
            type: "double",
            size: 8,
            nativeType: "double"
        };
        return obj;
    }
    
    float() {
        let obj = {
            type: "float",
            size: 4,
            nativeType: "float"
        }
        return obj;
    }
    
    int(size) {
        if (!this.verifyIntSize(size)) {
            throw `size can not be converted to an int: ${size}` 
        }
        let type = this.sizeToUint(size).substring(1);
        let obj = {
            type: "int",
            size: size,
            nativeType: type 
        }
        return obj;
    }
    
    uint(size) {
        if (!this.verifyIntSize(size)) {
            throw `size can not be converted to an int: ${size}` 
        }
        let obj = {
            type: "uint",
            size: size,
            nativeType: this.sizeToUint(size)
        }
        return obj;
    }
    
    packedFloat(size, min, max) {
        if (!this.verifyIntSize(size)) {
            throw `size can not be converted to an int: ${size}` 
        }
        let obj = {
            type: "packedFloat",
            size: size,
            min: min,
            max: max,
            nativeType: this.sizeToUint(size)
        }
        return obj
    }
    
    scaledFloat(size, scale) {
        if (!this.verifyIntSize(size)) {
            throw `size can not be converted to an int: ${size}` 
        }
        let obj = {
            type: "scaledFloat",
            size: size,
            scale: scale,
            nativeType: this.sizeToUint(size)
        }
        return obj
    }
    
    enumerator(name) {
        let obj = {
            type: "enum",
            enumName: name,
            nativeType: this.enums[name].nativeType,
            size: this.enums[name].size
        }
        return obj;
    }
}

exports.Schema = Schema