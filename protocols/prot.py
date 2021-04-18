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

class wifi_config_from_web_to_plant:
    def __init__(self):
        self._sender = nodes.web
        self._receiver = nodes.plant
        self._message = messages.wifi_config
        self._category = categories.none
        self._id = 1
        self._size = 128
        self._SSID = 0
        self._password = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
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
class configure_plant_from_web_to_plant:
    def __init__(self):
        self._sender = nodes.web
        self._receiver = nodes.plant
        self._message = messages.configure_plant
        self._category = categories.none
        self._id = 2
        self._size = 17
        self._plant_id = 0
        self._lower_limit = 0
        self._upper_limit = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
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
class get_active_plants_from_web_to_plant:
    def __init__(self):
        self._sender = nodes.web
        self._receiver = nodes.plant
        self._message = messages.get_active_plants
        self._category = categories.none
        self._id = 3
        self._size = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
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
        self._sender = nodes.web
        self._receiver = nodes.plant
        self._message = messages.get_humidity_measurement
        self._category = categories.none
        self._id = 4
        self._size = 1
        self._plant_id = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_plant_id(self, value):
        self._plant_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._plant_id)
        return buf
    def get_plant_id(self):
        return self._plant_id
    def get_all_data(self):
        data = []
        data.append((fields.plant_id, self.get_plant_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._plant_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class get_configuration_from_web_to_plant:
    def __init__(self):
        self._sender = nodes.web
        self._receiver = nodes.plant
        self._message = messages.get_configuration
        self._category = categories.none
        self._id = 5
        self._size = 1
        self._plant_id = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def set_plant_id(self, value):
        self._plant_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._plant_id)
        return buf
    def get_plant_id(self):
        return self._plant_id
    def get_all_data(self):
        data = []
        data.append((fields.plant_id, self.get_plant_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._plant_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class active_plants_from_plant_to_web:
    def __init__(self):
        self._sender = nodes.plant
        self._receiver = nodes.web
        self._message = messages.active_plants
        self._category = categories.none
        self._id = 6
        self._size = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def build_buf(self):
        buf = b""
        return buf
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
class humidity_measurement_from_plant_to_web:
    def __init__(self):
        self._sender = nodes.plant
        self._receiver = nodes.web
        self._message = messages.humidity_measurement
        self._category = categories.none
        self._id = 7
        self._size = 9
        self._plant_id = 0
        self._humidity = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
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
class configuration_from_plant_to_web:
    def __init__(self):
        self._sender = nodes.plant
        self._receiver = nodes.web
        self._message = messages.configuration
        self._category = categories.none
        self._id = 8
        self._size = 0
    def get_sender(self):
        return self._sender
    def get_receiver(self):
        return self._receiver
    def get_message(self):
        return self._message
    def get_id(self):
        return self._id
    def get_size(self):
        return self._size
    def get_category(self):
        return self._category
    def build_buf(self):
        buf = b""
        return buf
    def get_all_data(self):
        data = []
        return data
    def parse_buf(self, buf):
        index = 0
        return
def id_to_receiver(id):
    if id == 1:
        receiver = wifi_config_from_web_to_plant()
        return receiver
    if id == 2:
        receiver = configure_plant_from_web_to_plant()
        return receiver
    if id == 3:
        receiver = get_active_plants_from_web_to_plant()
        return receiver
    if id == 4:
        receiver = get_humidity_measurement_from_web_to_plant()
        return receiver
    if id == 5:
        receiver = get_configuration_from_web_to_plant()
        return receiver
    if id == 6:
        receiver = active_plants_from_plant_to_web()
        return receiver
    if id == 7:
        receiver = humidity_measurement_from_plant_to_web()
        return receiver
    if id == 8:
        receiver = configuration_from_plant_to_web()
        return receiver
