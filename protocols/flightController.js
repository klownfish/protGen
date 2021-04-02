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
let ec = "edda_controller"

let gs_tc = "ground_station"
let gs_tm = "ground_station"
let fc_tc = "flight_controller"
let fc_can = "flight_controller"
let ec_tc = "engine_controller"
let ec_can = "engine_controller"

s.setIdType("uint8")
s.setName("fc")

s.addMsg({
    id: 0xFF,
    source: "local",
    target: "local",
    name: "local_timestamp",
    fields: {
        timestamp: s.uint(4)
    }
})
//############# REMOVE THESE
s.addMsg({
    id: 64,
    source: "test",
    target: "test",
    name: "ms_since_boot",
    fields: {
        ms_since_boot: s.uint(4)
    }
})

s.addMsg({
    id: test++,
    source: "test",
    target: "test",
    name: "altitude",
    fields: {
        altitude: s.uint(2),
    }
})

s.addMsg({
    id: test++,
    source: "test",
    target: "test",
    name: "acceleration",
    fields: {
        altitude: s.uint(1),
    }
})

s.addMsg({
    id: test++,
    source: "test",
    target: "test",
    name: "pressure",
    fields: {
        altitude: s.uint(2),
    }
})

s.addMsg({
    id: test++,
    source: "test",
    target: "test",
    name: "catastrophe",
    bitField: [
        "catastrophe"
    ]
})

s.addMsg({
    id: test++,
    source: "test",
    target: "test",
    name: "gyro",
    fields: {
        x: s.uint(1),
        y: s.uint(1),
        z: s.uint(1)
    }
})

//##################################remove these ^^^^

//END TEST

s.addMsg({
    id: gs_to_fc++,
    source: gs,
    target: fc_tc,
    name: "time_sync",
    fields: {
        system_time: s.uint(4),
    }
});

s.addMsg({
    id: gs_to_fc++,
    source: gs,
    target: fc_tc,
    name: "set_power_mode",
})

s.addMsg({
    id: gs_to_fc++,
    source: gs,
    target: fc_tc,
    name: "set_radio_equipment",
    bitField: [
        "is_fpv_en",
        "is_tm_en",
    ]   
})

s.addMsg({
    id: gs_to_fc++,
    source: gs,
    target: fc_tc,
    name: "set_parachute_output",
    bitField: [
        "is_parachute_armed",
        "is_parachute1_en",
        "is_parachute2_en",
    ]
})

s.addMsg({
    id: gs_to_fc++,
    source: gs,
    target: fc_tc,
    name: "set_data_logging",
    bitField: [
        "is_logging_en",
    ]
})


s.addMsg({
    id: gs_to_fc++,
    source: gs,
    target: fc_tc,
    name: "dump_flash",
    bitField: [
        "dump_sd",
        "dump_usb"
    ]
})

s.addMsg({
    id: gs_to_fc++,
    source: gs,
    target: fc_tc,
    name: "handshake"
})



////////////////////responses
s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    name: "return_time_sync",
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    name: "return_power_mode",
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    name: "return_radio_equipment",
    bitField: [
        'is_fpv_en',
        "is_tm_en"
    ]
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    name: "return_parachute_output",
    bitField: [
        "is_parachute_armed",
        "is_parachute1_en",
        "is_parachute2_en"
    ]
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    name: "onboard_battery_voltage",
    fields: {
        battery_1: s.scaledFloat(2, 100, false),
        battery_2: s.scaledFloat(2, 100, false)
    }
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    name: "gnss_data",
    fields: {
        gnss_time: s.uint(4),
        latitude: s.int(4),
        longitude: s.int(4),
        h_dop: s.scaledFloat(2, 100, false),
        n_satellites: s.uint(1)
    }
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    name: "flight_controller_status",
    fields: {
        HW_state: s.uint(1),
        SW_state: s.uint(1),
        mission_state: s.uint(1),
    }
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    name: "return_data_logging",
    bitField: [
        "is_logging_en"
    ]
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    name: "return_dump_flash",
    bitField: [
        "dump_sd",
        "dump_usb"
    ]
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    name: "return_handshake",
})

///////////////////////////////fc telemetry
s.addMsg({
    id: fc_to_gs_tm++,
    source: fc,
    target: gs_tm,
    name: "ms_since_boot",
    fields : {
        ms_since_boot: s.uint(4)
    }
})
s.addMsg({
    id: fc_to_gs_tm++,
    source: fc,
    target: gs_tm,
    name: "us_since_boot",
    fields: {
        us_since_boot: s.uint(8)
    }
})

s.addMsg({
    id: fc_to_gs_tm++,
    source: fc,
    target: gs_tm,
    name: "current_time",
    fields: {
        current_time: s.uint(4)
    }
})
s.addMsg({
    id: fc_to_gs_tm++,
    source: fc,
    target: gs_tm,
    name: "GNSS_data_1",
    fields: {
        gnss_time: s.uint(4),
        latitude: s.int(4),
        longitude: s.int(4),
    }
})
s.addEnum("fix_status", [
    "no_fix",
    "fix_2D",
    "fix_3D"
])
s.addMsg({
    id: fc_to_gs_tm++,
    source: fc,
    target: gs_tm,
    name: "GNSS_data_2",
    fields: {
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
    source: fc,
    target: gs_tm,
    name: "inside_static_temperature",
    fields: {
        temperature_1: s.scaledFloat(4, 100, true),
        temperature_2: s.scaledFloat(4, 100, true)
    }
})

s.addMsg({
    id: fc_to_gs_tm++,
    source: fc,
    target: gs_tm,
    name: "inside_static_pressure",
    fields: {
        pressure_1: s.scaledFloat(4, 100, true),
        pressure_2: s.scaledFloat(4, 100, true)
    }
})

s.addMsg({
    id: fc_to_gs_tm++,
    source: fc,
    target: gs_tm,
    name: "IMU1",
    fields: {
        accel_x: s.uint(2),
        accel_y: s.uint(2),
        accel_z: s.uint(2),
        gyro_x: s.uint(2),
        gyro_y: s.uint(2),
        gyro_z: s.uint(2),
        magnet_x: s.uint(2),
        magnet_y: s.uint(2),
        magnet_z: s.uint(2),
    }
})

s.addMsg({
    id: fc_to_gs_tm++,
    source: fc,
    target: gs_tm,
    name: "IMU2",
    fields: {
        accel_x: s.uint(2),
        accel_y: s.uint(2),
        accel_z: s.uint(2),
        gyro_x: s.uint(2),
        gyro_y: s.uint(2),
        gyro_z: s.uint(2),
        magnet_x: s.uint(2),
        magnet_y: s.uint(2),
        magnet_z: s.uint(2),
    }
})


s.createJson(output);