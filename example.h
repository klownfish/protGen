/*****************************
GENERATED FILE DO NOT EDIT
******************************/

#include <stdint.h>

#define SET_RADIO_EQUIPMENT_IS_FPV_EN (1 << 0)
#define SET_RADIO_EQUIPMENT_IS_TM_EN (1 << 1)

#define SET_PARACHUTE_OUTPUT_IS_PARACHUTE_ARMED (1 << 0)
#define SET_PARACHUTE_OUTPUT_IS_PARACHUTE1_EN (1 << 1)
#define SET_PARACHUTE_OUTPUT_IS_PARACHUTE2_EN (1 << 2)

#define SET_DATA_LOGGING_IS_LOGGING_EN (1 << 0)

#define DUMP_FLASH_CHIP_DUMP_SD (1 << 0)
#define DUMP_FLASH_CHIP_DUMP_USB (1 << 1)

#define RETURN_RADIO_EQUIPMENT_IS_FPV_EN (1 << 0)
#define RETURN_RADIO_EQUIPMENT_IS_TM_EN (1 << 1)

#define RETURN_PARACHUTE_OUTPUT_IS_PARACHUTE_ARMED (1 << 0)
#define RETURN_PARACHUTE_OUTPUT_IS_PARACHUTE1_EN (1 << 1)
#define RETURN_PARACHUTE_OUTPUT_IS_PARACHUTE2_EN (1 << 2)

#define RETURN_DATA_LOGGING_IS_LOGGING_EN (1 << 0)

#define RETURN_DUMP_FLASH_DUMP_SD (1 << 0)
#define RETURN_DUMP_FLASH_DUMP_USB (1 << 1)

enum struct units : uint8_t {
  ground_station = 0,
  flight_controller_tc = 1,
  flight_controller = 2,
  ground_station_tc = 3,
};
template <typename T>
void scaledFloat_to_uint(double value, double scale, T *out) {
  *out = value * scale;
}

template <typename T>
void uint_to_scaledFloat(T value, double scale, double *out) {
  *out = value / scale;
}

template <typename T>
void packedFloat_to_uint(double value, double min, double max, T *out) {
  T max_value = ~0;
  double difference = max - min;
  *out = (value - min) / difference * max_value;
}

template <typename T>
void uint_to_packedFloat(T value, double min, double max, double *out) {
  T max_value = ~0;
  double difference = max - min;
  *out = difference * value / max_value;
}

class time_sync {
public:
  uint32_t system_time;
  uint8_t size = 4;
  uint8_t get_size() { return size; }
  uint64_t id = 16;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) {
    uint8_t index = 0;
    memcpy(&system_time, buf + index, sizeof(system_time));
    index += sizeof(system_time);
  }
  uint32_t get_system_time() { return system_time; }
};

class set_power_mode {
public:
  uint8_t size = 0;
  uint8_t get_size() { return size; }
  uint64_t id = 17;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) { uint8_t index = 0; }
};

class set_radio_equipment {
public:
  uint8_t bit_field;
  uint8_t get_bit_field() { return bit_field; }
  uint8_t size = 1;
  uint8_t get_size() { return size; }
  uint64_t id = 18;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) {
    uint8_t index = 0;
    memcpy(&bit_field, buf + index, sizeof(bit_field));
    index += sizeof(bit_field);
  }
};

class set_parachute_output {
public:
  uint8_t bit_field;
  uint8_t get_bit_field() { return bit_field; }
  uint8_t size = 1;
  uint8_t get_size() { return size; }
  uint64_t id = 19;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) {
    uint8_t index = 0;
    memcpy(&bit_field, buf + index, sizeof(bit_field));
    index += sizeof(bit_field);
  }
};

class set_data_logging {
public:
  uint8_t bit_field;
  uint8_t get_bit_field() { return bit_field; }
  uint8_t size = 1;
  uint8_t get_size() { return size; }
  uint64_t id = 20;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) {
    uint8_t index = 0;
    memcpy(&bit_field, buf + index, sizeof(bit_field));
    index += sizeof(bit_field);
  }
};

