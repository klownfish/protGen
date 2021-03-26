################################
#GENERATED FILE DO NOT EDIT
################################

from enum import Enum
import struct

def scaledFloat_to_uint(value, scale):
    return value * scale

def uint_to_scaledFloat(value, scale):
    return value / scale

def packedFloat_to_uint(value, min, max, size):
    max_value = (1 << size * 8) - 1
    difference = max - min
    return (value - min) / difference * max_value

def uint_to_packedFloat(value, min, max, size):
    max_value = (1 << size * 8) - 1
    difference = max - min
    return difference * value / max_value

class units(Enum):
    ground_station = 0
    flight_controller_tc = 1
    flight_controller = 2
    ground_station_tc = 3
    ground_station_tm = 4
class datatypes(Enum):
    time_sync = 0
    set_power_mode = 1
    set_radio_equipment = 2
    set_parachute_output = 3
    set_data_logging = 4
    dump_flash_chip = 5
    handshake = 6
    return_time_sync = 7
    return_power_mode = 8
    return_radio_equipment = 9
    return_parachute_output = 10
    onboard_battery_voltage = 11
    gnss_data = 12
    flight_controller_status = 13
    return_data_logging = 14
    return_dump_flash = 15
    return_handshake = 16
    ms_since_boot = 17
class time_sync_from_ground_station_to_flight_controller_tc:
    def __init__(self):
        self.system_time = 0
        return
    def set_system_time(self, value):
        self.system_time = value
    def get_buf(self):
        buf = b""
        buf += struct.pack("<L", self.system_time)
        return buf
class set_power_mode_from_ground_station_to_flight_controller_tc:
    def __init__(self):
        return
    def get_buf(self):
        buf = b""
        return buf
class set_radio_equipment_from_ground_station_to_flight_controller_tc:
    def __init__(self):
        self.bit_field = 0
        return
    def set_is_fpv_en(self, value):
        self.bit_field =  value * (self.bit_field | 1 << 0) + (not value) * (self.bit_field & ~(1 << 0))
    def set_is_tm_en(self, value):
        self.bit_field =  value * (self.bit_field | 1 << 1) + (not value) * (self.bit_field & ~(1 << 1))
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self.bit_field)
        return buf
class set_parachute_output_from_ground_station_to_flight_controller_tc:
    def __init__(self):
        self.bit_field = 0
        return
    def set_is_parachute_armed(self, value):
        self.bit_field =  value * (self.bit_field | 1 << 0) + (not value) * (self.bit_field & ~(1 << 0))
    def set_is_parachute1_en(self, value):
        self.bit_field =  value * (self.bit_field | 1 << 1) + (not value) * (self.bit_field & ~(1 << 1))
    def set_is_parachute2_en(self, value):
        self.bit_field =  value * (self.bit_field | 1 << 2) + (not value) * (self.bit_field & ~(1 << 2))
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self.bit_field)
        return buf
class set_data_logging_from_ground_station_to_flight_controller_tc:
    def __init__(self):
        self.bit_field = 0
        return
    def set_is_logging_en(self, value):
        self.bit_field =  value * (self.bit_field | 1 << 0) + (not value) * (self.bit_field & ~(1 << 0))
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self.bit_field)
        return buf
class dump_flash_chip_from_ground_station_to_flight_controller_tc:
    def __init__(self):
        self.bit_field = 0
        return
    def set_dump_sd(self, value):
        self.bit_field =  value * (self.bit_field | 1 << 0) + (not value) * (self.bit_field & ~(1 << 0))
    def set_dump_usb(self, value):
        self.bit_field =  value * (self.bit_field | 1 << 1) + (not value) * (self.bit_field & ~(1 << 1))
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self.bit_field)
        return buf
class handshake_from_ground_station_to_flight_controller_tc:
    def __init__(self):
        return
    def get_buf(self):
        buf = b""
        return buf
class return_time_sync_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        return
    def get_buf(self):
        buf = b""
        return buf
class return_power_mode_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        return
    def get_buf(self):
        buf = b""
        return buf
class return_radio_equipment_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self.bit_field = 0
        return
    def set_is_fpv_en(self, value):
        self.bit_field =  value * (self.bit_field | 1 << 0) + (not value) * (self.bit_field & ~(1 << 0))
    def set_is_tm_en(self, value):
        self.bit_field =  value * (self.bit_field | 1 << 1) + (not value) * (self.bit_field & ~(1 << 1))
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self.bit_field)
        return buf
