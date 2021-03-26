# protGen - binary protocol generator
Automatically generates a dataprotocol from a schematic

## features
ProtGen takes a schematic for a protocol and generates a JSON description of it. The JSON file can then be parsed to generate encoders, decoders and everything needed to support them. Currently only an exporter for C++ exists (and json).

#### supported datatypes
* integers
* float
* packedFloat (uint scaled between two numbers)
* scaledFloat (uint/int scaled by a factor)
* bool (represented by a single bit)
* enums

## usage
### messages
The dataprotocol is defined by specifying messages. Messages are recognized by a numeric ID and every message contains the source, the target, the datatype and the fields of itself. Messages can have a bit field for booleans and byte fields for other datatypes. Multiple messages can have the same datatype but then all the fields have to be left empty as to not overwrite it.

#### example message
```
{
    id: 5,
    source: "flight_controller",
    target: "ground_station",
    datatype: "gnss_data",
    fields: {
        gnss_time: schema.uint(4),
        latitude: schema.int(4),
        longitude: schema.int(4),
        h_dop: schema.scaledFloat(2, 100, false),
        n_satellites: schema.uint(1)
    }
}
```

### enums
Enums are created with a name and an array with strings
```
schema.addEnum("power_state", [
    "idle",
    "armed",
    "powered"
])
```

### the schema class
The schema class generates and contains all functions required to create the protocol.

* addMsg(msg) 
    * adds a message to the schematic| 
* addEnum(name, entries)
    * adds an enum, see above
* uint(size) 
    * creates an uint, size in bytes
* int(size) 
    * creates an int, size in bytes
* scaledFloat(size, scale, is_signed) 
    * creates a scaled float, scale is what it should be multiplied with (scale > 1 to have decimals)
* packedFloat(size, min, max) 
    * creates packed float, can represent numbers between min and max
* getObject() 
    * returns the schematic object
* createJson(path)
    * outputs the JSON schematic

## usage
```
let protGen = require("./protGen.js")
let s = new protGen.Schema()
```
## requirements
* NodeJS

## example
Imagine a data protocol with two units, a base station("base") and two temperature sensors("temp_sensor1", "temp_sensor1"). The base station can send an enable/disable command and the sensors send the current time and a measurement.

the code for that would look like this
```
let protGen = require("./protGen.js")
let s = new protGen.Schema()
s.setName("temperature_sensor_prot")
s.addMsg({
    id: 0,
    source: "base",
    target: "temp_sensor1",
    datatype: "set_state",
    bitFields: [
        "enabled"
    ]
})
s.addMsg({
    id: 1,
    source: "base",
    target: "temp_sensor2"
    datatype: "set_state
})
s.addMsg({
    id: 2,
    source: "temp_sensor1"
    datatye: "measurement",
    fields: [
        time: s.uint(4), // same size as arduino's millis()
        measurement: s.packedFloat(4, -30, 40) // -30 to 40 should cover all temperatures 
    ]
})
s.addMsg({
    id: 3,
    source: "temp_sensor2"
    datatye: "measurement"
})
```