class dump_flash_chip {
public:
  uint8_t bit_field;
  uint8_t get_bit_field() { return bit_field; }
  uint8_t size = 1;
  uint8_t get_size() { return size; }
  uint64_t id = 21;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) {
    uint8_t index = 0;
    memcpy(&bit_field, buf + index, sizeof(bit_field));
    index += sizeof(bit_field);
  }
};

class handshake {
public:
  uint8_t size = 0;
  uint8_t get_size() { return size; }
  uint64_t id = 22;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) { uint8_t index = 0; }
};

class return_time_sync {
public:
  uint8_t size = 0;
  uint8_t get_size() { return size; }
  uint64_t id = 32;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) { uint8_t index = 0; }
};

class return_power_mode {
public:
  uint8_t size = 0;
  uint8_t get_size() { return size; }
  uint64_t id = 33;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) { uint8_t index = 0; }
};

class return_radio_equipment {
public:
  uint8_t bit_field;
  uint8_t get_bit_field() { return bit_field; }
  uint8_t size = 1;
  uint8_t get_size() { return size; }
  uint64_t id = 34;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) {
    uint8_t index = 0;
    memcpy(&bit_field, buf + index, sizeof(bit_field));
    index += sizeof(bit_field);
  }
};

class return_parachute_output {
public:
  uint8_t bit_field;
  uint8_t get_bit_field() { return bit_field; }
  uint8_t size = 1;
  uint8_t get_size() { return size; }
  uint64_t id = 35;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) {
    uint8_t index = 0;
    memcpy(&bit_field, buf + index, sizeof(bit_field));
    index += sizeof(bit_field);
  }
};

class onboard_battery_voltage {
public:
  uint16_t battery_1;
  uint16_t battery_2;
  uint8_t size = 4;
  uint8_t get_size() { return size; }
  uint64_t id = 36;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) {
    uint8_t index = 0;
    memcpy(&battery_1, buf + index, sizeof(battery_1));
    index += sizeof(battery_1);
    memcpy(&battery_2, buf + index, sizeof(battery_2));
    index += sizeof(battery_2);
  }
  double get_battery_1() {
    double out;
    uint_to_scaledFloat(battery_1, 100, &out);
    return out;
  }
  double get_battery_2() {
    double out;
    uint_to_scaledFloat(battery_2, 100, &out);
    return out;
  }
};

class gnss_data {
public:
  uint32_t gnss_time;
  int32_t latitude;
  int32_t longitude;
  uint16_t h_dop;
  uint8_t n_satellites;
  uint8_t size = 15;
  uint8_t get_size() { return size; }
  uint64_t id = 37;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) {
    uint8_t index = 0;
    memcpy(&gnss_time, buf + index, sizeof(gnss_time));
    index += sizeof(gnss_time);
    memcpy(&latitude, buf + index, sizeof(latitude));
    index += sizeof(latitude);
    memcpy(&longitude, buf + index, sizeof(longitude));
    index += sizeof(longitude);
    memcpy(&h_dop, buf + index, sizeof(h_dop));
    index += sizeof(h_dop);
    memcpy(&n_satellites, buf + index, sizeof(n_satellites));
    index += sizeof(n_satellites);
  }
  uint32_t get_gnss_time() { return gnss_time; }
  int32_t get_latitude() { return latitude; }
  int32_t get_longitude() { return longitude; }
  double get_h_dop() {
    double out;
    uint_to_scaledFloat(h_dop, 100, &out);
    return out;
  }
  uint8_t get_n_satellites() { return n_satellites; }
};

class flight_controller_status {
public:
  uint8_t HW_state;
  uint8_t SW_state;
  uint8_t mission_state;
  uint8_t size = 3;
  uint8_t get_size() { return size; }
  uint64_t id = 38;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) {
    uint8_t index = 0;
    memcpy(&HW_state, buf + index, sizeof(HW_state));
    index += sizeof(HW_state);
    memcpy(&SW_state, buf + index, sizeof(SW_state));
    index += sizeof(SW_state);
    memcpy(&mission_state, buf + index, sizeof(mission_state));
    index += sizeof(mission_state);
  }
  uint8_t get_HW_state() { return HW_state; }
  uint8_t get_SW_state() { return SW_state; }
  uint8_t get_mission_state() { return mission_state; }
};

