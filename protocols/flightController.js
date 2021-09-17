"use strict";

let protGen = require("../protGen.js")

if (process.argv.length < 3) {
    console.log(`usage: node OUTPUT_FILE `)
    return -1
}

let output = process.argv[2]

let s = new protGen.Schema()

let test = 0x00

let gs_to_fc = 0x10
let fc_to_gs = 0x20
let fc_to_gs_tm = 0x50

let fc = "flight_controller"
let gs = "ground_station"

let gs_tc = "ground_station"
let gs_tm = "ground_station"
let fc_tc = "flight_controller"



s.setIdType("uint8")
s.setName("fc")

s.addEnum("flight_state", [
    "sleeping",
    "idle",
    "ready",
    "burning",
    "ascending",
    "descending",
    "drogue",
    "main_chute",
    "landed"
])

s.addEnum("fix_status", [
    "no_fix",
    "fix_2D",
    "fix_3D"
])

s.addMsg({
    id: 0xFF,
    sender: "local",
    receiver: "local",
    name: "local_timestamp",
    fields: {
        timestamp: s.uint(4)
    }
})

s.addMsg({
    id: gs_to_fc++,
    sender: gs,
    receiver: fc_tc,
    name: "time_sync",
    fields: {
        system_time: s.uint(4),
    }
});

s.addMsg({
    id: gs_to_fc++,
    sender: gs,
    receiver: fc_tc,
    name: "set_state",
    fields: {
        state: s.enumerator("flight_state")
    }
})

s.addMsg({
    id: gs_to_fc++,
    sender: gs,
    receiver: fc_tc,
    name: "set_parachute_output",
    bitField: [
        "is_parachute_armed",
        "is_parachute1_en",
        "is_parachute2_en",
    ]
})

s.addMsg({
    id: gs_to_fc++,
    sender: gs,
    receiver: fc_tc,
    name: "set_data_logging",
    bitField: [
        "is_logging_en",
    ]
})


s.addMsg({
    id: gs_to_fc++,
    sender: gs,
    receiver: fc_tc,
    name: "dump_flash",
    bitField: [
        "dump_sd",
        "dump_usb"
    ]
})

s.addMsg({
    id: gs_to_fc++,
    sender: gs,
    receiver: fc_tc,
    name: "handshake"
})



////////////////////responses
s.addMsg({
    id: fc_to_gs++,
    sender: fc,
    receiver: gs_tc,
    name: "return_time_sync",
})

s.addMsg({
    id: fc_to_gs++,
    sender: fc,
    receiver: gs_tc,
    name: "return_power_mode",
})

s.addMsg({
    id: fc_to_gs++,
    sender: fc,
    receiver: gs_tc,
    name: "return_radio_equipment",
    bitField: [
        'is_fpv_en',
        "is_tm_en"
    ]
})

s.addMsg({
    id: fc_to_gs++,
    sender: fc,
    receiver: gs_tc,
    name: "return_parachute_output",
    bitField: [
        "is_parachute_armed",
        "is_parachute1_en",
        "is_parachute2_en"
    ]
})

s.addMsg({
    id: fc_to_gs++,
    sender: fc,
    receiver: gs_tc,
    name: "onboard_battery_voltage",
    fields: {
        battery_1: s.scaledFloat(2, 100, false),
        battery_2: s.scaledFloat(2, 100, false)
    }
})

s.addMsg({
    id: fc_to_gs++,
    sender: fc,
    receiver: gs_tc,
    name: "return_data_logging",
    bitField: [
        "is_logging_en"
    ]
})

s.addMsg({
    id: fc_to_gs++,
    sender: fc,
    receiver: gs_tc,
    name: "return_dump_flash",
    bitField: [
        "dump_sd",
        "dump_usb"
    ]
})

s.addMsg({
    id: fc_to_gs++,
    sender: fc,
    receiver: gs_tc,
    name: "return_handshake",
})



///////////////////////////////fc telemetry
s.addMsg({
    id: fc_to_gs_tm++,
    sender: fc,
    receiver: gs_tm,
    name: "ms_since_boot",
    fields : {
        ms_since_boot: s.uint(4)
    }
})

s.addMsg({
    id: fc_to_gs_tm++,
    sender: fc,
    receiver: gs_tm,
    name: "GNSS_data",
    fields: {
        gnss_time: s.float(),
        altitude: s.scaledFloat(4, 10, true),
        heading: s.int(2),
        horiz_speed: s.scaledFloat(2, 10, true),
        fix_status: s.enumerator("fix_status"),
        n_satellites: s.uint(1),
        h_dop: s.scaledFloat(2, 10, false)
    }
})

s.addMsg({
    id: fc_to_gs_tm++,
    sender: fc,
    receiver: gs_tm,
    name: "ms_raw",
    fields: {
        pressure: s.float(),
        temperature: s.float()
    }
})

s.addMsg({
    id: fc_to_gs_tm++,
    sender: fc,
    receiver: gs_tm,
    name: "bmp_raw",
    fields: {
        pressure: s.float(),
        temperature: s.float()
    }
})

s.addMsg({
    id: fc_to_gs_tm++,
    sender: fc,
    receiver: gs_tm,
    name: "imu_raw",
    fields: {
        imu_id: s.uint(1),
        accel_x: s.float(),
        accel_y: s.float(),
        accel_z: s.float(),
        gyro_x: s.float(),
        gyro_y: s.float(),
        gyro_z: s.float(),
        magnet_x: s.float(),
        magnet_y: s.float(),
        magnet_z: s.float()
    }
})

s.addMsg({
    id: fc_to_gs_tm++,
    sender: fc,
    receiver: gs_tm,
    name: "position",
    fields: {
        altitude: s.float(),
        longitude: s.float(),
        latitude: s.float()
    }
})

s.addMsg({
    id: fc_to_gs_tm++,
    sender: fc,
    receiver: gs_tm,
    name: "differential_pressure",
    fields: {
        differential_pressure: s.float()
    }
})

s.createJson(output);