/* for struct library
The MIT License (MIT)

Copyright (c) 2016 Aksel Jensen (TheRealAksel at github)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

/*eslint-env es6*/
const rechk = /^([<>])?(([1-9]\d*)?([xcbB?hHiIfdsp]))*$/
const refmt = /([1-9]\d*)?([xcbB?hHiIfdsp])/g
const str = (v,o,c) => String.fromCharCode(
    ...new Uint8Array(v.buffer, v.byteOffset + o, c))
const rts = (v,o,c,s) => new Uint8Array(v.buffer, v.byteOffset + o, c)
    .set(s.split('').map(str => str.charCodeAt(0)))
const pst = (v,o,c) => str(v, o + 1, Math.min(v.getUint8(o), c - 1))
const tsp = (v,o,c,s) => { v.setUint8(o, s.length); rts(v, o + 1, c - 1, s) }
const lut = le => ({
    x: c=>[1,c,0],
    c: c=>[c,1,o=>({u:v=>str(v, o, 1)      , p:(v,c)=>rts(v, o, 1, c)     })],
    '?': c=>[c,1,o=>({u:v=>Boolean(v.getUint8(o)),p:(v,B)=>v.setUint8(o,B)})],
    b: c=>[c,1,o=>({u:v=>v.getInt8(   o   ), p:(v,b)=>v.setInt8(   o,b   )})],
    B: c=>[c,1,o=>({u:v=>v.getUint8(  o   ), p:(v,B)=>v.setUint8(  o,B   )})],
    h: c=>[c,2,o=>({u:v=>v.getInt16(  o,le), p:(v,h)=>v.setInt16(  o,h,le)})],
    H: c=>[c,2,o=>({u:v=>v.getUint16( o,le), p:(v,H)=>v.setUint16( o,H,le)})],
    i: c=>[c,4,o=>({u:v=>v.getInt32(  o,le), p:(v,i)=>v.setInt32(  o,i,le)})],
    I: c=>[c,4,o=>({u:v=>v.getUint32( o,le), p:(v,I)=>v.setUint32( o,I,le)})],
    f: c=>[c,4,o=>({u:v=>v.getFloat32(o,le), p:(v,f)=>v.setFloat32(o,f,le)})],
    d: c=>[c,8,o=>({u:v=>v.getFloat64(o,le), p:(v,d)=>v.setFloat64(o,d,le)})],
    s: c=>[1,c,o=>({u:v=>str(v,o,c), p:(v,s)=>rts(v,o,c,s.slice(0,c    ) )})],
    p: c=>[1,c,o=>({u:v=>pst(v,o,c), p:(v,s)=>tsp(v,o,c,s.slice(0,c - 1) )})]
})
const errbuf = new RangeError("Structure larger than remaining buffer")
const errval = new RangeError("Not enough values for structure")
function struct(format) {
    let fns = [], size = 0, m = rechk.exec(format)
    if (!m) { throw new RangeError("Invalid format string") }
    const t = lut('<' === m[1]), lu = (n, c) => t[c](n ? parseInt(n, 10) : 1)
    while ((m = refmt.exec(format))) { ((r, s, f) => {
        for (let i = 0; i < r; ++i, size += s) { if (f) {fns.push(f(size))} }
    })(...lu(...m.slice(1)))}
    const unpack_from = (arrb, offs) => {
        if (arrb.byteLength < (offs|0) + size) { throw errbuf }
        let v = new DataView(arrb, offs|0)
        return fns.map(f => f.u(v))
    }
    const pack_into = (arrb, offs, ...values) => {
        if (values.length < fns.length) { throw errval }
        if (arrb.byteLength < offs + size) { throw errbuf }
        const v = new DataView(arrb, offs)
        new Uint8Array(arrb, offs, size).fill(0)
        fns.forEach((f, i) => f.p(v, values[i]))
    }
    const pack = (...values) => {
        let b = new ArrayBuffer(size)
        pack_into(b, 0, ...values)
        return b
    }
    const unpack = arrb => unpack_from(arrb, 0)
    function* iter_unpack(arrb) { 
        for (let offs = 0; offs + size <= arrb.byteLength; offs += size) {
            yield unpack_from(arrb, offs);
        }
    }
    return Object.freeze({
        unpack, pack, unpack_from, pack_into, iter_unpack, format, size})
}
//end struct library