class return_data_logging {
public:
  uint8_t bit_field;
  uint8_t get_bit_field() { return bit_field; }
  uint8_t size = 1;
  uint8_t get_size() { return size; }
  uint64_t id = 39;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) {
    uint8_t index = 0;
    memcpy(&bit_field, buf + index, sizeof(bit_field));
    index += sizeof(bit_field);
  }
};

class return_dump_flash {
public:
  uint8_t bit_field;
  uint8_t get_bit_field() { return bit_field; }
  uint8_t size = 1;
  uint8_t get_size() { return size; }
  uint64_t id = 40;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) {
    uint8_t index = 0;
    memcpy(&bit_field, buf + index, sizeof(bit_field));
    index += sizeof(bit_field);
  }
};

class return_handshake {
public:
  uint8_t size = 0;
  uint8_t get_size() { return size; }
  uint64_t id = 41;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void parse_buf(uint8_t *buf) { uint8_t index = 0; }
};

class time_sync_from_ground_station_to_flight_controller_tc {
public:
  uint32_t system_time;
  uint8_t size = 4;
  uint8_t get_size() { return size; }
  uint64_t id = 16;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) {
    *len = 0;
    memcpy(buf + *len, &system_time, sizeof(system_time));
    *len += sizeof(system_time);
  }

  void set_system_time(uint32_t value) { system_time = value; }
};

class set_power_mode_from_ground_station_to_flight_controller_tc {
public:
  uint8_t size = 0;
  uint8_t get_size() { return size; }
  uint64_t id = 17;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) { *len = 0; }
};

class set_radio_equipment_from_ground_station_to_flight_controller_tc {
public:
  uint8_t bit_field;
  void set_bit_field(uint8_t value) { bit_field = value; }
  uint8_t size = 1;
  uint8_t get_size() { return size; }
  uint64_t id = 18;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) {
    *len = 0;
    memcpy(buf + *len, &bit_field, sizeof(bit_field));
    *len += sizeof(bit_field);
  }
};

class set_parachute_output_from_ground_station_to_flight_controller_tc {
public:
  uint8_t bit_field;
  void set_bit_field(uint8_t value) { bit_field = value; }
  uint8_t size = 1;
  uint8_t get_size() { return size; }
  uint64_t id = 19;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) {
    *len = 0;
    memcpy(buf + *len, &bit_field, sizeof(bit_field));
    *len += sizeof(bit_field);
  }
};

class set_data_logging_from_ground_station_to_flight_controller_tc {
public:
  uint8_t bit_field;
  void set_bit_field(uint8_t value) { bit_field = value; }
  uint8_t size = 1;
  uint8_t get_size() { return size; }
  uint64_t id = 20;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) {
    *len = 0;
    memcpy(buf + *len, &bit_field, sizeof(bit_field));
    *len += sizeof(bit_field);
  }
};

class dump_flash_chip_from_ground_station_to_flight_controller_tc {
public:
  uint8_t bit_field;
  void set_bit_field(uint8_t value) { bit_field = value; }
  uint8_t size = 1;
  uint8_t get_size() { return size; }
  uint64_t id = 21;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) {
    *len = 0;
    memcpy(buf + *len, &bit_field, sizeof(bit_field));
    *len += sizeof(bit_field);
  }
};

class handshake_from_ground_station_to_flight_controller_tc {
public:
  uint8_t size = 0;
  uint8_t get_size() { return size; }
  uint64_t id = 22;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) { *len = 0; }
};

class return_time_sync_from_flight_controller_to_ground_station_tc {
public:
  uint8_t size = 0;
  uint8_t get_size() { return size; }
  uint64_t id = 32;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) { *len = 0; }
};

class return_power_mode_from_flight_controller_to_ground_station_tc {
public:
  uint8_t size = 0;
  uint8_t get_size() { return size; }
  uint64_t id = 33;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) { *len = 0; }
};

class return_radio_equipment_from_flight_controller_to_ground_station_tc {
public:
  uint8_t bit_field;
  void set_bit_field(uint8_t value) { bit_field = value; }
  uint8_t size = 1;
  uint8_t get_size() { return size; }
  uint64_t id = 34;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) {
    *len = 0;
    memcpy(buf + *len, &bit_field, sizeof(bit_field));
    *len += sizeof(bit_field);
  }
};

