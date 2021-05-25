"use strict";

let protGen = require("../protGen.js")

if (process.argv.length < 3) {
    console.log(`usage: node OUTPUT_FILE `)
    return -1
}

let output = process.argv[2]

let s = new protGen.Schema()

s.setIdType("uint8")
s.setName("rocket")

s.addMsg({
    name: "local_timestamp",
    sender: "local",
    receiver: "local",
    fields: {
        local_timestamp: s.uint(4)
    }
})

s.addMsg({
    name: "timestamp",
    sender: "rocket",
    receiver: "ground",
    fields: {
        ms_since_boot: s.uint(4)
    }
})

s.addMsg({
    name: "handshake",
    sender: "ground",
    receiver: "rocket",
})

s.addMsg({
    name: "handshake",
    sender: "rocket",
    receiver: "ground",
})

s.addMsg({
    name: "simple_calibration",
    sender: "ground",
    receiver: "rocket",
})

s.addMsg({
    name: "mag_calibration",
    sender: "ground",
    receiver: "rocket",
    fields: {
        declination: s.float()
    }
})

s.addMsg({
    name: "wipe_flash",
    sender: "ground",
    receiver: "rocket",
    fields: {
        this_to_42: s.uint(1)
    }
})

s.addMsg({
    name: "play_music",
    sender: "ground",
    receiver: "rocket"
})

s.addMsg({
    name: "flash_address",
    sender: "rocket",
    receiver: "ground",
    fields: {
        address: s.uint(4)   
    }
})

s.addMsg({
    name: "bmp",
    sender: "rocket",
    receiver: "ground",
    fields: {
        altitude: s.float(),
        temperature: s.float()
    }
})

s.addMsg({
    name: "mpu",
    sender: "rocket",
    receiver: "ground",
    fields: {
        acc_x: s.float(),
        acc_y: s.float(),
        acc_z: s.float(),
        gyro_x: s.float(),
        gyro_y: s.float(),
        gyro_z: s.float(),
        mag_x: s.float(),
        mag_y: s.float(),
        mag_z: s.float(),
    }
})

s.addMsg({
    name: "battery_voltage",
    sender: "rocket",
    receiver: "ground",
    fields: {
        voltage: s.float()
    }
})

s.addEnum("state", [
    "sleeping",
    "awake",
    "ready",
    "ascending",
    "falling",
    "landed"
])

s.addMsg({
    name: "set_state",
    sender: "ground",
    receiver: "rocket",
    fields: {
        state: s.enumerator("state")
    }
})

s.addMsg({
    name: "state",
    sender: "rocket",
    receiver: "ground",
    fields: {
        state: s.enumerator("state")
    }
})

s.addMsg({
    name: "rssi",
    sender: "rocket",
    receiver: "ground",
    fields: {
        rssi: s.scaledFloat(2, 100, true)
    }
})

s.addMsg({
    name: "rssi",
    sender: "relay",
    receiver: "ground",
    fields: {
        rssi: s.scaledFloat(2, 100, true)
    }
})

s.addMsg({
    name: "ms_since_boot",
    sender: "rocket",
    receiver: "ground",
    fields: {
        ms_since_boot: s.uint(4)
    }
})

s.createJson(output)