class return_parachute_output_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self.bit_field = 0
        return
    def set_is_parachute_armed(self, value):
        self.bit_field =  value * (self.bit_field | 1 << 0) + (not value) * (self.bit_field & ~(1 << 0))
    def set_is_parachute1_en(self, value):
        self.bit_field =  value * (self.bit_field | 1 << 1) + (not value) * (self.bit_field & ~(1 << 1))
    def set_is_parachute2_en(self, value):
        self.bit_field =  value * (self.bit_field | 1 << 2) + (not value) * (self.bit_field & ~(1 << 2))
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self.bit_field)
        return buf
class onboard_battery_voltage_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self.battery_1 = 0
        self.battery_2 = 0
        return
    def set_battery_1(self, value):
        self.battery_1 = scaledFloat_to_uint(value, 100)
    def set_battery_2(self, value):
        self.battery_2 = scaledFloat_to_uint(value, 100)
    def get_buf(self):
        buf = b""
        buf += struct.pack("<H", self.battery_1)
        buf += struct.pack("<H", self.battery_2)
        return buf
class gnss_data_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self.gnss_time = 0
        self.latitude = 0
        self.longitude = 0
        self.h_dop = 0
        self.n_satellites = 0
        return
    def set_gnss_time(self, value):
        self.gnss_time = value
    def set_latitude(self, value):
        self.latitude = value
    def set_longitude(self, value):
        self.longitude = value
    def set_h_dop(self, value):
        self.h_dop = scaledFloat_to_uint(value, 100)
    def set_n_satellites(self, value):
        self.n_satellites = value
    def get_buf(self):
        buf = b""
        buf += struct.pack("<L", self.gnss_time)
        buf += struct.pack("<l", self.latitude)
        buf += struct.pack("<l", self.longitude)
        buf += struct.pack("<H", self.h_dop)
        buf += struct.pack("<B", self.n_satellites)
        return buf
class flight_controller_status_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self.HW_state = 0
        self.SW_state = 0
        self.mission_state = 0
        return
    def set_HW_state(self, value):
        self.HW_state = value
    def set_SW_state(self, value):
        self.SW_state = value
    def set_mission_state(self, value):
        self.mission_state = value
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self.HW_state)
        buf += struct.pack("<B", self.SW_state)
        buf += struct.pack("<B", self.mission_state)
        return buf
class return_data_logging_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self.bit_field = 0
        return
    def set_is_logging_en(self, value):
        self.bit_field =  value * (self.bit_field | 1 << 0) + (not value) * (self.bit_field & ~(1 << 0))
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self.bit_field)
        return buf
class return_dump_flash_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        self.bit_field = 0
        return
    def set_dump_sd(self, value):
        self.bit_field =  value * (self.bit_field | 1 << 0) + (not value) * (self.bit_field & ~(1 << 0))
    def set_dump_usb(self, value):
        self.bit_field =  value * (self.bit_field | 1 << 1) + (not value) * (self.bit_field & ~(1 << 1))
    def get_buf(self):
        buf = b""
        buf += struct.pack("<B", self.bit_field)
        return buf
class return_handshake_from_flight_controller_to_ground_station_tc:
    def __init__(self):
        return
    def get_buf(self):
        buf = b""
        return buf
class ms_since_boot_from_flight_controller_to_ground_station_tm:
    def __init__(self):
        self.ms_since_boot = 0
        return
    def set_ms_since_boot(self, value):
        self.ms_since_boot = value
    def get_buf(self):
        buf = b""
        buf += struct.pack("<L", self.ms_since_boot)
        return buf
class time_sync:
    def __init__(self):
        self.length = 4
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 4
        self.system_time = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_system_time(self):
        return self.system_time
    def get_all_data(self):
        data = []
        data.append(("system_time", self.get_system_time()))
        return data
    def parse_buf(self, buf):
        index = 0
        struct.unpack_from("<L", buf, index)
        index += 4
        return
class set_power_mode:
    def __init__(self):
        self.length = 0
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class set_radio_equipment:
    def __init__(self):
        self.length = 1
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 1
        self.bit_field = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_is_fpv_en(self):
        return self.bit_field & (1 << 0)
    def get_is_tm_en(self):
        return self.bit_field & (1 << 1)
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        self.bit_field = struct.unpack_from("<B", buf, index)
        index += 1
        return
class set_parachute_output:
    def __init__(self):
        self.length = 1
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 1
        self.bit_field = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_is_parachute_armed(self):
        return self.bit_field & (1 << 0)
    def get_is_parachute1_en(self):
        return self.bit_field & (1 << 1)
    def get_is_parachute2_en(self):
        return self.bit_field & (1 << 2)
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        self.bit_field = struct.unpack_from("<B", buf, index)
        index += 1
        return