class return_parachute_output_from_flight_controller_to_ground_station_tc {
public:
  uint8_t bit_field;
  void set_bit_field(uint8_t value) { bit_field = value; }
  uint8_t size = 1;
  uint8_t get_size() { return size; }
  uint64_t id = 35;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) {
    *len = 0;
    memcpy(buf + *len, &bit_field, sizeof(bit_field));
    *len += sizeof(bit_field);
  }
};

class onboard_battery_voltage_from_flight_controller_to_ground_station_tc {
public:
  uint16_t battery_1;
  uint16_t battery_2;
  uint8_t size = 4;
  uint8_t get_size() { return size; }
  uint64_t id = 36;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) {
    *len = 0;
    memcpy(buf + *len, &battery_1, sizeof(battery_1));
    *len += sizeof(battery_1);
    memcpy(buf + *len, &battery_2, sizeof(battery_2));
    *len += sizeof(battery_2);
  }

  void set_battery_1(double value) {
    scaledFloat_to_uint(value, 100, &battery_1);
  }

  void set_battery_2(double value) {
    scaledFloat_to_uint(value, 100, &battery_2);
  }
};

class gnss_data_from_flight_controller_to_ground_station_tc {
public:
  uint32_t gnss_time;
  int32_t latitude;
  int32_t longitude;
  uint16_t h_dop;
  uint8_t n_satellites;
  uint8_t size = 15;
  uint8_t get_size() { return size; }
  uint64_t id = 37;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) {
    *len = 0;
    memcpy(buf + *len, &gnss_time, sizeof(gnss_time));
    *len += sizeof(gnss_time);
    memcpy(buf + *len, &latitude, sizeof(latitude));
    *len += sizeof(latitude);
    memcpy(buf + *len, &longitude, sizeof(longitude));
    *len += sizeof(longitude);
    memcpy(buf + *len, &h_dop, sizeof(h_dop));
    *len += sizeof(h_dop);
    memcpy(buf + *len, &n_satellites, sizeof(n_satellites));
    *len += sizeof(n_satellites);
  }

  void set_gnss_time(uint32_t value) { gnss_time = value; }

  void set_latitude(int32_t value) { latitude = value; }

  void set_longitude(int32_t value) { longitude = value; }

  void set_h_dop(double value) { scaledFloat_to_uint(value, 100, &h_dop); }

  void set_n_satellites(uint8_t value) { n_satellites = value; }
};

class flight_controller_status_from_flight_controller_to_ground_station_tc {
public:
  uint8_t HW_state;
  uint8_t SW_state;
  uint8_t mission_state;
  uint8_t size = 3;
  uint8_t get_size() { return size; }
  uint64_t id = 38;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) {
    *len = 0;
    memcpy(buf + *len, &HW_state, sizeof(HW_state));
    *len += sizeof(HW_state);
    memcpy(buf + *len, &SW_state, sizeof(SW_state));
    *len += sizeof(SW_state);
    memcpy(buf + *len, &mission_state, sizeof(mission_state));
    *len += sizeof(mission_state);
  }

  void set_HW_state(uint8_t value) { HW_state = value; }

  void set_SW_state(uint8_t value) { SW_state = value; }

  void set_mission_state(uint8_t value) { mission_state = value; }
};

class return_data_logging_from_flight_controller_to_ground_station_tc {
public:
  uint8_t bit_field;
  void set_bit_field(uint8_t value) { bit_field = value; }
  uint8_t size = 1;
  uint8_t get_size() { return size; }
  uint64_t id = 39;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) {
    *len = 0;
    memcpy(buf + *len, &bit_field, sizeof(bit_field));
    *len += sizeof(bit_field);
  }
};

class return_dump_flash_from_flight_controller_to_ground_station_tc {
public:
  uint8_t bit_field;
  void set_bit_field(uint8_t value) { bit_field = value; }
  uint8_t size = 1;
  uint8_t get_size() { return size; }
  uint64_t id = 40;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) {
    *len = 0;
    memcpy(buf + *len, &bit_field, sizeof(bit_field));
    *len += sizeof(bit_field);
  }
};

