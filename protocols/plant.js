"use strict";

let protGen = require("../protGen.js")

if (process.argv.length < 3) {
    console.log(`usage: node OUTPUT_FILE `)
    return -1
}

let output = process.argv[2]

let s = new protGen.Schema()

s.setIdType("uint8")
s.setName("prot")

s.addMsg({
    name: "wifi_config",
    source: "web",
    target: "plant",
    fields: {
        SSID: s.fixedString(64),
        password: s.fixedString(64),
    }
})

s.addMsg({
    name: "configure_plant",
    source: "web",
    target: "plant",
    fields: {
        plant_id: s.uint(1),
        lower_limit: s.double(),
        upper_limit: s.double()
    }
})

s.addMsg({
    name: "get_active_plants",
    source: "web",
    target: "plant",
})

s.addMsg({
    name: "get_humidity_measurement",
    source: "web",
    target: "plant",
    field: {
        plant_id: s.uint(1),
    }
})

s.addMsg({
    name: "get_configuration",
    source: "web",
    target: "plant",
    field: {
        plant_id: s.uint(1),
    }
})

s.addMsg({
    name: "active_plants",
    source: "plant",
    target: "web",
    bitField: [
        "plant_0",
        "plant_1",
        "plant_2",
        "plant_3",
        "plant_4",
        "plant_5",
        "plant_6",
        "plant_7",
    ]
})

s.addMsg({
    name: "humidity_measurement",
    source: "plant",
    target: "web",
    fields: {
        plant_id: s.uint(1),
        humidity: s.double(),
    }
})

s.addMsg({
    name: "configuration",
    source: "plant",
    target: "web",
    fields: {

    }
})

s.createJson(output);