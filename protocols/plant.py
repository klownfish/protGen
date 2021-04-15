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
    plant = 0
    web = 1
class fields(Enum):
    name = 0
    password = 1
class messages(Enum):
    wifi_config = 0
class wifi_config_from_plant_to_web:
    def __init__(self):
        self._source = units.plant
        self._target = units.web
        self._message = messages.wifi_config
        self._id = 1
        self._size = 95
        self._name = 0
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
    def set_name(self, value):
        self._name = value
    def set_password(self, value):
        self._password = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<32s", self._name)
        buf += struct.pack("<63s", self._password)
        return buf
    def get_name(self):
        return self._name
    def get_password(self):
        return self._password
    def get_all_data(self):
        data = []
        data.append((fields.name, self.get_name()))
        data.append((fields.password, self.get_password()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._name = struct.unpack_from("<32s", buf, index)[0]
        index += 32
        self._password = struct.unpack_from("<63s", buf, index)[0]
        index += 63
        return
def id_to_receiver(id):
    if id == 1:
        receiver = wifi_config_from_plant_to_web()
        return receiver
