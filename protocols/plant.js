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
    sender: "web",
    receiver: "plant",
    fields: {
        SSID: s.fixedString(64),
        password: s.fixedString(64),
    }
})

s.addMsg({
    name: "configure_plant",
    sender: "web",
    receiver: "plant",
    fields: {
        plant_id: s.uint(1),
        lower_limit: s.double(),
        upper_limit: s.double()
    }
})

s.addMsg({
    name: "get_water_level",
    sender: "web",
    receiver: "plant",
})

s.addMsg({
    name: "water_level",
    sender: "plant",
    receiver: "web",
    fields: {
        water_level: s.float()
    }
})

s.addMsg({
    name: "get_plant_info",
    sender: "web",
    receiver: "plant",
    fields: {
        plant_id: s.uint(1)
    }
})

s.addMsg({
    name: "plant_info",
    sender: "plant",
    receiver: "web",
    bitField: [
        "is_connected"
    ],
    fields: {
        plant_id: s.uint(1),
        lower_limit: s.float(),
        upper_limit: s.float(),
        humidity: s.float()
    }
})

s.createJson(output);