class set_data_logging:
    def __init__(self):
        self.length = 1
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 1
        self.bit_field = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_is_logging_en(self):
        return self.bit_field & (1 << 0)
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        self.bit_field = struct.unpack_from("<B", buf, index)
        index += 1
        return
class dump_flash_chip:
    def __init__(self):
        self.length = 1
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 1
        self.bit_field = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_dump_sd(self):
        return self.bit_field & (1 << 0)
    def get_dump_usb(self):
        return self.bit_field & (1 << 1)
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        self.bit_field = struct.unpack_from("<B", buf, index)
        index += 1
        return
class handshake:
    def __init__(self):
        self.length = 0
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class return_time_sync:
    def __init__(self):
        self.length = 0
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class return_power_mode:
    def __init__(self):
        self.length = 0
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class return_radio_equipment:
    def __init__(self):
        self.length = 1
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 1
        self.bit_field = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_is_fpv_en(self):
        return self.bit_field & (1 << 0)
    def get_is_tm_en(self):
        return self.bit_field & (1 << 1)
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        self.bit_field = struct.unpack_from("<B", buf, index)
        index += 1
        return
class return_parachute_output:
    def __init__(self):
        self.length = 1
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 1
        self.bit_field = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_is_parachute_armed(self):
        return self.bit_field & (1 << 0)
    def get_is_parachute1_en(self):
        return self.bit_field & (1 << 1)
    def get_is_parachute2_en(self):
        return self.bit_field & (1 << 2)
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        self.bit_field = struct.unpack_from("<B", buf, index)
        index += 1
        return
class onboard_battery_voltage:
    def __init__(self):
        self.length = 4
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 4
        self.battery_1 = 0
        self.battery_2 = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_battery_1(self):
        return uint_to_scaledFloat(self.battery_1, 100)
    def get_battery_2(self):
        return uint_to_scaledFloat(self.battery_2, 100)
    def get_all_data(self):
        data = []
        data.append(("battery_1", self.get_battery_1()))
        data.append(("battery_2", self.get_battery_2()))
        return data
    def parse_buf(self, buf):
        index = 0
        struct.unpack_from("<H", buf, index)
        index += 2
        struct.unpack_from("<H", buf, index)
        index += 2
        return
class gnss_data:
    def __init__(self):
        self.length = 15
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 15
        self.gnss_time = 0
        self.latitude = 0
        self.longitude = 0
        self.h_dop = 0
        self.n_satellites = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_gnss_time(self):
        return self.gnss_time
    def get_latitude(self):
        return self.latitude
    def get_longitude(self):
        return self.longitude
    def get_h_dop(self):
        return uint_to_scaledFloat(self.h_dop, 100)
    def get_n_satellites(self):
        return self.n_satellites
    def get_all_data(self):
        data = []
        data.append(("gnss_time", self.get_gnss_time()))
        data.append(("latitude", self.get_latitude()))
        data.append(("longitude", self.get_longitude()))
        data.append(("h_dop", self.get_h_dop()))
        data.append(("n_satellites", self.get_n_satellites()))
        return data
    def parse_buf(self, buf):
        index = 0
        struct.unpack_from("<L", buf, index)
        index += 4
        struct.unpack_from("<l", buf, index)
        index += 4
        struct.unpack_from("<l", buf, index)
        index += 4
        struct.unpack_from("<H", buf, index)
        index += 2
        struct.unpack_from("<B", buf, index)
        index += 1
        return
class flight_controller_status:
    def __init__(self):
        self.length = 3
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 3
        self.HW_state = 0
        self.SW_state = 0
        self.mission_state = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_HW_state(self):
        return self.HW_state
    def get_SW_state(self):
        return self.SW_state
    def get_mission_state(self):
        return self.mission_state
    def get_all_data(self):
        data = []
        data.append(("HW_state", self.get_HW_state()))
        data.append(("SW_state", self.get_SW_state()))
        data.append(("mission_state", self.get_mission_state()))
        return data
    def parse_buf(self, buf):
        index = 0
        struct.unpack_from("<B", buf, index)
        index += 1
        struct.unpack_from("<B", buf, index)
        index += 1
        struct.unpack_from("<B", buf, index)
        index += 1
        return
class return_data_logging:
    def __init__(self):
        self.length = 1
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 1
        self.bit_field = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_is_logging_en(self):
        return self.bit_field & (1 << 0)
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        self.bit_field = struct.unpack_from("<B", buf, index)
        index += 1
        return
