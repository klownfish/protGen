"use strict";

class Schema {
    constructor() {
        this.config = {
            name: "protGen",
            idNativeType: "uint8_t",
        };
        this.enums = {};
        this.datatypes = {};
        this.messages = {};

        this.unitsEnum = []
        this.datatypesEnum = []
        this.fieldsEnum = []
    }

    setIdType(type) {
        this.config.idNativeType =type 
    }

    setName(name) {
        this.config.name = name
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
        if (!msg.datatype) {
            throw `Message has no datatype: id ${msg.id}`
        }
        if (!msg.source) {
            throw `Message has no source: id ${msg.id}`
        }
        if (this.unitsEnum.indexOf(msg.source) == -1) {
            this.unitsEnum.push(msg.source);
        }
        if (this.unitsEnum.indexOf(msg.target) == -1) {
            this.unitsEnum.push(msg.target);
        }
        if (this.datatypesEnum.indexOf(msg.datatype) == -1) {
            this.datatypesEnum.push(msg.datatype);
        }

        let outDatatype = {};
        outDatatype = {}
        outDatatype["name"] = msg.datatype;
        if (msg.datatype.match(/[^A-Za-z0-9\-_]/)) {
            throw "only a-z, A-Z and '_' can be used in datatype names"
        }
        //extract fields
        outDatatype["fields"] = [];
        for (let key in msg.fields) {
            if (this.fieldsEnum.indexOf(key) == -1) {
                this.fieldsEnum.push(key);
            }
            if (key.match(/[^A-Za-z0-9\-_]/)) {
                throw "only a-z, A-Z and '_' can be used in field names"
            }
            msg["fields"][key].name = key;
            outDatatype["fields"].push(msg["fields"][key]);
        }
        delete msg.fields;

        if (!this.datatypes[outDatatype.name]) {
            this.datatypes[outDatatype.name] = outDatatype
        }
        //extracts bitField
        if (msg.bitField) {
            for (let bit of msg.bitField) {
                if (this.fieldsEnum.indexOf(bit) == -1) {
                    this.fieldsEnum.push(bit);
                }
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

    addEnum(name, enumerator, overwrite_error = false) {
        if (this.enums[name]) {
            throw `Duplicate enum name: ${name}`
        }
        if (name == "units" && !overwrite_error) {
            throw "reserved enum name: units"
        }
        if (name == "datatypes" && !overwrite_error) {
            throw "reserved enum name: datatypes"
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
        this.addEnum("units", this.unitsEnum, true);
        this.addEnum("datatypes", this.datatypesEnum, true);
        this.addEnum("fields", this.fieldsEnum, true);
        
        let obj = {
            config: this.config,
            enums: this.enums,
            datatypes: this.datatypes,
            messages: this.messages,
        };
        return obj;
    }

    createJson(path) {
        let obj = this.getObject()
        let raw = JSON.stringify(obj, null, 4)
        let fs = require('fs');
        fs.writeFileSync(path, raw)
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
            return "uint8"
        else if (size <= 2)
            return "uint16";
        else if (size <= 4)
            return "uint32";
        else if (size <= 8)
            return "uint64";
        else if (size <= 16)
            return "uint128";
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
    
    scaledFloat(size, scale, signed) {
        if (!this.verifyIntSize(size)) {
            throw `size can not be converted to an int: ${size}` 
        }
        let type = this.sizeToUint(size)

        if (signed) {
            type = type.substring(1)
        }
        let obj = {
            type: "scaledFloat",
            size: size,
            scale: scale,
            nativeType: type
        }
        return obj
    }
    
    enumerator(name) {
        if (this.enums.indexOf(name) == -1) {
            throw `undefined enum: ${name}`
        }
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