################################
#GENERATED FILE DO NOT EDIT
################################

from enum import Enum
import struct

def scaledFloat_to_uint(value, scale):
    return value * scale

def uint_to_scaledFloat(value, scale):
    return value / scale

def packedFloat_to_uint(value, minValue, maxValue, size):
    intMax = (1 << size * 8) - 1
    if(value < minValue):
      return 0
    if(value > maxValue):
      return intMax
    ratio = (value - minValue) / (maxValue - minValue)
    return 1 + ((intMax - 2)) * ratio
  
def uint_to_packedFloat(value, minValue, maxValue, size):
    intMax = (1 << size * 8) - 1
    if(value <= 0):
      return minValue - 1.0
    if(value >= intMax):
      return maxValue + 1.0
    ratio = (value - 1) / (intMax - 2)
    return ratio * (maxValue - minValue) + minValue

class units(Enum):
    web = 0
    plant = 1
class fields(Enum):
    SSID = 0
    password = 1
    plant_0 = 2
    plant_1 = 3
    plant_2 = 4
    plant_3 = 5
    plant_4 = 6
    plant_5 = 7
    plant_6 = 8
    plant_7 = 9
    plant_id = 10
    humidity = 11
    lower_limit = 12
    upper_limit = 13
class messages(Enum):
    wifi_config = 0
    get_active_plants = 1
    get_humidity_measurement = 2
    active_plants = 3
    humidity_measurement = 4
    configure_plant = 5
class wifi_config_from_web_to_plant:
    def __init__(self):
        self._source = units.web
        self._target = units.plant
        self._message = messages.wifi_config
        self._id = 1
        self._size = 128
        self._SSID = 0
        self._password = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_SSID(self, value):
        self._SSID = value
    def set_password(self, value):
        self._password = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<64s", self._SSID)
        buf += struct.pack("<64s", self._password)
        return buf
    def get_SSID(self):
        return self._SSID
    def get_password(self):
        return self._password
    def get_all_data(self):
        data = []
        data.append((fields.SSID, self.get_SSID()))
        data.append((fields.password, self.get_password()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._SSID = struct.unpack_from("<64s", buf, index)[0]
        index += 64
        self._password = struct.unpack_from("<64s", buf, index)[0]
        index += 64
        return
class get_active_plants_from_web_to_plant:
    def __init__(self):
        self._source = units.web
        self._target = units.plant
        self._message = messages.get_active_plants
        self._id = 2
        self._size = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def build_buf(self):
        buf = b""
        return buf
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class get_humidity_measurement_from_web_to_plant:
    def __init__(self):
        self._source = units.web
        self._target = units.plant
        self._message = messages.get_humidity_measurement
        self._id = 3
        self._size = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def build_buf(self):
        buf = b""
        return buf
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class active_plants_from_plant_to_web:
    def __init__(self):
        self._source = units.plant
        self._target = units.web
        self._message = messages.active_plants
        self._id = 4
        self._size = 1
        self._bit_field = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_plant_0(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 0)) + (not value) * (self._bit_field & ~(1 << 0))
    def set_plant_1(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 1)) + (not value) * (self._bit_field & ~(1 << 1))
    def set_plant_2(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 2)) + (not value) * (self._bit_field & ~(1 << 2))
    def set_plant_3(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 3)) + (not value) * (self._bit_field & ~(1 << 3))
    def set_plant_4(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 4)) + (not value) * (self._bit_field & ~(1 << 4))
    def set_plant_5(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 5)) + (not value) * (self._bit_field & ~(1 << 5))
    def set_plant_6(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 6)) + (not value) * (self._bit_field & ~(1 << 6))
    def set_plant_7(self, value):
        self._bit_field =  value * (self._bit_field | (1 << 7)) + (not value) * (self._bit_field & ~(1 << 7))
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bit_field)
        return buf
    def get_plant_0(self):
        return self._bit_field & (1 << 0)
    def get_plant_1(self):
        return self._bit_field & (1 << 1)
    def get_plant_2(self):
        return self._bit_field & (1 << 2)
    def get_plant_3(self):
        return self._bit_field & (1 << 3)
    def get_plant_4(self):
        return self._bit_field & (1 << 4)
    def get_plant_5(self):
        return self._bit_field & (1 << 5)
    def get_plant_6(self):
        return self._bit_field & (1 << 6)
    def get_plant_7(self):
        return self._bit_field & (1 << 7)
    def get_all_data(self):
        data = []
        data.append((fields.plant_0, self.get_plant_0()))
        data.append((fields.plant_1, self.get_plant_1()))
        data.append((fields.plant_2, self.get_plant_2()))
        data.append((fields.plant_3, self.get_plant_3()))
        data.append((fields.plant_4, self.get_plant_4()))
        data.append((fields.plant_5, self.get_plant_5()))
        data.append((fields.plant_6, self.get_plant_6()))
        data.append((fields.plant_7, self.get_plant_7()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bit_field = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class humidity_measurement_from_plant_to_web:
    def __init__(self):
        self._source = units.plant
        self._target = units.web
        self._message = messages.humidity_measurement
        self._id = 5
        self._size = 9
        self._plant_id = 0
        self._humidity = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_plant_id(self, value):
        self._plant_id = value
    def set_humidity(self, value):
        self._humidity = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._plant_id)
        buf += struct.pack("<d", self._humidity)
        return buf
    def get_plant_id(self):
        return self._plant_id
    def get_humidity(self):
        return self._humidity
    def get_all_data(self):
        data = []
        data.append((fields.plant_id, self.get_plant_id()))
        data.append((fields.humidity, self.get_humidity()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._plant_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._humidity = struct.unpack_from("<d", buf, index)[0]
        index += 8
        return
class configure_plant_from_web_to_plant:
    def __init__(self):
        self._source = units.web
        self._target = units.plant
        self._message = messages.configure_plant
        self._id = 6
        self._size = 17
        self._plant_id = 0
        self._lower_limit = 0
        self._upper_limit = 0
    def get_source(self):
        return self._source
    def get_target(self):
        return self._target
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def set_plant_id(self, value):
        self._plant_id = value
    def set_lower_limit(self, value):
        self._lower_limit = value
    def set_upper_limit(self, value):
        self._upper_limit = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._plant_id)
        buf += struct.pack("<d", self._lower_limit)
        buf += struct.pack("<d", self._upper_limit)
        return buf
    def get_plant_id(self):
        return self._plant_id
    def get_lower_limit(self):
        return self._lower_limit
    def get_upper_limit(self):
        return self._upper_limit
    def get_all_data(self):
        data = []
        data.append((fields.plant_id, self.get_plant_id()))
        data.append((fields.lower_limit, self.get_lower_limit()))
        data.append((fields.upper_limit, self.get_upper_limit()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._plant_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._lower_limit = struct.unpack_from("<d", buf, index)[0]
        index += 8
        self._upper_limit = struct.unpack_from("<d", buf, index)[0]
        index += 8
        return
def id_to_receiver(id):
    if id == 1:
        receiver = wifi_config_from_web_to_plant()
        return receiver
    if id == 2:
        receiver = get_active_plants_from_web_to_plant()
        return receiver
    if id == 3:
        receiver = get_humidity_measurement_from_web_to_plant()
        return receiver
    if id == 4:
        receiver = active_plants_from_plant_to_web()
        return receiver
    if id == 5:
        receiver = humidity_measurement_from_plant_to_web()
        return receiver
    if id == 6:
        receiver = configure_plant_from_web_to_plant()
        return receiver
