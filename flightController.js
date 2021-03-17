"use strict";

let protGen = require("./protGen.js")

if (process.argv.length < 3) {
    console.log(`usage: node OUTPUT_FILE `)
    return -1
}

let output = process.argv[2]

let s = new protGen.Schema()

let gs_to_fc = 0x10
let fc_to_gs = 0x20

let fc = "flight_controller"
let gs = "ground_station"
let ec = "edda_controller"

let gs_tc = "ground_station_tc"
let gs_tm = "ground_station_tm"
let fc_tc = "flight_controller_tc"
let fc_can = "flight_controller_can"
let ec_tc = "edda_controller_tc"
let ec_can = "edda_controller_can"

s.setIdType("uint8_t")
s.setName("fc")

s.addMsg({
    id: gs_to_fc++,
    source: gs,
    target: fc_tc,
    datatype: "time_sync",
    fields: {
        system_time: s.uint(4),
    }
});

s.addMsg({
    id: gs_to_fc++,
    source: gs,
    target: fc_tc,
    datatype: "set_power_mode",
})

s.addMsg({
    id: gs_to_fc++,
    source: gs,
    target: fc_tc,
    datatype: "set_radio_equipment",
    bitField: [
        "is_fpv_en",
        "is_tm_en",
    ]   
})

s.addMsg({
    id: gs_to_fc++,
    source: gs,
    target: fc_tc,
    datatype: "set_parachute_output",
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
    datatype: "set_data_logging",
    bitField: [
        "is_logging_en",
    ]
})


s.addMsg({
    id: gs_to_fc++,
    source: gs,
    target: fc_tc,
    datatype: "dump_flash_chip",
    bitField: [
        "dump_sd",
        "dump_usb"
    ]
})

s.addMsg({
    id: gs_to_fc++,
    source: gs,
    target: fc_tc,
    datatype: "handshake"
})



////////////////////responses
s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    datatype: "return_time_sync",
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    datatype: "return_power_mode",
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    datatype: "return_radio_equipment",
    bitField: [
        'is_fpv_en',
        "is_tm_en"
    ]
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    datatype: "return_parachute_output",
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
    datatype: "onboard_battery_voltage",
    fields: {
        battery_1: s.uint(2),
        battery_2: s.uint(2)
    }
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    datatype: "gnss_data",
    fields: {
        gnss_time: s.uint(4),
        latitude: s.int(4),
        longitude: s.int(4),
        h_dop: s.scaledFloat(2, 100),
        n_satellites: s.uint(1)
    }
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    datatype: "flight_controller_status",
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
    datatype: "return_data_logging",
    bitField: [
        "is_logging_en"
    ]
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    datatype: "return_dump_flash",
    bitField: [
        "dump_sd",
        "dump_usb"
    ]
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    target: gs_tc,
    datatype: "return_handshake",
})

s.createJson(output);