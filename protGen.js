"use strict";

class Schema {
    constructor() {
        this.config = {
            name: "protGen",
            idNativeType: "uint32",
        };
        this.enums = {};
        this.messages = [];

        this.validFields = [
            "sender",
            "receiver",
            "fields",
            "id",
            "name",
            "bitField",
            "category"
        ]

        this.currentId = -1;
        this.usedIds = []

        this.nodesEnum = []
        this.messageNamesEnum = []
        this.fieldsEnum = []
        this.categoriesEnum = []
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
        if (!msg.name) {
            throw `Message has no name: id ${msg.id}`
        }
        if (!msg.sender) {
            throw `Message has no sender: name ${msg.name}`
        }
        if (!msg.receiver) {
            throw `Message has no receiver: name ${msg.name}`
        }
        if (!msg.category) {
            msg.category = "none"
        }
        if (this.nodesEnum.indexOf(msg.sender) == -1) {
            this.nodesEnum.push(msg.sender);
        }
        if (this.nodesEnum.indexOf(msg.receiver) == -1) {
            this.nodesEnum.push(msg.receiver);
        }
        if (this.messageNamesEnum.indexOf(msg.name) == -1) {
            this.messageNamesEnum.push(msg.name);
        }
        if (this.categoriesEnum.indexOf(msg.category) == -1) {
            this.categoriesEnum.push(msg.category);
        }

        for (let field in msg) {
            let valid = false;
            for (let name of this.validFields) {
                if (field == name) {
                    valid = true
                }
            }
            if (!valid) {
                throw `invalid field in message: message ${msg.name} field ${field}`
            }
        }

        let outMsg = {}
        if (msg.category) {
            outMsg.category = msg.category
        }
        if (msg.description) {
            outMsg.description = msg.description
        }
        if (msg.id != null) {
            outMsg.id = msg.id
            if (this.usedIds.indexOf(outMsg.id) != -1) {
                console.log(`Duplicate ID: this is either and error or you know what you are doing: ID ${outMsg.id}`)
                outMsg.duplicate = true
            }
        } else {
            while (this.usedIds.indexOf(++this.currentId) != -1) {}
            outMsg.id = this.currentId
        }
        this.usedIds.push(outMsg.id);
        //copy misc
        outMsg.name = msg.name
        outMsg.receiver = msg.receiver
        outMsg.sender = msg.sender

        //copy datatype
        outMsg["name"] = msg.name;
        if (outMsg.name.match(/[^A-Za-z0-9\-_]/)) {
            throw "only a-z, A-Z and '_' can be used in names"
        }
        //extract fields
        outMsg["fields"] = [];
        for (let key in msg.fields) {
            if (this.fieldsEnum.indexOf(key) == -1) {
                this.fieldsEnum.push(key);
            }
            if (key.match(/[^A-Za-z0-9\-_]/)) {
                throw "only a-z, A-Z and '_' can be used in names"
            }
            msg["fields"][key].name = key;
            outMsg["fields"].push(msg["fields"][key]);
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
            outMsg.bitField = msg.bitField;
            outMsg.bitFieldSize = this.actualSizeToUintSize(Math.ceil(msg.bitField.length / 8))
            outMsg.bitFieldNativeType = this.sizeToUint(outMsg.bitFieldSize)
        }

        //get total size of datatype
        let totalSize = 0;
        if (outMsg.fields) {
            for (let v of outMsg.fields) {
                totalSize += v.size
            }
        }
        if (outMsg.bitField) {
            totalSize += outMsg.bitFieldSize;
        }
        outMsg.totalSize = totalSize
        return outMsg;
    }

    addMsg(msg) {
        msg = this.decodeMsg(msg)
        this.messages.push(msg);
    }

    addEnum(name, enumerator, overwrite_error = false) {
        if (this.enums[name]) {
            throw `Duplicate enum name: ${name}`
        }
        if (name == "nodes" && !overwrite_error) {
            throw "reserved enum name: nodes"
        }
        if (name == "messages" && !overwrite_error) {
            throw "reserved enum name: messages"
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
        obj.size = Math.ceil(Math.log2(enumSize + 1) / 8)
        obj.nativeType = this.sizeToUint(obj.size)
        this.enums[name] = obj;
    }

    getObject() {
        this.addEnum("nodes", this.nodesEnum, true);
        this.addEnum("fields", this.fieldsEnum, true);
        this.addEnum("messages", this.messageNamesEnum, true);
        this.addEnum("categories", this.categoriesEnum, true);

        let realEnums = []
        for (let v in this.enums) {
            realEnums.push(this.enums[v])
        }

        let obj = {
            config: this.config,
            enums: realEnums,
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
    
    fixedString(max_len) {
        let obj = {
            type: "fixedString",
            size: max_len, //account for null terminator
            nativeType: "fixedString"
        }
        return obj;
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
        if (this.enums[name] == null) {
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