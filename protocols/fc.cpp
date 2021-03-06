/*****************************
GENERATED FILE DO NOT EDIT
******************************/

#include "fc.h"
#include <stdint.h>

namespace fc {
__attribute__((weak)) void rx(local_timestamp_from_local_to_local msg) {}
__attribute__((weak)) void rx(ms_since_boot_from_test_to_test msg) {}
__attribute__((weak)) void rx(altitude_from_test_to_test msg) {}
__attribute__((weak)) void rx(acceleration_from_test_to_test msg) {}
__attribute__((weak)) void rx(pressure_from_test_to_test msg) {}
__attribute__((weak)) void rx(catastrophe_from_test_to_test msg) {}
__attribute__((weak)) void rx(gyro_from_test_to_test msg) {}
__attribute__((weak)) void
rx(time_sync_from_ground_station_to_flight_controller msg) {}
__attribute__((weak)) void
rx(set_power_mode_from_ground_station_to_flight_controller msg) {}
__attribute__((weak)) void
rx(set_radio_equipment_from_ground_station_to_flight_controller msg) {}
__attribute__((weak)) void
rx(set_parachute_output_from_ground_station_to_flight_controller msg) {}
__attribute__((weak)) void
rx(set_data_logging_from_ground_station_to_flight_controller msg) {}
__attribute__((weak)) void
rx(dump_flash_from_ground_station_to_flight_controller msg) {}
__attribute__((weak)) void
rx(handshake_from_ground_station_to_flight_controller msg) {}
__attribute__((weak)) void
rx(return_time_sync_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(return_power_mode_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(return_radio_equipment_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(return_parachute_output_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(onboard_battery_voltage_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(gnss_data_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(flight_controller_status_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(return_data_logging_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(return_dump_flash_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(return_handshake_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(ms_since_boot_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(us_since_boot_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(current_time_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(GNSS_data_1_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(GNSS_data_2_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(inside_static_temperature_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(inside_static_pressure_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(IMU1_from_flight_controller_to_ground_station msg) {}
__attribute__((weak)) void
rx(IMU2_from_flight_controller_to_ground_station msg) {}
void parse_message(uint8_t id, uint8_t *buf) {
  switch (id) {
  case 255: {
    local_timestamp_from_local_to_local __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 64: {
    ms_since_boot_from_test_to_test __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 0: {
    altitude_from_test_to_test __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 1: {
    acceleration_from_test_to_test __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 2: {
    pressure_from_test_to_test __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 3: {
    catastrophe_from_test_to_test __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 4: {
    gyro_from_test_to_test __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 16: {
    time_sync_from_ground_station_to_flight_controller __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 17: {
    set_power_mode_from_ground_station_to_flight_controller __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 18: {
    set_radio_equipment_from_ground_station_to_flight_controller __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 19: {
    set_parachute_output_from_ground_station_to_flight_controller __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 20: {
    set_data_logging_from_ground_station_to_flight_controller __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 21: {
    dump_flash_from_ground_station_to_flight_controller __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 22: {
    handshake_from_ground_station_to_flight_controller __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 32: {
    return_time_sync_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 33: {
    return_power_mode_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 34: {
    return_radio_equipment_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 35: {
    return_parachute_output_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 36: {
    onboard_battery_voltage_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 37: {
    gnss_data_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 38: {
    flight_controller_status_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 39: {
    return_data_logging_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 40: {
    return_dump_flash_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 41: {
    return_handshake_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 80: {
    ms_since_boot_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 81: {
    us_since_boot_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 82: {
    current_time_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 83: {
    GNSS_data_1_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 84: {
    GNSS_data_2_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 85: {
    inside_static_temperature_from_flight_controller_to_ground_station
        __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 86: {
    inside_static_pressure_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 87: {
    IMU1_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  case 88: {
    IMU2_from_flight_controller_to_ground_station __message;
    __message.parse_buf(buf);
    rx(__message);
    break;
  }
  }
}

bool is_valid_id(uint8_t id) {
  switch (id) {
  case 255:
    return true;
    break;
  case 64:
    return true;
    break;
  case 0:
    return true;
    break;
  case 1:
    return true;
    break;
  case 2:
    return true;
    break;
  case 3:
    return true;
    break;
  case 4:
    return true;
    break;
  case 16:
    return true;
    break;
  case 17:
    return true;
    break;
  case 18:
    return true;
    break;
  case 19:
    return true;
    break;
  case 20:
    return true;
    break;
  case 21:
    return true;
    break;
  case 22:
    return true;
    break;
  case 32:
    return true;
    break;
  case 33:
    return true;
    break;
  case 34:
    return true;
    break;
  case 35:
    return true;
    break;
  case 36:
    return true;
    break;
  case 37:
    return true;
    break;
  case 38:
    return true;
    break;
  case 39:
    return true;
    break;
  case 40:
    return true;
    break;
  case 41:
    return true;
    break;
  case 80:
    return true;
    break;
  case 81:
    return true;
    break;
  case 82:
    return true;
    break;
  case 83:
    return true;
    break;
  case 84:
    return true;
    break;
  case 85:
    return true;
    break;
  case 86:
    return true;
    break;
  case 87:
    return true;
    break;
  case 88:
    return true;
    break;
  default:
    return false;
  }
}

uint8_t id_to_len(uint8_t id) {
  switch (id) {
  case 255:
    return 4;
    break;
  case 64:
    return 4;
    break;
  case 0:
    return 2;
    break;
  case 1:
    return 1;
    break;
  case 2:
    return 2;
    break;
  case 3:
    return 1;
    break;
  case 4:
    return 3;
    break;
  case 16:
    return 4;
    break;
  case 17:
    return 0;
    break;
  case 18:
    return 1;
    break;
  case 19:
    return 1;
    break;
  case 20:
    return 1;
    break;
  case 21:
    return 1;
    break;
  case 22:
    return 0;
    break;
  case 32:
    return 0;
    break;
  case 33:
    return 0;
    break;
  case 34:
    return 1;
    break;
  case 35:
    return 1;
    break;
  case 36:
    return 4;
    break;
  case 37:
    return 15;
    break;
  case 38:
    return 3;
    break;
  case 39:
    return 1;
    break;
  case 40:
    return 1;
    break;
  case 41:
    return 0;
    break;
  case 80:
    return 2;
    break;
  case 81:
    return 4;
    break;
  case 82:
    return 4;
    break;
  case 83:
    return 12;
    break;
  case 84:
    return 12;
    break;
  case 85:
    return 8;
    break;
  case 86:
    return 8;
    break;
  case 87:
    return 18;
    break;
  case 88:
    return 18;
    break;
  default:
    return 0;
  }
}

enum nodes id_to_sender(uint8_t id) {
  switch (id) {
  case 255:
    return nodes::local;
    break;
  case 64:
    return nodes::test;
    break;
  case 0:
    return nodes::test;
    break;
  case 1:
    return nodes::test;
    break;
  case 2:
    return nodes::test;
    break;
  case 3:
    return nodes::test;
    break;
  case 4:
    return nodes::test;
    break;
  case 16:
    return nodes::ground_station;
    break;
  case 17:
    return nodes::ground_station;
    break;
  case 18:
    return nodes::ground_station;
    break;
  case 19:
    return nodes::ground_station;
    break;
  case 20:
    return nodes::ground_station;
    break;
  case 21:
    return nodes::ground_station;
    break;
  case 22:
    return nodes::ground_station;
    break;
  case 32:
    return nodes::flight_controller;
    break;
  case 33:
    return nodes::flight_controller;
    break;
  case 34:
    return nodes::flight_controller;
    break;
  case 35:
    return nodes::flight_controller;
    break;
  case 36:
    return nodes::flight_controller;
    break;
  case 37:
    return nodes::flight_controller;
    break;
  case 38:
    return nodes::flight_controller;
    break;
  case 39:
    return nodes::flight_controller;
    break;
  case 40:
    return nodes::flight_controller;
    break;
  case 41:
    return nodes::flight_controller;
    break;
  case 80:
    return nodes::flight_controller;
    break;
  case 81:
    return nodes::flight_controller;
    break;
  case 82:
    return nodes::flight_controller;
    break;
  case 83:
    return nodes::flight_controller;
    break;
  case 84:
    return nodes::flight_controller;
    break;
  case 85:
    return nodes::flight_controller;
    break;
  case 86:
    return nodes::flight_controller;
    break;
  case 87:
    return nodes::flight_controller;
    break;
  case 88:
    return nodes::flight_controller;
    break;
  }
}

enum nodes id_to_receiver(uint8_t id) {
  switch (id) {
  case 255:
    return nodes::local;
    break;
  case 64:
    return nodes::test;
    break;
  case 0:
    return nodes::test;
    break;
  case 1:
    return nodes::test;
    break;
  case 2:
    return nodes::test;
    break;
  case 3:
    return nodes::test;
    break;
  case 4:
    return nodes::test;
    break;
  case 16:
    return nodes::flight_controller;
    break;
  case 17:
    return nodes::flight_controller;
    break;
  case 18:
    return nodes::flight_controller;
    break;
  case 19:
    return nodes::flight_controller;
    break;
  case 20:
    return nodes::flight_controller;
    break;
  case 21:
    return nodes::flight_controller;
    break;
  case 22:
    return nodes::flight_controller;
    break;
  case 32:
    return nodes::ground_station;
    break;
  case 33:
    return nodes::ground_station;
    break;
  case 34:
    return nodes::ground_station;
    break;
  case 35:
    return nodes::ground_station;
    break;
  case 36:
    return nodes::ground_station;
    break;
  case 37:
    return nodes::ground_station;
    break;
  case 38:
    return nodes::ground_station;
    break;
  case 39:
    return nodes::ground_station;
    break;
  case 40:
    return nodes::ground_station;
    break;
  case 41:
    return nodes::ground_station;
    break;
  case 80:
    return nodes::ground_station;
    break;
  case 81:
    return nodes::ground_station;
    break;
  case 82:
    return nodes::ground_station;
    break;
  case 83:
    return nodes::ground_station;
    break;
  case 84:
    return nodes::ground_station;
    break;
  case 85:
    return nodes::ground_station;
    break;
  case 86:
    return nodes::ground_station;
    break;
  case 87:
    return nodes::ground_station;
    break;
  case 88:
    return nodes::ground_station;
    break;
  }
}

enum categories id_to_category(uint8_t id) {
  switch (id) {
  case 255:
    return categories::none;
    break;
  case 64:
    return categories::none;
    break;
  case 0:
    return categories::none;
    break;
  case 1:
    return categories::none;
    break;
  case 2:
    return categories::none;
    break;
  case 3:
    return categories::none;
    break;
  case 4:
    return categories::none;
    break;
  case 16:
    return categories::none;
    break;
  case 17:
    return categories::none;
    break;
  case 18:
    return categories::none;
    break;
  case 19:
    return categories::none;
    break;
  case 20:
    return categories::none;
    break;
  case 21:
    return categories::none;
    break;
  case 22:
    return categories::none;
    break;
  case 32:
    return categories::none;
    break;
  case 33:
    return categories::none;
    break;
  case 34:
    return categories::none;
    break;
  case 35:
    return categories::none;
    break;
  case 36:
    return categories::none;
    break;
  case 37:
    return categories::none;
    break;
  case 38:
    return categories::none;
    break;
  case 39:
    return categories::none;
    break;
  case 40:
    return categories::none;
    break;
  case 41:
    return categories::none;
    break;
  case 80:
    return categories::none;
    break;
  case 81:
    return categories::none;
    break;
  case 82:
    return categories::none;
    break;
  case 83:
    return categories::none;
    break;
  case 84:
    return categories::none;
    break;
  case 85:
    return categories::none;
    break;
  case 86:
    return categories::none;
    break;
  case 87:
    return categories::none;
    break;
  case 88:
    return categories::none;
    break;
  }
}

} // namespace fc