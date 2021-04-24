/********************************
* GENERATED FILE DO NOT EDIT
********************************/

import struct from "./structjs/struct.mjs";

function scaledFloat_to_uint(value, scale) {
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

export const nodes = {
    web: 0,
    plant: 1,
}
export const fields = {
    SSID: 0,
    password: 1,
    plant_id: 2,
    lower_limit: 3,
    upper_limit: 4,
    humidity: 5,
}
export const messages = {
    wifi_config: 0,
    configure_plant: 1,
    get_active_plants: 2,
    get_humidity_measurement: 3,
    get_configuration: 4,
    active_plants: 5,
    humidity_measurement: 6,
    configuration: 7,
}
export const categories = {
    none: 0,
}
export class wifi_config_from_web_to_plant {
    constructor() {
        this._sender = nodes.web
        this._receiver = nodes.plant
        this._message = messages.wifi_config
        this._category = categories.none
        this._id = 0
        this._size = 128
        this._SSID = 0
        this._password = 0
    }
    get_sender() { return this._sender }
    get_receiver() { return this._receiver }
    get_message() { return this._message }
    get_id() { return this._id }
    get_size() { return this._size }
    get_category() { return this._category }
    set_SSID(value) {
        this._SSID = value
    }
    set_password(value) {
        this._password = value
    }
    build_buf() {
            let buf = new ArrayBuffer(128)
            let index = 0
        tmp += struct("<64s").pack_into(buf, index, this._SSID)
        index += 64
        tmp += struct("<64s").pack_into(buf, index, this._password)
        index += 64
        return buf
    }
    get_SSID() {
        return this._SSID
    }
    get_password() {
        return this._password
    }
    get_all_data() {
        data = []
        data.push({field: fields.SSID, value: this.get_SSID()})
        data.push({field: fields.password, value: this.get_password()})
        return data
    }
    parse_buf(buf) {
        index = 0
        this._SSID = struct("<64s").unpack_from(buf, index)[0]
        index += 64
        this._password = struct("<64s").unpack_from(buf, index)[0]
        index += 64
        return
    }
}
export class configure_plant_from_web_to_plant {
    constructor() {
        this._sender = nodes.web
        this._receiver = nodes.plant
        this._message = messages.configure_plant
        this._category = categories.none
        this._id = 1
        this._size = 17
        this._plant_id = 0
        this._lower_limit = 0
        this._upper_limit = 0
    }
    get_sender() { return this._sender }
    get_receiver() { return this._receiver }
    get_message() { return this._message }
    get_id() { return this._id }
    get_size() { return this._size }
    get_category() { return this._category }
    set_plant_id(value) {
        this._plant_id = value
    }
    set_lower_limit(value) {
        this._lower_limit = value
    }
    set_upper_limit(value) {
        this._upper_limit = value
    }
    build_buf() {
            let buf = new ArrayBuffer(17)
            let index = 0
        tmp += struct("<B").pack_into(buf, index, this._plant_id)
        index += 1
        tmp += struct("<d").pack_into(buf, index, this._lower_limit)
        index += 8
        tmp += struct("<d").pack_into(buf, index, this._upper_limit)
        index += 8
        return buf
    }
    get_plant_id() {
        return this._plant_id
    }
    get_lower_limit() {
        return this._lower_limit
    }
    get_upper_limit() {
        return this._upper_limit
    }
    get_all_data() {
        data = []
        data.push({field: fields.plant_id, value: this.get_plant_id()})
        data.push({field: fields.lower_limit, value: this.get_lower_limit()})
        data.push({field: fields.upper_limit, value: this.get_upper_limit()})
        return data
    }
    parse_buf(buf) {
        index = 0
        this._plant_id = struct("<B").unpack_from(buf, index)[0]
        index += 1
        this._lower_limit = struct("<d").unpack_from(buf, index)[0]
        index += 8
        this._upper_limit = struct("<d").unpack_from(buf, index)[0]
        index += 8
        return
    }
}
export class get_active_plants_from_web_to_plant {
    constructor() {
        this._sender = nodes.web
        this._receiver = nodes.plant
        this._message = messages.get_active_plants
        this._category = categories.none
        this._id = 2
        this._size = 0
    }
    get_sender() { return this._sender }
    get_receiver() { return this._receiver }
    get_message() { return this._message }
    get_id() { return this._id }
    get_size() { return this._size }
    get_category() { return this._category }
    build_buf() {
            let buf = new ArrayBuffer(0)
            let index = 0
        return buf
    }
    get_all_data() {
        data = []
        return data
    }
    parse_buf(buf) {
        index = 0
        return
    }
}
export class get_humidity_measurement_from_web_to_plant {
    constructor() {
        this._sender = nodes.web
        this._receiver = nodes.plant
        this._message = messages.get_humidity_measurement
        this._category = categories.none
        this._id = 3
        this._size = 1
        this._plant_id = 0
    }
    get_sender() { return this._sender }
    get_receiver() { return this._receiver }
    get_message() { return this._message }
    get_id() { return this._id }
    get_size() { return this._size }
    get_category() { return this._category }
    set_plant_id(value) {
        this._plant_id = value
    }
    build_buf() {
            let buf = new ArrayBuffer(1)
            let index = 0
        tmp += struct("<B").pack_into(buf, index, this._plant_id)
        index += 1
        return buf
    }
    get_plant_id() {
        return this._plant_id
    }
    get_all_data() {
        data = []
        data.push({field: fields.plant_id, value: this.get_plant_id()})
        return data
    }
    parse_buf(buf) {
        index = 0
        this._plant_id = struct("<B").unpack_from(buf, index)[0]
        index += 1
        return
    }
}
export class get_configuration_from_web_to_plant {
    constructor() {
        this._sender = nodes.web
        this._receiver = nodes.plant
        this._message = messages.get_configuration
        this._category = categories.none
        this._id = 4
        this._size = 1
        this._plant_id = 0
    }
    get_sender() { return this._sender }
    get_receiver() { return this._receiver }
    get_message() { return this._message }
    get_id() { return this._id }
    get_size() { return this._size }
    get_category() { return this._category }
    set_plant_id(value) {
        this._plant_id = value
    }
    build_buf() {
            let buf = new ArrayBuffer(1)
            let index = 0
        tmp += struct("<B").pack_into(buf, index, this._plant_id)
        index += 1
        return buf
    }
    get_plant_id() {
        return this._plant_id
    }
    get_all_data() {
        data = []
        data.push({field: fields.plant_id, value: this.get_plant_id()})
        return data
    }
    parse_buf(buf) {
        index = 0
        this._plant_id = struct("<B").unpack_from(buf, index)[0]
        index += 1
        return
    }
}
export class active_plants_from_plant_to_web {
    constructor() {
        this._sender = nodes.plant
        this._receiver = nodes.web
        this._message = messages.active_plants
        this._category = categories.none
        this._id = 5
        this._size = 0
    }
    get_sender() { return this._sender }
    get_receiver() { return this._receiver }
    get_message() { return this._message }
    get_id() { return this._id }
    get_size() { return this._size }
    get_category() { return this._category }
    build_buf() {
            let buf = new ArrayBuffer(0)
            let index = 0
        return buf
    }
    get_all_data() {
        data = []
        return data
    }
    parse_buf(buf) {
        index = 0
        return
    }
}
export class humidity_measurement_from_plant_to_web {
    constructor() {
        this._sender = nodes.plant
        this._receiver = nodes.web
        this._message = messages.humidity_measurement
        this._category = categories.none
        this._id = 6
        this._size = 9
        this._plant_id = 0
        this._humidity = 0
    }
    get_sender() { return this._sender }
    get_receiver() { return this._receiver }
    get_message() { return this._message }
    get_id() { return this._id }
    get_size() { return this._size }
    get_category() { return this._category }
    set_plant_id(value) {
        this._plant_id = value
    }
    set_humidity(value) {
        this._humidity = value
    }
    build_buf() {
            let buf = new ArrayBuffer(9)
            let index = 0
        tmp += struct("<B").pack_into(buf, index, this._plant_id)
        index += 1
        tmp += struct("<d").pack_into(buf, index, this._humidity)
        index += 8
        return buf
    }
    get_plant_id() {
        return this._plant_id
    }
    get_humidity() {
        return this._humidity
    }
    get_all_data() {
        data = []
        data.push({field: fields.plant_id, value: this.get_plant_id()})
        data.push({field: fields.humidity, value: this.get_humidity()})
        return data
    }
    parse_buf(buf) {
        index = 0
        this._plant_id = struct("<B").unpack_from(buf, index)[0]
        index += 1
        this._humidity = struct("<d").unpack_from(buf, index)[0]
        index += 8
        return
    }
}
export class configuration_from_plant_to_web {
    constructor() {
        this._sender = nodes.plant
        this._receiver = nodes.web
        this._message = messages.configuration
        this._category = categories.none
        this._id = 7
        this._size = 0
    }
    get_sender() { return this._sender }
    get_receiver() { return this._receiver }
    get_message() { return this._message }
    get_id() { return this._id }
    get_size() { return this._size }
    get_category() { return this._category }
    build_buf() {
            let buf = new ArrayBuffer(0)
            let index = 0
        return buf
    }
    get_all_data() {
        data = []
        return data
    }
    parse_buf(buf) {
        index = 0
        return
    }
}
export function id_to_message_class(id) {
    if (id == 0) {
        receiver = wifi_config_from_web_to_plant()
        return receiver
    }
    if (id == 1) {
        receiver = configure_plant_from_web_to_plant()
        return receiver
    }
    if (id == 2) {
        receiver = get_active_plants_from_web_to_plant()
        return receiver
    }
    if (id == 3) {
        receiver = get_humidity_measurement_from_web_to_plant()
        return receiver
    }
    if (id == 4) {
        receiver = get_configuration_from_web_to_plant()
        return receiver
    }
    if (id == 5) {
        receiver = active_plants_from_plant_to_web()
        return receiver
    }
    if (id == 6) {
        receiver = humidity_measurement_from_plant_to_web()
        return receiver
    }
    if (id == 7) {
        receiver = configuration_from_plant_to_web()
        return receiver
    }
}