class return_handshake_from_flight_controller_to_ground_station_tc {
public:
  uint8_t size = 0;
  uint8_t get_size() { return size; }
  uint64_t id = 41;
  uint64_t get_id() { return id; }
  enum units source;
  enum units target;
  enum units get_source() { return source; }
  enum units get_target() { return target; }
  void set_source(enum units value) { source = value; }
  void set_target(enum units value) { target = value; }
  void build_buf(uint8_t *buf, uint8_t *len) { *len = 0; }
};

#define ID_TO_LEN(id, length)                                                  \
  switch (id) {                                                                \
  case 16:                                                                     \
    length = 4;                                                                \
    break;                                                                     \
  case 17:                                                                     \
    length = 0;                                                                \
    break;                                                                     \
  case 18:                                                                     \
    length = 1;                                                                \
    break;                                                                     \
  case 19:                                                                     \
    length = 1;                                                                \
    break;                                                                     \
  case 20:                                                                     \
    length = 1;                                                                \
    break;                                                                     \
  case 21:                                                                     \
    length = 1;                                                                \
    break;                                                                     \
  case 22:                                                                     \
    length = 0;                                                                \
    break;                                                                     \
  case 32:                                                                     \
    length = 0;                                                                \
    break;                                                                     \
  case 33:                                                                     \
    length = 0;                                                                \
    break;                                                                     \
  case 34:                                                                     \
    length = 1;                                                                \
    break;                                                                     \
  case 35:                                                                     \
    length = 1;                                                                \
    break;                                                                     \
  case 36:                                                                     \
    length = 4;                                                                \
    break;                                                                     \
  case 37:                                                                     \
    length = 15;                                                               \
    break;                                                                     \
  case 38:                                                                     \
    length = 3;                                                                \
    break;                                                                     \
  case 39:                                                                     \
    length = 1;                                                                \
    break;                                                                     \
  case 40:                                                                     \
    length = 1;                                                                \
    break;                                                                     \
  case 41:                                                                     \
    length = 0;                                                                \
    break;                                                                     \
  }

#define PARSE_MESSAGE(id, buf)                                                 \
  switch (id) {                                                                \
  case 16: {                                                                   \
    time_sync __message;                                                       \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::ground_station);                               \
    __message.set_target(units::flight_controller_tc);                         \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  case 17: {                                                                   \
    set_power_mode __message;                                                  \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::ground_station);                               \
    __message.set_target(units::flight_controller_tc);                         \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  case 18: {                                                                   \
    set_radio_equipment __message;                                             \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::ground_station);                               \
    __message.set_target(units::flight_controller_tc);                         \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  case 19: {                                                                   \
    set_parachute_output __message;                                            \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::ground_station);                               \
    __message.set_target(units::flight_controller_tc);                         \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  case 20: {                                                                   \
    set_data_logging __message;                                                \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::ground_station);                               \
    __message.set_target(units::flight_controller_tc);                         \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  case 21: {                                                                   \
    dump_flash_chip __message;                                                 \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::ground_station);                               \
    __message.set_target(units::flight_controller_tc);                         \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  case 22: {                                                                   \
    handshake __message;                                                       \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::ground_station);                               \
    __message.set_target(units::flight_controller_tc);                         \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  case 32: {                                                                   \
    return_time_sync __message;                                                \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::flight_controller);                            \
    __message.set_target(units::ground_station_tc);                            \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  case 33: {                                                                   \
    return_power_mode __message;                                               \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::flight_controller);                            \
    __message.set_target(units::ground_station_tc);                            \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  case 34: {                                                                   \
    return_radio_equipment __message;                                          \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::flight_controller);                            \
    __message.set_target(units::ground_station_tc);                            \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  case 35: {                                                                   \
    return_parachute_output __message;                                         \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::flight_controller);                            \
    __message.set_target(units::ground_station_tc);                            \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  case 36: {                                                                   \
    onboard_battery_voltage __message;                                         \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::flight_controller);                            \
    __message.set_target(units::ground_station_tc);                            \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  case 37: {                                                                   \
    gnss_data __message;                                                       \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::flight_controller);                            \
    __message.set_target(units::ground_station_tc);                            \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  case 38: {                                                                   \
    flight_controller_status __message;                                        \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::flight_controller);                            \
    __message.set_target(units::ground_station_tc);                            \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  case 39: {                                                                   \
    return_data_logging __message;                                             \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::flight_controller);                            \
    __message.set_target(units::ground_station_tc);                            \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  case 40: {                                                                   \
    return_dump_flash __message;                                               \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::flight_controller);                            \
    __message.set_target(units::ground_station_tc);                            \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  case 41: {                                                                   \
    return_handshake __message;                                                \
    __message.parse_buf(buf);                                                  \
    __message.set_source(units::flight_controller);                            \
    __message.set_target(units::ground_station_tc);                            \
    fc_rx(__message);                                                          \
    break;                                                                     \
  }                                                                            \
  }

