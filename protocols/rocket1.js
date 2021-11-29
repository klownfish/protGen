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
    sender: "everyone",
    receiver: "everyone",
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
    name: "set_logging",
    sender: "ground",
    receiver: "rocket",
    bitField: [
        "is_enabled"
    ]
})

s.addMsg({
    name: "dump_flash",
    sender: "ground",
    receiver: "rocket",
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
        pressure: s.float(),
        temperature: s.float()
    }
})

s.addMsg({
    name: "mpu",
    sender: "rocket",
    receiver: "ground",
    fields: {
        ax: s.float(),
        ay: s.float(),
        az: s.float(),
        gx: s.float(),
        gy: s.float(),
        gz: s.float(),
        mx: s.float(),
        my: s.float(),
        mz: s.float(),
    }
})

s.addMsg({
    name: "bmi",
    sender: "rocket",
    receiver: "ground",
    fields: {
        ax: s.float(),
        ay: s.float(),
        az: s.float(),
        gx: s.float(),
        gy: s.float(),
        gz: s.float(),
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
    "debug",
    "sleeping",
    "awake",
    "ready",
    "powered_flight",
    "passive_flight",
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

s.addEnum("fix_type", [
    "none",
    "fix2D",
    "fix3D"
])

s.addMsg({
    name: "gps_state",
    sender: "rocket",
    receiver: "ground",
    fields: {
        pdop: s.scaledFloat(2, 100, false),
        n_satellites: s.uint(1),
        fix_type: s.enumerator("fix_type")
    }
})

s.addMsg({
    name: "gps_pos",
    sender: "rocket",
    receiver: "ground",
    fields: {
        altitude: s.float(),
        latitude: s.float(),
        longitude: s.float(),
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

s.addMsg({
    name: "arm_pyro",
    sender: "ground",
    receiver: "launchpad",
    bitField: [
        "armed"
    ]
})

s.addMsg({
    name: "enable_pyro",
    sender: "ground",
    receiver: "launchpad",
    fields: {
        channel: s.uint(1)
    }
})

s.addMsg({
    name: "estimate",
    sender: "rocket",
    receiver: "ground",
    fields: {
        ax: s.float(),
        ay: s.float(),
        az: s.float(),
        gx: s.float(),
        gy: s.float(),
        gz: s.float(),
        hx: s.float(),
        hy: s.float(),
        hz: s.float(),
        vx: s.float(),
        vy: s.float(),
        vz: s.float(),
        px: s.float(),
        py: s.float(),
        pz: s.float()
    }
})

s.createJson(output)