/********************************
* GENERATED FILE DO NOT EDIT
********************************/

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

const nodes = {
    web: 0,
    plant: 1,
}
const fields = {
    SSID: 0,
    password: 1,
    plant_id: 2,
    lower_limit: 3,
    upper_limit: 4,
    is_connected: 5,
    water_level: 6,
    humidity: 7,
}
const messages = {
    wifi_config: 0,
    configure_plant: 1,
    get_water_level: 2,
    water_level: 3,
    get_plant_info: 4,
    plant_info: 5,
}
const categories = {
    none: 0,
}
class wifi_config_from_web_to_plant {
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
        struct("<64s").pack_into(buf, index, this._SSID)
        index += 64
        struct("<64s").pack_into(buf, index, this._password)
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
        let index = 0
        this._SSID = struct("<64s").unpack_from(buf, index)[0]
        index += 64
        this._password = struct("<64s").unpack_from(buf, index)[0]
        index += 64
        return
    }
}
class configure_plant_from_web_to_plant {
    constructor() {
        this._sender = nodes.web
        this._receiver = nodes.plant
        this._message = messages.configure_plant
        this._category = categories.none
        this._id = 1
        this._size = 10
        this._bit_field = 0
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
    set_is_connected(value) {
        this._bit_field =  value * (this._bit_field | (1 << 0)) + (!value) * (this._bit_field & ~(1 << 0))
    }
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
        let buf = new ArrayBuffer(10)
        let index = 0
        struct("<B").pack_into(buf, index, this._bit_field)
        index += 1
        struct("<B").pack_into(buf, index, this._plant_id)
        index += 1
        struct("<f").pack_into(buf, index, this._lower_limit)
        index += 4
        struct("<f").pack_into(buf, index, this._upper_limit)
        index += 4
        return buf
    }
    get_is_connected() {
        return this._bit_field & (1 << 0)
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
        data.push({field: fields.is_connected, value: this.get_is_connected()})
        data.push({field: fields.plant_id, value: this.get_plant_id()})
        data.push({field: fields.lower_limit, value: this.get_lower_limit()})
        data.push({field: fields.upper_limit, value: this.get_upper_limit()})
        return data
    }
    parse_buf(buf) {
        let index = 0
        this._bit_field = struct("<B").unpack_from(buf, index)[0]
        index += 1
        this._plant_id = struct("<B").unpack_from(buf, index)[0]
        index += 1
        this._lower_limit = struct("<f").unpack_from(buf, index)[0]
        index += 4
        this._upper_limit = struct("<f").unpack_from(buf, index)[0]
        index += 4
        return
    }
}
class get_water_level_from_web_to_plant {
    constructor() {
        this._sender = nodes.web
        this._receiver = nodes.plant
        this._message = messages.get_water_level
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
        let index = 0
        return
    }
}
class water_level_from_plant_to_web {
    constructor() {
        this._sender = nodes.plant
        this._receiver = nodes.web
        this._message = messages.water_level
        this._category = categories.none
        this._id = 3
        this._size = 4
        this._water_level = 0
    }
    get_sender() { return this._sender }
    get_receiver() { return this._receiver }
    get_message() { return this._message }
    get_id() { return this._id }
    get_size() { return this._size }
    get_category() { return this._category }
    set_water_level(value) {
        this._water_level = value
    }
    build_buf() {
        let buf = new ArrayBuffer(4)
        let index = 0
        struct("<f").pack_into(buf, index, this._water_level)
        index += 4
        return buf
    }
    get_water_level() {
        return this._water_level
    }
    get_all_data() {
        data = []
        data.push({field: fields.water_level, value: this.get_water_level()})
        return data
    }
    parse_buf(buf) {
        let index = 0
        this._water_level = struct("<f").unpack_from(buf, index)[0]
        index += 4
        return
    }
}
class get_plant_info_from_web_to_plant {
    constructor() {
        this._sender = nodes.web
        this._receiver = nodes.plant
        this._message = messages.get_plant_info
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
        struct("<B").pack_into(buf, index, this._plant_id)
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
        let index = 0
        this._plant_id = struct("<B").unpack_from(buf, index)[0]
        index += 1
        return
    }
}
class plant_info_from_plant_to_web {
    constructor() {
        this._sender = nodes.plant
        this._receiver = nodes.web
        this._message = messages.plant_info
        this._category = categories.none
        this._id = 5
        this._size = 14
        this._bit_field = 0
        this._plant_id = 0
        this._lower_limit = 0
        this._upper_limit = 0
        this._humidity = 0
    }
    get_sender() { return this._sender }
    get_receiver() { return this._receiver }
    get_message() { return this._message }
    get_id() { return this._id }
    get_size() { return this._size }
    get_category() { return this._category }
    set_is_connected(value) {
        this._bit_field =  value * (this._bit_field | (1 << 0)) + (!value) * (this._bit_field & ~(1 << 0))
    }
    set_plant_id(value) {
        this._plant_id = value
    }
    set_lower_limit(value) {
        this._lower_limit = value
    }
    set_upper_limit(value) {
        this._upper_limit = value
    }
    set_humidity(value) {
        this._humidity = value
    }
    build_buf() {
        let buf = new ArrayBuffer(14)
        let index = 0
        struct("<B").pack_into(buf, index, this._bit_field)
        index += 1
        struct("<B").pack_into(buf, index, this._plant_id)
        index += 1
        struct("<f").pack_into(buf, index, this._lower_limit)
        index += 4
        struct("<f").pack_into(buf, index, this._upper_limit)
        index += 4
        struct("<f").pack_into(buf, index, this._humidity)
        index += 4
        return buf
    }
    get_is_connected() {
        return this._bit_field & (1 << 0)
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
    get_humidity() {
        return this._humidity
    }
    get_all_data() {
        data = []
        data.push({field: fields.is_connected, value: this.get_is_connected()})
        data.push({field: fields.plant_id, value: this.get_plant_id()})
        data.push({field: fields.lower_limit, value: this.get_lower_limit()})
        data.push({field: fields.upper_limit, value: this.get_upper_limit()})
        data.push({field: fields.humidity, value: this.get_humidity()})
        return data
    }
    parse_buf(buf) {
        let index = 0
        this._bit_field = struct("<B").unpack_from(buf, index)[0]
        index += 1
        this._plant_id = struct("<B").unpack_from(buf, index)[0]
        index += 1
        this._lower_limit = struct("<f").unpack_from(buf, index)[0]
        index += 4
        this._upper_limit = struct("<f").unpack_from(buf, index)[0]
        index += 4
        this._humidity = struct("<f").unpack_from(buf, index)[0]
        index += 4
        return
    }
}
function id_to_message_class(id) {
    if (id == 0) {
        receiver = wifi_config_from_web_to_plant()
        return receiver
    }
    if (id == 1) {
        receiver = configure_plant_from_web_to_plant()
        return receiver
    }
    if (id == 2) {
        receiver = get_water_level_from_web_to_plant()
        return receiver
    }
    if (id == 3) {
        receiver = water_level_from_plant_to_web()
        return receiver
    }
    if (id == 4) {
        receiver = get_plant_info_from_web_to_plant()
        return receiver
    }
    if (id == 5) {
        receiver = plant_info_from_plant_to_web()
        return receiver
    }
}