#define ID_TO_SOURCE(id, source)                                               \
  switch (id) {                                                                \
  case 16:                                                                     \
    source = units::ground_station;                                            \
    break;                                                                     \
  case 17:                                                                     \
    source = units::ground_station;                                            \
    break;                                                                     \
  case 18:                                                                     \
    source = units::ground_station;                                            \
    break;                                                                     \
  case 19:                                                                     \
    source = units::ground_station;                                            \
    break;                                                                     \
  case 20:                                                                     \
    source = units::ground_station;                                            \
    break;                                                                     \
  case 21:                                                                     \
    source = units::ground_station;                                            \
    break;                                                                     \
  case 22:                                                                     \
    source = units::ground_station;                                            \
    break;                                                                     \
  case 32:                                                                     \
    source = units::flight_controller;                                         \
    break;                                                                     \
  case 33:                                                                     \
    source = units::flight_controller;                                         \
    break;                                                                     \
  case 34:                                                                     \
    source = units::flight_controller;                                         \
    break;                                                                     \
  case 35:                                                                     \
    source = units::flight_controller;                                         \
    break;                                                                     \
  case 36:                                                                     \
    source = units::flight_controller;                                         \
    break;                                                                     \
  case 37:                                                                     \
    source = units::flight_controller;                                         \
    break;                                                                     \
  case 38:                                                                     \
    source = units::flight_controller;                                         \
    break;                                                                     \
  case 39:                                                                     \
    source = units::flight_controller;                                         \
    break;                                                                     \
  case 40:                                                                     \
    source = units::flight_controller;                                         \
    break;                                                                     \
  case 41:                                                                     \
    source = units::flight_controller;                                         \
    break;                                                                     \
  }

#define ID_TO_TARGET(id, source)                                               \
  switch (id) {                                                                \
  case 16:                                                                     \
    source = units::flight_controller_tc;                                      \
    break;                                                                     \
  case 17:                                                                     \
    source = units::flight_controller_tc;                                      \
    break;                                                                     \
  case 18:                                                                     \
    source = units::flight_controller_tc;                                      \
    break;                                                                     \
  case 19:                                                                     \
    source = units::flight_controller_tc;                                      \
    break;                                                                     \
  case 20:                                                                     \
    source = units::flight_controller_tc;                                      \
    break;                                                                     \
  case 21:                                                                     \
    source = units::flight_controller_tc;                                      \
    break;                                                                     \
  case 22:                                                                     \
    source = units::flight_controller_tc;                                      \
    break;                                                                     \
  case 32:                                                                     \
    source = units::ground_station_tc;                                         \
    break;                                                                     \
  case 33:                                                                     \
    source = units::ground_station_tc;                                         \
    break;                                                                     \
  case 34:                                                                     \
    source = units::ground_station_tc;                                         \
    break;                                                                     \
  case 35:                                                                     \
    source = units::ground_station_tc;                                         \
    break;                                                                     \
  case 36:                                                                     \
    source = units::ground_station_tc;                                         \
    break;                                                                     \
  case 37:                                                                     \
    source = units::ground_station_tc;                                         \
    break;                                                                     \
  case 38:                                                                     \
    source = units::ground_station_tc;                                         \
    break;                                                                     \
  case 39:                                                                     \
    source = units::ground_station_tc;                                         \
    break;                                                                     \
  case 40:                                                                     \
    source = units::ground_station_tc;                                         \
    break;                                                                     \
  case 41:                                                                     \
    source = units::ground_station_tc;                                         \
    break;                                                                     \
  }
