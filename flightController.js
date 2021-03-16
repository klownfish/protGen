const { group } = require("console");
let protGen = require("./protGen.js")

let s = new protGen.Schema()

let gs_to_fc = 0x10
let fc_to_gs = 0x20
let gs = "ground_station"
let fc = "flight_controller"

s.addMsg({
    id: gs_to_fc++,
    source: gs,
    datatype: "time_sync",
    fields: {
        system_time: s.uint(4),
    }
});

s.addMsg({
    id: gs_to_fc++,
    source: gs,
    datatype: "set_power_mode",
})

s.addMsg({
    id: gs_to_fc++,
    source: gs,
    datatype: "set_radio_equipment",
    bitField: [
        "is_fpv_en",
        "is_tm_en",
    ]   
})

s.addMsg({
    id: gs_to_fc++,
    source: gs,
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
    datatype: "set_data_logging",
    bitField: [
        "is_logging_en",
    ]
})


s.addMsg({
    id: gs_to_fc++,
    source: gs,
    datatype: "dump_flash_chip",
    bitField: [
        "dump_sd",
        "dump_usb"
    ]
})

s.addMsg({
    id: gs_to_fc++,
    source: gs,
    datatype: "handshake"
})

//responses
s.addMsg({
    id: fc_to_gs++,
    source: gs,
    datatype: "return_time_sync",
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    datatype: "return_radio_equipment",
    bitField: [
        'is_fpv_en',
        "is_tm_en"
    ]
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
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
    datatype: "onboard_battery_voltage",
    fields: {
        battery_1: s.uint(2),
        battery_2: s.uint(2)
    }
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
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
    datatype: "return_data_logging",
    bitField: [
        "is_logging_en"
    ]
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    datatype: "return_dump_flash",
    bitField: [
        "dump_sd",
        "dump_usb"
    ]
})

s.addMsg({
    id: fc_to_gs++,
    source: fc,
    datatype: "return_handshake",
})

s.createJson();