class return_dump_flash:
    def __init__(self):
        self.length = 1
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 1
        self.bit_field = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_dump_sd(self):
        return self.bit_field & (1 << 0)
    def get_dump_usb(self):
        return self.bit_field & (1 << 1)
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        self.bit_field = struct.unpack_from("<B", buf, index)
        index += 1
        return
class return_handshake:
    def __init__(self):
        self.length = 0
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class ms_since_boot:
    def __init__(self):
        self.length = 4
        self.source = 0
        self.target = 0
        self.datatype = 0
        self.id = 0
        self.size = 4
        self.ms_since_boot = 0
    def set_source(self, value):
        self.source = value
    def set_target(self, value):
        self.target = value
    def set_datatype(self, value):
        self.datatype = value
    def set_id(self, value):
        self.id = value
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_datatype(self):
        return self.datatype
    def get_size(self):
        return self.size
    def get_id(self):
        return self.id
    def get_ms_since_boot(self):
        return self.ms_since_boot
    def get_all_data(self):
        data = []
        data.append(("ms_since_boot", self.get_ms_since_boot()))
        return data
    def parse_buf(self, buf):
        index = 0
        struct.unpack_from("<L", buf, index)
        index += 4
        return
def id_to_receiver(id):
    if id == 16:
        receiver = time_sync()
        receiver.set_id(16)
        receiver.set_target(units.flight_controller_tc)
        receiver.set_source(units.ground_station)
        receiver.set_datatype(datatypes.time_sync)
        return receiver
    if id == 17:
        receiver = set_power_mode()
        receiver.set_id(17)
        receiver.set_target(units.flight_controller_tc)
        receiver.set_source(units.ground_station)
        receiver.set_datatype(datatypes.set_power_mode)
        return receiver
    if id == 18:
        receiver = set_radio_equipment()
        receiver.set_id(18)
        receiver.set_target(units.flight_controller_tc)
        receiver.set_source(units.ground_station)
        receiver.set_datatype(datatypes.set_radio_equipment)
        return receiver
    if id == 19:
        receiver = set_parachute_output()
        receiver.set_id(19)
        receiver.set_target(units.flight_controller_tc)
        receiver.set_source(units.ground_station)
        receiver.set_datatype(datatypes.set_parachute_output)
        return receiver
    if id == 20:
        receiver = set_data_logging()
        receiver.set_id(20)
        receiver.set_target(units.flight_controller_tc)
        receiver.set_source(units.ground_station)
        receiver.set_datatype(datatypes.set_data_logging)
        return receiver
    if id == 21:
        receiver = dump_flash_chip()
        receiver.set_id(21)
        receiver.set_target(units.flight_controller_tc)
        receiver.set_source(units.ground_station)
        receiver.set_datatype(datatypes.dump_flash_chip)
        return receiver
    if id == 22:
        receiver = handshake()
        receiver.set_id(22)
        receiver.set_target(units.flight_controller_tc)
        receiver.set_source(units.ground_station)
        receiver.set_datatype(datatypes.handshake)
        return receiver
    if id == 32:
        receiver = return_time_sync()
        receiver.set_id(32)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.return_time_sync)
        return receiver
    if id == 33:
        receiver = return_power_mode()
        receiver.set_id(33)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.return_power_mode)
        return receiver
    if id == 34:
        receiver = return_radio_equipment()
        receiver.set_id(34)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.return_radio_equipment)
        return receiver
    if id == 35:
        receiver = return_parachute_output()
        receiver.set_id(35)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.return_parachute_output)
        return receiver
    if id == 36:
        receiver = onboard_battery_voltage()
        receiver.set_id(36)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.onboard_battery_voltage)
        return receiver
    if id == 37:
        receiver = gnss_data()
        receiver.set_id(37)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.gnss_data)
        return receiver
    if id == 38:
        receiver = flight_controller_status()
        receiver.set_id(38)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.flight_controller_status)
        return receiver
    if id == 39:
        receiver = return_data_logging()
        receiver.set_id(39)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.return_data_logging)
        return receiver
    if id == 40:
        receiver = return_dump_flash()
        receiver.set_id(40)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.return_dump_flash)
        return receiver
    if id == 41:
        receiver = return_handshake()
        receiver.set_id(41)
        receiver.set_target(units.ground_station_tc)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.return_handshake)
        return receiver
    if id == 80:
        receiver = ms_since_boot()
        receiver.set_id(80)
        receiver.set_target(units.ground_station_tm)
        receiver.set_source(units.flight_controller)
        receiver.set_datatype(datatypes.ms_since_boot)
        return receiver
