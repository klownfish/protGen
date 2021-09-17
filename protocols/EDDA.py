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

class fields(Enum):
    currentMillis = 0
    currentMicros = 1
    debugMessagesMode = 2
    debugStatusLedsMode = 3
    powerMode = 4
    uptime_ms = 5
    receiver_node_id = 6
    messages = 7
    statusLeds = 8
    mode = 9
    debug_mode = 10
    powercan_channel = 11
    edda_signature = 12
    request = 13
    timeSpentAwake_ms = 14
    timeSpentSleeping_us = 15
    roundTripTime_us = 16
    destination_node_id = 17
    maxTxQueueSize = 18
    maxRxQueueSize = 19
    meanTxQueueSize = 20
    meanRxQueueSize = 21
    w = 22
    e = 23
    n = 24
    h = 25
    o = 26
    p = 27
    current_amperes = 28
    voltage_volts = 29
    power_watts = 30
    error = 31
    sensor_index = 32
    pressure_millibars = 33
    pressure_pascal = 34
    coefficient_index = 35
    coefficient_value = 36
    sensor_type = 37
    temperature_celsius = 38
    resistance_ohms = 39
    ratio_fraction = 40
    relative_humidity = 41
    is_heater_on = 42
    acceleration_x_gforce = 43
    acceleration_y_gforce = 44
    acceleration_z_gforce = 45
    sign = 46
    result = 47
    ambientLight_lux = 48
    bus = 49
    serial_byte0 = 50
    serial_byte1 = 51
    serial_byte2 = 52
    serial_byte3 = 53
    serial_byte4 = 54
    serial_byte5 = 55
    found_family_code = 56
    found_crc = 57
    system_state = 58
    gate_state = 59
    kind = 60
    channel = 61
    measurement_reference = 62
    failure_reason = 63
    value = 64
    threshold = 65
    validity = 66
    reference_voltage_volts = 67
    differential_voltage_volts = 68
    positive_voltage_volts = 69
    negative_voltage_volts = 70
    location = 71
    register_address = 72
    read_data = 73
    write_data = 74
    expected_data = 75
    checks_failed = 76
    checks_performed = 77
    total_checks = 78
    response = 79
    frequency_hertz = 80
    scanned_address = 81
    found_device_address = 82
    missing_device_address = 83
    devices_successfully_found = 84
    addresses_with_error = 85
    search_time_us = 86
    warning_count = 87
    error_count = 88
    type = 89
    thread_id = 90
    taskTime_microseconds = 91
    truncated_startTime_microseconds = 92
    loopTime_microseconds = 93
    byte0 = 94
    start_time_ms = 95
    board_index = 96
    sensor_board_index = 97
    device_index = 98
    byte1 = 99
    searched_family_code = 100
    devices_insuccessfully_found = 101
    search_time_ms = 102
    raw_fault_register = 103
    byte2 = 104
    byte3 = 105
    byte4 = 106
    byte5 = 107
    byte6 = 108
class messages(Enum):
    CurrentTimePing = 0
    SayHi = 1
    CurrentTimePong = 2
    Hello = 3
    SetDebugModeRequest = 4
    SetPowerModeRequest = 5
    PowerCAN_SetDebugMode = 6
    PowerCAN_GetState = 7
    PowerCAN_TransitionRequest = 8
    GoingToSleep = 9
    WokeUp = 10
    CanLatency = 11
    CanStatistics = 12
    WenHop = 13
    PowerInputMeasurement = 14
    PowerInputMeasurementError = 15
    RawTransducerVoltage = 16
    AmbientPressure = 17
    TransducerPressure = 18
    TransducerError = 19
    AmbientPressureError = 20
    AmbientPressureCoefficient = 21
    ColdSideTemperature = 22
    PlatinumSensorTemperature = 23
    PlatinumSensorResistance = 24
    PlatinumSensorRatio = 25
    ThermocoupleTypeKTemperature = 26
    Humidity = 27
    HumidityError = 28
    Acceleration = 29
    AccelerationSelfTest = 30
    AccelerationError = 31
    AmbientLight = 32
    AmbientLightError = 33
    OneWireSearchFamilyMismatch = 34
    OneWireSearchCRCMismatch = 35
    OneWireSearchFoundDevice = 36
    PowerCAN_Hello = 37
    PowerCAN_CurrentState = 38
    PowerCAN_Temperature = 39
    PowerCAN_Voltage = 40
    PowerCAN_ChannelMeasurementPower = 41
    PowerCAN_ChannelMeasurementVoltage = 42
    PowerCAN_ChannelMeasurementCurrent = 43
    PowerCAN_LoadMeasurementResistance = 44
    PowerCAN_LoadMeasurementVoltage = 45
    PowerCAN_LoadMeasurementPower = 46
    PowerCAN_LoadMeasurementCurrent = 47
    PowerCAN_FailedLoadMeasurementValue = 48
    PowerCAN_FailedLoadMeasurementThreshold = 49
    PowerCAN_ResistanceMeasurementResistance = 50
    PowerCAN_ResistanceMeasurementReferenceVoltage = 51
    PowerCAN_ResistanceMeasurementDifferentialVoltage = 52
    PowerCAN_ResistanceMeasurementPositiveVoltage = 53
    PowerCAN_ResistanceMeasurementNegativeVoltage = 54
    PowerCAN_LTC2992Error = 55
    PowerCAN_ADS122C04Error = 56
    PowerCAN_CheckResult = 57
    PowerCAN_TransitionResponse = 58
    PowerCAN_I2CBusStarted = 59
    PowerCAN_I2CSearchStarted = 60
    PowerCAN_I2CSearchError = 61
    PowerCAN_I2CSearchFoundDevice = 62
    PowerCAN_I2CSearchMissingDevice = 63
    PowerCAN_I2CSearchEnded = 64
    PowerCAN_ErrorStatistics = 65
    TaskInfo = 66
    LoopInfo = 67
    DS28E18QError = 68
    PartialDebugMessage1 = 69
    OneWireSearchStarted = 70
    TemperatureBoardBridgeError = 71
    I2CBusStarted = 72
    MAX31850KError = 73
    PartialDebugMessage2 = 74
    OneWireSearchEnded = 75
    I2CSearchStarted = 76
    MAX31856Error = 77
    PartialDebugMessage3 = 78
    OneWireDeviceStartupSuccess = 79
    I2CSearchError = 80
    MAX31865Error = 81
    PartialDebugMessage4 = 82
    OneWireDeviceStartupFailure = 83
    I2CSearchFoundDevice = 84
    PartialDebugMessage5 = 85
    OneWireDevicePairedWithSensor = 86
    I2CSearchEnded = 87
    PartialDebugMessage6 = 88
    PartialDebugMessage7 = 89
class categories(Enum):
    none = 0
class nodes(Enum):
    Flight_Controller = 0
    Edda_Controller = 1
    Edda_Telemetry = 2
    Edda_Pressure_Top = 3
    Edda_Pressure_Bottom = 4
    Edda_Simulator = 5
    Ground_Controller = 16
class AccelerationSelfTestDirection(Enum):
    Positive = 0
    Negative = 1
class AccelerationSelfTestResult(Enum):
    Success = 0
    Failure = 1
class ADS122C04Error(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
class ColdSideTemperatureSensorType(Enum):
    InternalTemperature = 0
    PowerRegulator = 1
    AmbientPressureSensor = 2
    ThermocoupleColdSide = 3
    HumiditySensor = 4
class DebugMessagesMode(Enum):
    Enabled = 0
    Disabled = 1
class DebugStatusLedsMode(Enum):
    Enabled = 0
    Disabled = 1
class DS2482Error(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
    BusShortDetected = 7
    NoDevicesResponded = 8
    ConfigError = 9
    WaitOnBusyTimeout = 10
    ResetFailure = 11
class DS28E18QError(Enum):
    RequestCRCFailure = 0
    ResponseCRCFailure = 1
    InvalidRequestLength = 2
    InvalidResponseLength = 3
    TransactionFailed = 4
    ExecutionError = 5
    PowerOnResetError = 6
    FailedNackAtCommand = 7
    InvalidInput = 8
    InvalidResult = 9
    InvalidStatusByte = 10
    Unknown = 11
class I2CBus(Enum):
    Wire0 = 0
    Wire1 = 1
    Wire2 = 2
    Unknown = 3
class I2CError(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
class INA260Error(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
    UnexpectedManufacturer = 7
    UnexpectedDie = 8
    UnexpectedConfiguration = 9
    UnexpectedMask = 10
    UnexpectedAlertLimit = 11
class LIS331Error(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
    FailedSelfTestX = 7
    FailedSelfTestY = 8
    FailedSelfTestZ = 9
    InitializationTimeout = 10
class LoopType(Enum):
    MainLoop = 0
    ChitchatLoop = 1
    RGBLoop = 2
    GenericThreadLoop = 3
    EddaLoop = 4
class LTR303Error(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
    UnexpectedManufacturer = 7
    UnexpectedPartNumber = 8
    ReadOldData = 9
    DataIsInvalid = 10
    DataWasReadWithWrongGain = 11
class MAX31850KError(Enum):
    CRCMismatch = 0
    OneWireUnknownError = 1
    SensorShortToVDD = 2
    SensorShortToGND = 3
    SensorOpenCircuit = 4
class MS5803Error(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
    D1BelowBounds = 7
    D1AboveBounds = 8
    D2BelowBounds = 9
    D2AboveBounds = 10
    Value_dT_BelowBounds = 11
    Value_dT_AboveBounds = 12
    Value_TEMP_BelowBounds = 13
    Value_TEMP_AboveBounds = 14
    Value_OFF_BelowBounds = 15
    Value_OFF_AboveBounds = 16
    Value_SENS_BelowBounds = 17
    Value_SENS_AboveBounds = 18
    Value_P_BelowBounds = 19
    Value_P_AboveBounds = 20
class OneWireBus(Enum):
    Bus0A = 0
    Bus0B = 1
    Bus1A = 2
    Bus1B = 3
    Unknown = 4
class PowerCAN_ADS122C04Error(Enum):
    I2CArbitration = 0
    I2CBus = 1
    I2CBusy = 2
    I2CNack = 3
    I2CUnknownError = 4
    RegisterWriteFailed = 5
    RegisterResetFailed = 6
class PowerCAN_ADS122C04ErrorLocation(Enum):
    WriteRegister = 0
    ReadRegister = 1
    Reset = 2
    Start = 3
    Stop = 4
    ReadData = 5
    LMAONone = 6
class PowerCAN_CheckResult(Enum):
    SomeFailed = 0
    AllFailed = 1
    AllPassed = 2
    NotYetDone = 3
class PowerCAN_DebugMode(Enum):
    Enabled = 0
    Disabled = 1
class PowerCAN_GateState(Enum):
    Grounded = 0
    ResistanceMeasurement = 1
    High = 2
class PowerCAN_I2CBus(Enum):
    Wire0 = 0
    Wire1 = 1
    Wire2 = 2
    Unknown = 3
class PowerCAN_I2CError(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
class PowerCAN_LoadMeasurementResult(Enum):
    Passed = 0
    Failed = 1
    Invalid = 2
class PowerCAN_LTC2992Error(Enum):
    I2CArbitration = 0
    I2CBus = 1
    I2CBusy = 2
    I2CNack = 3
    I2CUnknownError = 4
    RegisterWriteFailed = 5
    RegisterResetFailed = 6
class PowerCAN_LTC2992ErrorLocation(Enum):
    WriteRegister = 0
    ReadRegister = 1
    Reset = 2
    LoadVoltage = 3
    BoardVoltage = 4
    LoadCurrent = 5
    BoardCurrent = 6
    LoadPower = 7
    BoardPower = 8
    GPIO1 = 9
    GPIO2 = 10
    GPIO3 = 11
    GPIO4 = 12
    LMAONone = 13
class PowerCAN_MeasurementChannel(Enum):
    Load = 0
    Board = 1
class PowerCAN_MeasurementFailureReason(Enum):
    PowerAboveMax = 0
    PowerBelowMin = 1
    CurrentAboveMax = 2
    CurrentBelowMin = 3
    VoltageAboveMax = 4
    VoltageBelowMin = 5
    ResistanceAboveMax = 6
    ResistanceBelowMin = 7
class PowerCAN_MeasurementReference(Enum):
    Internal = 0
    ExternalReference = 1
    Supply = 2
class PowerCAN_ResistanceMeasurementReference(Enum):
    Internal = 0
    ExternalReference = 1
    Supply = 2
class PowerCAN_ResistanceMeasurementValidity(Enum):
    Valid = 0
    Invalid = 1
class PowerCAN_SystemState(Enum):
    Idle = 0
    Arming = 1
    Armed = 2
    Firing = 3
class PowerCAN_TemperatureKind(Enum):
    ADC = 0
    Gates = 1
class PowerCAN_TransitionRequest(Enum):
    Arm = 0
    Disarm = 1
    Fire = 2
    StopFire = 3
class PowerCAN_TransitionResponse(Enum):
    Success = 0
    Failure = 1
class PowerCAN_VoltageKind(Enum):
    Board3V3 = 0
class PowerCANChannel(Enum):
    Channel0_Unknown = 0
    Channel1_Ignition = 1
    Channel2_VentSolenoid = 2
    Channel3_MainValveSolenoid = 3
    Channel4_Unknown = 4
    Channel5_Unknown = 5
    Channel6_Unknown = 6
    Channel7_Unknown = 7
    Channel8_Unknown = 8
    Channel9_Unknown = 9
    Channel10_Unknown = 10
    Channel11_Unknown = 11
    Channel12_Unknown = 12
    Channel13_Unknown = 13
    Channel14_Unknown = 14
    Channel15_Unknown = 15
    Unknown = 16
class PowerMode(Enum):
    Active = 0
    Hibernate = 1
class SHT31Error(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
class TaskType(Enum):
    Startup = 0
    CANSetup = 1
    PeripheralSetup = 2
    SensorSetup = 3
    ThreadSetup = 4
    RGBSetup = 5
    MainLoop = 6
    ChitchatLoop = 7
    RGBLoop = 8
    GenericThreadLoop = 9
    EddaLoop = 10
    Wire0Start = 11
    Wire1Start = 12
    Wire2Start = 13
    StartTemperatureBusA = 14
    StartTemperatureBusB = 15
class TransducerError(Enum):
    LMAONone = 0
    CRCMismatch = 1
    I2CUnknownError = 2
    I2CReceiveBufferEmpty = 3
    I2CAddressNack = 4
    I2CDataNack = 5
    I2CTransmitBufferFull = 6
    Undervoltage = 7
    Overvoltage = 8
class CurrentTimePing_from_Flight_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.CurrentTimePing
        self._category = categories.none
        self._id = 0
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePing_from_Flight_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.CurrentTimePing
        self._category = categories.none
        self._id = 0
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePing_from_Flight_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.CurrentTimePing
        self._category = categories.none
        self._id = 0
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePing_from_Flight_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.CurrentTimePing
        self._category = categories.none
        self._id = 0
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePing_from_Flight_Controller_to_Edda_Simulator:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Simulator
        self._message = messages.CurrentTimePing
        self._category = categories.none
        self._id = 0
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class SayHi_from_Flight_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 1
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
class SayHi_from_Flight_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 1
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
class SayHi_from_Flight_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 1
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
class SayHi_from_Flight_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 1
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
class SayHi_from_Flight_Controller_to_Edda_Simulator:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Simulator
        self._message = messages.SayHi
        self._category = categories.none
        self._id = 1
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
class CurrentTimePong_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.CurrentTimePong
        self._category = categories.none
        self._id = 4
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePong_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.CurrentTimePong
        self._category = categories.none
        self._id = 5
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePong_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.CurrentTimePong
        self._category = categories.none
        self._id = 6
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePong_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.CurrentTimePong
        self._category = categories.none
        self._id = 7
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CurrentTimePong_from_Edda_Simulator_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Flight_Controller
        self._message = messages.CurrentTimePong
        self._category = categories.none
        self._id = 8
        self._size = 8
        self._currentMillis = 0
        self._currentMicros = 0
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
    def set_currentMillis(self, value):
        self._currentMillis = value
    def set_currentMicros(self, value):
        self._currentMicros = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._currentMillis)
        buf += struct.pack("<L", self._currentMicros)
        return buf
    def get_currentMillis(self):
        return self._currentMillis
    def get_currentMicros(self):
        return self._currentMicros
    def get_all_data(self):
        data = []
        data.append((fields.currentMillis, self.get_currentMillis()))
        data.append((fields.currentMicros, self.get_currentMicros()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._currentMillis = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._currentMicros = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class Hello_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.Hello
        self._category = categories.none
        self._id = 9
        self._size = 7
        self._debugMessagesMode = 0
        self._debugStatusLedsMode = 0
        self._powerMode = 0
        self._uptime_ms = 0
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
    def set_debugMessagesMode(self, value):
        self._debugMessagesMode = value.value
    def set_debugStatusLedsMode(self, value):
        self._debugStatusLedsMode = value.value
    def set_powerMode(self, value):
        self._powerMode = value.value
    def set_uptime_ms(self, value):
        self._uptime_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debugMessagesMode)
        buf += struct.pack("<B", self._debugStatusLedsMode)
        buf += struct.pack("<B", self._powerMode)
        buf += struct.pack("<L", self._uptime_ms)
        return buf
    def get_debugMessagesMode(self):
        return DebugMessagesMode(self._debugMessagesMode)
    def get_debugStatusLedsMode(self):
        return DebugStatusLedsMode(self._debugStatusLedsMode)
    def get_powerMode(self):
        return PowerMode(self._powerMode)
    def get_uptime_ms(self):
        return self._uptime_ms
    def get_all_data(self):
        data = []
        data.append((fields.debugMessagesMode, self.get_debugMessagesMode()))
        data.append((fields.debugStatusLedsMode, self.get_debugStatusLedsMode()))
        data.append((fields.powerMode, self.get_powerMode()))
        data.append((fields.uptime_ms, self.get_uptime_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debugMessagesMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debugStatusLedsMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powerMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._uptime_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class Hello_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.Hello
        self._category = categories.none
        self._id = 10
        self._size = 7
        self._debugMessagesMode = 0
        self._debugStatusLedsMode = 0
        self._powerMode = 0
        self._uptime_ms = 0
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
    def set_debugMessagesMode(self, value):
        self._debugMessagesMode = value.value
    def set_debugStatusLedsMode(self, value):
        self._debugStatusLedsMode = value.value
    def set_powerMode(self, value):
        self._powerMode = value.value
    def set_uptime_ms(self, value):
        self._uptime_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debugMessagesMode)
        buf += struct.pack("<B", self._debugStatusLedsMode)
        buf += struct.pack("<B", self._powerMode)
        buf += struct.pack("<L", self._uptime_ms)
        return buf
    def get_debugMessagesMode(self):
        return DebugMessagesMode(self._debugMessagesMode)
    def get_debugStatusLedsMode(self):
        return DebugStatusLedsMode(self._debugStatusLedsMode)
    def get_powerMode(self):
        return PowerMode(self._powerMode)
    def get_uptime_ms(self):
        return self._uptime_ms
    def get_all_data(self):
        data = []
        data.append((fields.debugMessagesMode, self.get_debugMessagesMode()))
        data.append((fields.debugStatusLedsMode, self.get_debugStatusLedsMode()))
        data.append((fields.powerMode, self.get_powerMode()))
        data.append((fields.uptime_ms, self.get_uptime_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debugMessagesMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debugStatusLedsMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powerMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._uptime_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class Hello_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.Hello
        self._category = categories.none
        self._id = 11
        self._size = 7
        self._debugMessagesMode = 0
        self._debugStatusLedsMode = 0
        self._powerMode = 0
        self._uptime_ms = 0
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
    def set_debugMessagesMode(self, value):
        self._debugMessagesMode = value.value
    def set_debugStatusLedsMode(self, value):
        self._debugStatusLedsMode = value.value
    def set_powerMode(self, value):
        self._powerMode = value.value
    def set_uptime_ms(self, value):
        self._uptime_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debugMessagesMode)
        buf += struct.pack("<B", self._debugStatusLedsMode)
        buf += struct.pack("<B", self._powerMode)
        buf += struct.pack("<L", self._uptime_ms)
        return buf
    def get_debugMessagesMode(self):
        return DebugMessagesMode(self._debugMessagesMode)
    def get_debugStatusLedsMode(self):
        return DebugStatusLedsMode(self._debugStatusLedsMode)
    def get_powerMode(self):
        return PowerMode(self._powerMode)
    def get_uptime_ms(self):
        return self._uptime_ms
    def get_all_data(self):
        data = []
        data.append((fields.debugMessagesMode, self.get_debugMessagesMode()))
        data.append((fields.debugStatusLedsMode, self.get_debugStatusLedsMode()))
        data.append((fields.powerMode, self.get_powerMode()))
        data.append((fields.uptime_ms, self.get_uptime_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debugMessagesMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debugStatusLedsMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powerMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._uptime_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class Hello_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.Hello
        self._category = categories.none
        self._id = 12
        self._size = 7
        self._debugMessagesMode = 0
        self._debugStatusLedsMode = 0
        self._powerMode = 0
        self._uptime_ms = 0
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
    def set_debugMessagesMode(self, value):
        self._debugMessagesMode = value.value
    def set_debugStatusLedsMode(self, value):
        self._debugStatusLedsMode = value.value
    def set_powerMode(self, value):
        self._powerMode = value.value
    def set_uptime_ms(self, value):
        self._uptime_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debugMessagesMode)
        buf += struct.pack("<B", self._debugStatusLedsMode)
        buf += struct.pack("<B", self._powerMode)
        buf += struct.pack("<L", self._uptime_ms)
        return buf
    def get_debugMessagesMode(self):
        return DebugMessagesMode(self._debugMessagesMode)
    def get_debugStatusLedsMode(self):
        return DebugStatusLedsMode(self._debugStatusLedsMode)
    def get_powerMode(self):
        return PowerMode(self._powerMode)
    def get_uptime_ms(self):
        return self._uptime_ms
    def get_all_data(self):
        data = []
        data.append((fields.debugMessagesMode, self.get_debugMessagesMode()))
        data.append((fields.debugStatusLedsMode, self.get_debugStatusLedsMode()))
        data.append((fields.powerMode, self.get_powerMode()))
        data.append((fields.uptime_ms, self.get_uptime_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debugMessagesMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debugStatusLedsMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powerMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._uptime_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class Hello_from_Edda_Simulator_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Flight_Controller
        self._message = messages.Hello
        self._category = categories.none
        self._id = 13
        self._size = 7
        self._debugMessagesMode = 0
        self._debugStatusLedsMode = 0
        self._powerMode = 0
        self._uptime_ms = 0
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
    def set_debugMessagesMode(self, value):
        self._debugMessagesMode = value.value
    def set_debugStatusLedsMode(self, value):
        self._debugStatusLedsMode = value.value
    def set_powerMode(self, value):
        self._powerMode = value.value
    def set_uptime_ms(self, value):
        self._uptime_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debugMessagesMode)
        buf += struct.pack("<B", self._debugStatusLedsMode)
        buf += struct.pack("<B", self._powerMode)
        buf += struct.pack("<L", self._uptime_ms)
        return buf
    def get_debugMessagesMode(self):
        return DebugMessagesMode(self._debugMessagesMode)
    def get_debugStatusLedsMode(self):
        return DebugStatusLedsMode(self._debugStatusLedsMode)
    def get_powerMode(self):
        return PowerMode(self._powerMode)
    def get_uptime_ms(self):
        return self._uptime_ms
    def get_all_data(self):
        data = []
        data.append((fields.debugMessagesMode, self.get_debugMessagesMode()))
        data.append((fields.debugStatusLedsMode, self.get_debugStatusLedsMode()))
        data.append((fields.powerMode, self.get_powerMode()))
        data.append((fields.uptime_ms, self.get_uptime_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debugMessagesMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._debugStatusLedsMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powerMode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._uptime_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class SetDebugModeRequest_from_Flight_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.SetDebugModeRequest
        self._category = categories.none
        self._id = 48
        self._size = 3
        self._receiver_node_id = 0
        self._messages = 0
        self._statusLeds = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_messages(self, value):
        self._messages = value.value
    def set_statusLeds(self, value):
        self._statusLeds = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._messages)
        buf += struct.pack("<B", self._statusLeds)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_messages(self):
        return DebugMessagesMode(self._messages)
    def get_statusLeds(self):
        return DebugStatusLedsMode(self._statusLeds)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.messages, self.get_messages()))
        data.append((fields.statusLeds, self.get_statusLeds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._messages = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._statusLeds = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetDebugModeRequest_from_Flight_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.SetDebugModeRequest
        self._category = categories.none
        self._id = 48
        self._size = 3
        self._receiver_node_id = 0
        self._messages = 0
        self._statusLeds = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_messages(self, value):
        self._messages = value.value
    def set_statusLeds(self, value):
        self._statusLeds = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._messages)
        buf += struct.pack("<B", self._statusLeds)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_messages(self):
        return DebugMessagesMode(self._messages)
    def get_statusLeds(self):
        return DebugStatusLedsMode(self._statusLeds)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.messages, self.get_messages()))
        data.append((fields.statusLeds, self.get_statusLeds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._messages = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._statusLeds = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetDebugModeRequest_from_Flight_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.SetDebugModeRequest
        self._category = categories.none
        self._id = 48
        self._size = 3
        self._receiver_node_id = 0
        self._messages = 0
        self._statusLeds = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_messages(self, value):
        self._messages = value.value
    def set_statusLeds(self, value):
        self._statusLeds = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._messages)
        buf += struct.pack("<B", self._statusLeds)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_messages(self):
        return DebugMessagesMode(self._messages)
    def get_statusLeds(self):
        return DebugStatusLedsMode(self._statusLeds)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.messages, self.get_messages()))
        data.append((fields.statusLeds, self.get_statusLeds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._messages = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._statusLeds = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetDebugModeRequest_from_Flight_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.SetDebugModeRequest
        self._category = categories.none
        self._id = 48
        self._size = 3
        self._receiver_node_id = 0
        self._messages = 0
        self._statusLeds = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_messages(self, value):
        self._messages = value.value
    def set_statusLeds(self, value):
        self._statusLeds = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._messages)
        buf += struct.pack("<B", self._statusLeds)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_messages(self):
        return DebugMessagesMode(self._messages)
    def get_statusLeds(self):
        return DebugStatusLedsMode(self._statusLeds)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.messages, self.get_messages()))
        data.append((fields.statusLeds, self.get_statusLeds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._messages = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._statusLeds = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetDebugModeRequest_from_Flight_Controller_to_Edda_Simulator:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Simulator
        self._message = messages.SetDebugModeRequest
        self._category = categories.none
        self._id = 48
        self._size = 3
        self._receiver_node_id = 0
        self._messages = 0
        self._statusLeds = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_messages(self, value):
        self._messages = value.value
    def set_statusLeds(self, value):
        self._statusLeds = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._messages)
        buf += struct.pack("<B", self._statusLeds)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_messages(self):
        return DebugMessagesMode(self._messages)
    def get_statusLeds(self):
        return DebugStatusLedsMode(self._statusLeds)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.messages, self.get_messages()))
        data.append((fields.statusLeds, self.get_statusLeds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._messages = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._statusLeds = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetPowerModeRequest_from_Flight_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.SetPowerModeRequest
        self._category = categories.none
        self._id = 49
        self._size = 2
        self._receiver_node_id = 0
        self._mode = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_mode(self, value):
        self._mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._mode)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_mode(self):
        return PowerMode(self._mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.mode, self.get_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetPowerModeRequest_from_Flight_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.SetPowerModeRequest
        self._category = categories.none
        self._id = 49
        self._size = 2
        self._receiver_node_id = 0
        self._mode = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_mode(self, value):
        self._mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._mode)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_mode(self):
        return PowerMode(self._mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.mode, self.get_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetPowerModeRequest_from_Flight_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.SetPowerModeRequest
        self._category = categories.none
        self._id = 49
        self._size = 2
        self._receiver_node_id = 0
        self._mode = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_mode(self, value):
        self._mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._mode)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_mode(self):
        return PowerMode(self._mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.mode, self.get_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetPowerModeRequest_from_Flight_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.SetPowerModeRequest
        self._category = categories.none
        self._id = 49
        self._size = 2
        self._receiver_node_id = 0
        self._mode = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_mode(self, value):
        self._mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._mode)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_mode(self):
        return PowerMode(self._mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.mode, self.get_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class SetPowerModeRequest_from_Flight_Controller_to_Edda_Simulator:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Simulator
        self._message = messages.SetPowerModeRequest
        self._category = categories.none
        self._id = 49
        self._size = 2
        self._receiver_node_id = 0
        self._mode = 0
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
    def set_receiver_node_id(self, value):
        self._receiver_node_id = value
    def set_mode(self, value):
        self._mode = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._receiver_node_id)
        buf += struct.pack("<B", self._mode)
        return buf
    def get_receiver_node_id(self):
        return self._receiver_node_id
    def get_mode(self):
        return PowerMode(self._mode)
    def get_all_data(self):
        data = []
        data.append((fields.receiver_node_id, self.get_receiver_node_id()))
        data.append((fields.mode, self.get_mode()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._receiver_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_SetDebugMode_from_Ground_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.PowerCAN_SetDebugMode
        self._category = categories.none
        self._id = 50
        self._size = 2
        self._debug_mode = 0
        self._powercan_channel = 0
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
    def set_debug_mode(self, value):
        self._debug_mode = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debug_mode)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_debug_mode(self):
        return PowerCAN_DebugMode(self._debug_mode)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.debug_mode, self.get_debug_mode()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debug_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_GetState_from_Ground_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.PowerCAN_GetState
        self._category = categories.none
        self._id = 51
        self._size = 1
        self._powercan_channel = 0
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
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_TransitionRequest_from_Ground_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Ground_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.PowerCAN_TransitionRequest
        self._category = categories.none
        self._id = 52
        self._size = 4
        self._edda_signature = 0
        self._request = 0
        self._powercan_channel = 0
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
    def set_edda_signature(self, value):
        self._edda_signature = value
    def set_request(self, value):
        self._request = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._edda_signature)
        buf += struct.pack("<B", self._request)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_edda_signature(self):
        return self._edda_signature
    def get_request(self):
        return PowerCAN_TransitionRequest(self._request)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.edda_signature, self.get_edda_signature()))
        data.append((fields.request, self.get_request()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._edda_signature = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._request = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class GoingToSleep_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.GoingToSleep
        self._category = categories.none
        self._id = 64
        self._size = 4
        self._timeSpentAwake_ms = 0
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
    def set_timeSpentAwake_ms(self, value):
        self._timeSpentAwake_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentAwake_ms)
        return buf
    def get_timeSpentAwake_ms(self):
        return self._timeSpentAwake_ms
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentAwake_ms, self.get_timeSpentAwake_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentAwake_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class GoingToSleep_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.GoingToSleep
        self._category = categories.none
        self._id = 65
        self._size = 4
        self._timeSpentAwake_ms = 0
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
    def set_timeSpentAwake_ms(self, value):
        self._timeSpentAwake_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentAwake_ms)
        return buf
    def get_timeSpentAwake_ms(self):
        return self._timeSpentAwake_ms
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentAwake_ms, self.get_timeSpentAwake_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentAwake_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class GoingToSleep_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.GoingToSleep
        self._category = categories.none
        self._id = 66
        self._size = 4
        self._timeSpentAwake_ms = 0
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
    def set_timeSpentAwake_ms(self, value):
        self._timeSpentAwake_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentAwake_ms)
        return buf
    def get_timeSpentAwake_ms(self):
        return self._timeSpentAwake_ms
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentAwake_ms, self.get_timeSpentAwake_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentAwake_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class GoingToSleep_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.GoingToSleep
        self._category = categories.none
        self._id = 67
        self._size = 4
        self._timeSpentAwake_ms = 0
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
    def set_timeSpentAwake_ms(self, value):
        self._timeSpentAwake_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentAwake_ms)
        return buf
    def get_timeSpentAwake_ms(self):
        return self._timeSpentAwake_ms
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentAwake_ms, self.get_timeSpentAwake_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentAwake_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class GoingToSleep_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.GoingToSleep
        self._category = categories.none
        self._id = 68
        self._size = 4
        self._timeSpentAwake_ms = 0
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
    def set_timeSpentAwake_ms(self, value):
        self._timeSpentAwake_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentAwake_ms)
        return buf
    def get_timeSpentAwake_ms(self):
        return self._timeSpentAwake_ms
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentAwake_ms, self.get_timeSpentAwake_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentAwake_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class WokeUp_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.WokeUp
        self._category = categories.none
        self._id = 69
        self._size = 4
        self._timeSpentSleeping_us = 0
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
    def set_timeSpentSleeping_us(self, value):
        self._timeSpentSleeping_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentSleeping_us)
        return buf
    def get_timeSpentSleeping_us(self):
        return self._timeSpentSleeping_us
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentSleeping_us, self.get_timeSpentSleeping_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentSleeping_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class WokeUp_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.WokeUp
        self._category = categories.none
        self._id = 70
        self._size = 4
        self._timeSpentSleeping_us = 0
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
    def set_timeSpentSleeping_us(self, value):
        self._timeSpentSleeping_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentSleeping_us)
        return buf
    def get_timeSpentSleeping_us(self):
        return self._timeSpentSleeping_us
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentSleeping_us, self.get_timeSpentSleeping_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentSleeping_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class WokeUp_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.WokeUp
        self._category = categories.none
        self._id = 71
        self._size = 4
        self._timeSpentSleeping_us = 0
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
    def set_timeSpentSleeping_us(self, value):
        self._timeSpentSleeping_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentSleeping_us)
        return buf
    def get_timeSpentSleeping_us(self):
        return self._timeSpentSleeping_us
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentSleeping_us, self.get_timeSpentSleeping_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentSleeping_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class WokeUp_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.WokeUp
        self._category = categories.none
        self._id = 72
        self._size = 4
        self._timeSpentSleeping_us = 0
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
    def set_timeSpentSleeping_us(self, value):
        self._timeSpentSleeping_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentSleeping_us)
        return buf
    def get_timeSpentSleeping_us(self):
        return self._timeSpentSleeping_us
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentSleeping_us, self.get_timeSpentSleeping_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentSleeping_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class WokeUp_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.WokeUp
        self._category = categories.none
        self._id = 73
        self._size = 4
        self._timeSpentSleeping_us = 0
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
    def set_timeSpentSleeping_us(self, value):
        self._timeSpentSleeping_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._timeSpentSleeping_us)
        return buf
    def get_timeSpentSleeping_us(self):
        return self._timeSpentSleeping_us
    def get_all_data(self):
        data = []
        data.append((fields.timeSpentSleeping_us, self.get_timeSpentSleeping_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._timeSpentSleeping_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class CanLatency_from_Flight_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanLatency
        self._category = categories.none
        self._id = 144
        self._size = 5
        self._roundTripTime_us = 0
        self._destination_node_id = 0
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
    def set_roundTripTime_us(self, value):
        self._roundTripTime_us = value
    def set_destination_node_id(self, value):
        self._destination_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._roundTripTime_us)
        buf += struct.pack("<B", self._destination_node_id)
        return buf
    def get_roundTripTime_us(self):
        return self._roundTripTime_us
    def get_destination_node_id(self):
        return self._destination_node_id
    def get_all_data(self):
        data = []
        data.append((fields.roundTripTime_us, self.get_roundTripTime_us()))
        data.append((fields.destination_node_id, self.get_destination_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._roundTripTime_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._destination_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CanLatency_from_Flight_Controller_to_Edda_Controller:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Controller
        self._message = messages.CanLatency
        self._category = categories.none
        self._id = 144
        self._size = 5
        self._roundTripTime_us = 0
        self._destination_node_id = 0
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
    def set_roundTripTime_us(self, value):
        self._roundTripTime_us = value
    def set_destination_node_id(self, value):
        self._destination_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._roundTripTime_us)
        buf += struct.pack("<B", self._destination_node_id)
        return buf
    def get_roundTripTime_us(self):
        return self._roundTripTime_us
    def get_destination_node_id(self):
        return self._destination_node_id
    def get_all_data(self):
        data = []
        data.append((fields.roundTripTime_us, self.get_roundTripTime_us()))
        data.append((fields.destination_node_id, self.get_destination_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._roundTripTime_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._destination_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CanLatency_from_Flight_Controller_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.CanLatency
        self._category = categories.none
        self._id = 144
        self._size = 5
        self._roundTripTime_us = 0
        self._destination_node_id = 0
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
    def set_roundTripTime_us(self, value):
        self._roundTripTime_us = value
    def set_destination_node_id(self, value):
        self._destination_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._roundTripTime_us)
        buf += struct.pack("<B", self._destination_node_id)
        return buf
    def get_roundTripTime_us(self):
        return self._roundTripTime_us
    def get_destination_node_id(self):
        return self._destination_node_id
    def get_all_data(self):
        data = []
        data.append((fields.roundTripTime_us, self.get_roundTripTime_us()))
        data.append((fields.destination_node_id, self.get_destination_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._roundTripTime_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._destination_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CanLatency_from_Flight_Controller_to_Edda_Pressure_Top:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Top
        self._message = messages.CanLatency
        self._category = categories.none
        self._id = 144
        self._size = 5
        self._roundTripTime_us = 0
        self._destination_node_id = 0
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
    def set_roundTripTime_us(self, value):
        self._roundTripTime_us = value
    def set_destination_node_id(self, value):
        self._destination_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._roundTripTime_us)
        buf += struct.pack("<B", self._destination_node_id)
        return buf
    def get_roundTripTime_us(self):
        return self._roundTripTime_us
    def get_destination_node_id(self):
        return self._destination_node_id
    def get_all_data(self):
        data = []
        data.append((fields.roundTripTime_us, self.get_roundTripTime_us()))
        data.append((fields.destination_node_id, self.get_destination_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._roundTripTime_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._destination_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CanLatency_from_Flight_Controller_to_Edda_Pressure_Bottom:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Pressure_Bottom
        self._message = messages.CanLatency
        self._category = categories.none
        self._id = 144
        self._size = 5
        self._roundTripTime_us = 0
        self._destination_node_id = 0
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
    def set_roundTripTime_us(self, value):
        self._roundTripTime_us = value
    def set_destination_node_id(self, value):
        self._destination_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._roundTripTime_us)
        buf += struct.pack("<B", self._destination_node_id)
        return buf
    def get_roundTripTime_us(self):
        return self._roundTripTime_us
    def get_destination_node_id(self):
        return self._destination_node_id
    def get_all_data(self):
        data = []
        data.append((fields.roundTripTime_us, self.get_roundTripTime_us()))
        data.append((fields.destination_node_id, self.get_destination_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._roundTripTime_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._destination_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CanLatency_from_Flight_Controller_to_Edda_Simulator:
    def __init__(self):
        self._sender = nodes.Flight_Controller
        self._receiver = nodes.Edda_Simulator
        self._message = messages.CanLatency
        self._category = categories.none
        self._id = 144
        self._size = 5
        self._roundTripTime_us = 0
        self._destination_node_id = 0
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
    def set_roundTripTime_us(self, value):
        self._roundTripTime_us = value
    def set_destination_node_id(self, value):
        self._destination_node_id = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<L", self._roundTripTime_us)
        buf += struct.pack("<B", self._destination_node_id)
        return buf
    def get_roundTripTime_us(self):
        return self._roundTripTime_us
    def get_destination_node_id(self):
        return self._destination_node_id
    def get_all_data(self):
        data = []
        data.append((fields.roundTripTime_us, self.get_roundTripTime_us()))
        data.append((fields.destination_node_id, self.get_destination_node_id()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._roundTripTime_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._destination_node_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class CanStatistics_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanStatistics
        self._category = categories.none
        self._id = 145
        self._size = 8
        self._maxTxQueueSize = 0
        self._maxRxQueueSize = 0
        self._meanTxQueueSize = 0
        self._meanRxQueueSize = 0
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
    def set_maxTxQueueSize(self, value):
        self._maxTxQueueSize = value
    def set_maxRxQueueSize(self, value):
        self._maxRxQueueSize = value
    def set_meanTxQueueSize(self, value):
        self._meanTxQueueSize = value
    def set_meanRxQueueSize(self, value):
        self._meanRxQueueSize = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._maxTxQueueSize)
        buf += struct.pack("<H", self._maxRxQueueSize)
        buf += struct.pack("<H", self._meanTxQueueSize)
        buf += struct.pack("<H", self._meanRxQueueSize)
        return buf
    def get_maxTxQueueSize(self):
        return self._maxTxQueueSize
    def get_maxRxQueueSize(self):
        return self._maxRxQueueSize
    def get_meanTxQueueSize(self):
        return self._meanTxQueueSize
    def get_meanRxQueueSize(self):
        return self._meanRxQueueSize
    def get_all_data(self):
        data = []
        data.append((fields.maxTxQueueSize, self.get_maxTxQueueSize()))
        data.append((fields.maxRxQueueSize, self.get_maxRxQueueSize()))
        data.append((fields.meanTxQueueSize, self.get_meanTxQueueSize()))
        data.append((fields.meanRxQueueSize, self.get_meanRxQueueSize()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._maxTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._maxRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class CanStatistics_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanStatistics
        self._category = categories.none
        self._id = 146
        self._size = 8
        self._maxTxQueueSize = 0
        self._maxRxQueueSize = 0
        self._meanTxQueueSize = 0
        self._meanRxQueueSize = 0
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
    def set_maxTxQueueSize(self, value):
        self._maxTxQueueSize = value
    def set_maxRxQueueSize(self, value):
        self._maxRxQueueSize = value
    def set_meanTxQueueSize(self, value):
        self._meanTxQueueSize = value
    def set_meanRxQueueSize(self, value):
        self._meanRxQueueSize = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._maxTxQueueSize)
        buf += struct.pack("<H", self._maxRxQueueSize)
        buf += struct.pack("<H", self._meanTxQueueSize)
        buf += struct.pack("<H", self._meanRxQueueSize)
        return buf
    def get_maxTxQueueSize(self):
        return self._maxTxQueueSize
    def get_maxRxQueueSize(self):
        return self._maxRxQueueSize
    def get_meanTxQueueSize(self):
        return self._meanTxQueueSize
    def get_meanRxQueueSize(self):
        return self._meanRxQueueSize
    def get_all_data(self):
        data = []
        data.append((fields.maxTxQueueSize, self.get_maxTxQueueSize()))
        data.append((fields.maxRxQueueSize, self.get_maxRxQueueSize()))
        data.append((fields.meanTxQueueSize, self.get_meanTxQueueSize()))
        data.append((fields.meanRxQueueSize, self.get_meanRxQueueSize()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._maxTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._maxRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class CanStatistics_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanStatistics
        self._category = categories.none
        self._id = 147
        self._size = 8
        self._maxTxQueueSize = 0
        self._maxRxQueueSize = 0
        self._meanTxQueueSize = 0
        self._meanRxQueueSize = 0
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
    def set_maxTxQueueSize(self, value):
        self._maxTxQueueSize = value
    def set_maxRxQueueSize(self, value):
        self._maxRxQueueSize = value
    def set_meanTxQueueSize(self, value):
        self._meanTxQueueSize = value
    def set_meanRxQueueSize(self, value):
        self._meanRxQueueSize = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._maxTxQueueSize)
        buf += struct.pack("<H", self._maxRxQueueSize)
        buf += struct.pack("<H", self._meanTxQueueSize)
        buf += struct.pack("<H", self._meanRxQueueSize)
        return buf
    def get_maxTxQueueSize(self):
        return self._maxTxQueueSize
    def get_maxRxQueueSize(self):
        return self._maxRxQueueSize
    def get_meanTxQueueSize(self):
        return self._meanTxQueueSize
    def get_meanRxQueueSize(self):
        return self._meanRxQueueSize
    def get_all_data(self):
        data = []
        data.append((fields.maxTxQueueSize, self.get_maxTxQueueSize()))
        data.append((fields.maxRxQueueSize, self.get_maxRxQueueSize()))
        data.append((fields.meanTxQueueSize, self.get_meanTxQueueSize()))
        data.append((fields.meanRxQueueSize, self.get_meanRxQueueSize()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._maxTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._maxRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class CanStatistics_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanStatistics
        self._category = categories.none
        self._id = 148
        self._size = 8
        self._maxTxQueueSize = 0
        self._maxRxQueueSize = 0
        self._meanTxQueueSize = 0
        self._meanRxQueueSize = 0
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
    def set_maxTxQueueSize(self, value):
        self._maxTxQueueSize = value
    def set_maxRxQueueSize(self, value):
        self._maxRxQueueSize = value
    def set_meanTxQueueSize(self, value):
        self._meanTxQueueSize = value
    def set_meanRxQueueSize(self, value):
        self._meanRxQueueSize = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._maxTxQueueSize)
        buf += struct.pack("<H", self._maxRxQueueSize)
        buf += struct.pack("<H", self._meanTxQueueSize)
        buf += struct.pack("<H", self._meanRxQueueSize)
        return buf
    def get_maxTxQueueSize(self):
        return self._maxTxQueueSize
    def get_maxRxQueueSize(self):
        return self._maxRxQueueSize
    def get_meanTxQueueSize(self):
        return self._meanTxQueueSize
    def get_meanRxQueueSize(self):
        return self._meanRxQueueSize
    def get_all_data(self):
        data = []
        data.append((fields.maxTxQueueSize, self.get_maxTxQueueSize()))
        data.append((fields.maxRxQueueSize, self.get_maxRxQueueSize()))
        data.append((fields.meanTxQueueSize, self.get_meanTxQueueSize()))
        data.append((fields.meanRxQueueSize, self.get_meanRxQueueSize()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._maxTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._maxRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class CanStatistics_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.CanStatistics
        self._category = categories.none
        self._id = 149
        self._size = 8
        self._maxTxQueueSize = 0
        self._maxRxQueueSize = 0
        self._meanTxQueueSize = 0
        self._meanRxQueueSize = 0
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
    def set_maxTxQueueSize(self, value):
        self._maxTxQueueSize = value
    def set_maxRxQueueSize(self, value):
        self._maxRxQueueSize = value
    def set_meanTxQueueSize(self, value):
        self._meanTxQueueSize = value
    def set_meanRxQueueSize(self, value):
        self._meanRxQueueSize = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._maxTxQueueSize)
        buf += struct.pack("<H", self._maxRxQueueSize)
        buf += struct.pack("<H", self._meanTxQueueSize)
        buf += struct.pack("<H", self._meanRxQueueSize)
        return buf
    def get_maxTxQueueSize(self):
        return self._maxTxQueueSize
    def get_maxRxQueueSize(self):
        return self._maxRxQueueSize
    def get_meanTxQueueSize(self):
        return self._meanTxQueueSize
    def get_meanRxQueueSize(self):
        return self._meanRxQueueSize
    def get_all_data(self):
        data = []
        data.append((fields.maxTxQueueSize, self.get_maxTxQueueSize()))
        data.append((fields.maxRxQueueSize, self.get_maxRxQueueSize()))
        data.append((fields.meanTxQueueSize, self.get_meanTxQueueSize()))
        data.append((fields.meanRxQueueSize, self.get_meanRxQueueSize()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._maxTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._maxRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanTxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._meanRxQueueSize = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class WenHop_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.WenHop
        self._category = categories.none
        self._id = 150
        self._size = 6
        self._w = 0
        self._e = 0
        self._n = 0
        self._h = 0
        self._o = 0
        self._p = 0
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
    def set_w(self, value):
        self._w = value
    def set_e(self, value):
        self._e = value
    def set_n(self, value):
        self._n = value
    def set_h(self, value):
        self._h = value
    def set_o(self, value):
        self._o = value
    def set_p(self, value):
        self._p = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._w)
        buf += struct.pack("<B", self._e)
        buf += struct.pack("<B", self._n)
        buf += struct.pack("<B", self._h)
        buf += struct.pack("<B", self._o)
        buf += struct.pack("<B", self._p)
        return buf
    def get_w(self):
        return self._w
    def get_e(self):
        return self._e
    def get_n(self):
        return self._n
    def get_h(self):
        return self._h
    def get_o(self):
        return self._o
    def get_p(self):
        return self._p
    def get_all_data(self):
        data = []
        data.append((fields.w, self.get_w()))
        data.append((fields.e, self.get_e()))
        data.append((fields.n, self.get_n()))
        data.append((fields.h, self.get_h()))
        data.append((fields.o, self.get_o()))
        data.append((fields.p, self.get_p()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._w = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._e = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._n = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._h = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._o = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._p = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class WenHop_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.WenHop
        self._category = categories.none
        self._id = 151
        self._size = 6
        self._w = 0
        self._e = 0
        self._n = 0
        self._h = 0
        self._o = 0
        self._p = 0
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
    def set_w(self, value):
        self._w = value
    def set_e(self, value):
        self._e = value
    def set_n(self, value):
        self._n = value
    def set_h(self, value):
        self._h = value
    def set_o(self, value):
        self._o = value
    def set_p(self, value):
        self._p = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._w)
        buf += struct.pack("<B", self._e)
        buf += struct.pack("<B", self._n)
        buf += struct.pack("<B", self._h)
        buf += struct.pack("<B", self._o)
        buf += struct.pack("<B", self._p)
        return buf
    def get_w(self):
        return self._w
    def get_e(self):
        return self._e
    def get_n(self):
        return self._n
    def get_h(self):
        return self._h
    def get_o(self):
        return self._o
    def get_p(self):
        return self._p
    def get_all_data(self):
        data = []
        data.append((fields.w, self.get_w()))
        data.append((fields.e, self.get_e()))
        data.append((fields.n, self.get_n()))
        data.append((fields.h, self.get_h()))
        data.append((fields.o, self.get_o()))
        data.append((fields.p, self.get_p()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._w = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._e = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._n = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._h = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._o = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._p = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class WenHop_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.WenHop
        self._category = categories.none
        self._id = 152
        self._size = 6
        self._w = 0
        self._e = 0
        self._n = 0
        self._h = 0
        self._o = 0
        self._p = 0
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
    def set_w(self, value):
        self._w = value
    def set_e(self, value):
        self._e = value
    def set_n(self, value):
        self._n = value
    def set_h(self, value):
        self._h = value
    def set_o(self, value):
        self._o = value
    def set_p(self, value):
        self._p = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._w)
        buf += struct.pack("<B", self._e)
        buf += struct.pack("<B", self._n)
        buf += struct.pack("<B", self._h)
        buf += struct.pack("<B", self._o)
        buf += struct.pack("<B", self._p)
        return buf
    def get_w(self):
        return self._w
    def get_e(self):
        return self._e
    def get_n(self):
        return self._n
    def get_h(self):
        return self._h
    def get_o(self):
        return self._o
    def get_p(self):
        return self._p
    def get_all_data(self):
        data = []
        data.append((fields.w, self.get_w()))
        data.append((fields.e, self.get_e()))
        data.append((fields.n, self.get_n()))
        data.append((fields.h, self.get_h()))
        data.append((fields.o, self.get_o()))
        data.append((fields.p, self.get_p()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._w = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._e = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._n = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._h = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._o = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._p = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class WenHop_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.WenHop
        self._category = categories.none
        self._id = 153
        self._size = 6
        self._w = 0
        self._e = 0
        self._n = 0
        self._h = 0
        self._o = 0
        self._p = 0
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
    def set_w(self, value):
        self._w = value
    def set_e(self, value):
        self._e = value
    def set_n(self, value):
        self._n = value
    def set_h(self, value):
        self._h = value
    def set_o(self, value):
        self._o = value
    def set_p(self, value):
        self._p = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._w)
        buf += struct.pack("<B", self._e)
        buf += struct.pack("<B", self._n)
        buf += struct.pack("<B", self._h)
        buf += struct.pack("<B", self._o)
        buf += struct.pack("<B", self._p)
        return buf
    def get_w(self):
        return self._w
    def get_e(self):
        return self._e
    def get_n(self):
        return self._n
    def get_h(self):
        return self._h
    def get_o(self):
        return self._o
    def get_p(self):
        return self._p
    def get_all_data(self):
        data = []
        data.append((fields.w, self.get_w()))
        data.append((fields.e, self.get_e()))
        data.append((fields.n, self.get_n()))
        data.append((fields.h, self.get_h()))
        data.append((fields.o, self.get_o()))
        data.append((fields.p, self.get_p()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._w = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._e = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._n = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._h = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._o = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._p = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class WenHop_from_Edda_Simulator_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Flight_Controller
        self._message = messages.WenHop
        self._category = categories.none
        self._id = 154
        self._size = 6
        self._w = 0
        self._e = 0
        self._n = 0
        self._h = 0
        self._o = 0
        self._p = 0
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
    def set_w(self, value):
        self._w = value
    def set_e(self, value):
        self._e = value
    def set_n(self, value):
        self._n = value
    def set_h(self, value):
        self._h = value
    def set_o(self, value):
        self._o = value
    def set_p(self, value):
        self._p = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._w)
        buf += struct.pack("<B", self._e)
        buf += struct.pack("<B", self._n)
        buf += struct.pack("<B", self._h)
        buf += struct.pack("<B", self._o)
        buf += struct.pack("<B", self._p)
        return buf
    def get_w(self):
        return self._w
    def get_e(self):
        return self._e
    def get_n(self):
        return self._n
    def get_h(self):
        return self._h
    def get_o(self):
        return self._o
    def get_p(self):
        return self._p
    def get_all_data(self):
        data = []
        data.append((fields.w, self.get_w()))
        data.append((fields.e, self.get_e()))
        data.append((fields.n, self.get_n()))
        data.append((fields.h, self.get_h()))
        data.append((fields.o, self.get_o()))
        data.append((fields.p, self.get_p()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._w = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._e = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._n = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._h = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._o = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._p = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerInputMeasurement_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurement
        self._category = categories.none
        self._id = 155
        self._size = 6
        self._current_amperes = 0
        self._voltage_volts = 0
        self._power_watts = 0
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
    def set_current_amperes(self, value):
        self._current_amperes = packedFloat_to_uint(value, -15, 15, 2)
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, 0, 36, 2)
    def set_power_watts(self, value):
        self._power_watts = packedFloat_to_uint(value, -540, 540, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._current_amperes)
        buf += struct.pack("<H", self._voltage_volts)
        buf += struct.pack("<H", self._power_watts)
        return buf
    def get_current_amperes(self):
        return uint_to_packedFloat(self._current_amperes, -15, 15, 2)
    def get_voltage_volts(self):
        return uint_to_packedFloat(self._voltage_volts, 0, 36, 2)
    def get_power_watts(self):
        return uint_to_packedFloat(self._power_watts, -540, 540, 2)
    def get_all_data(self):
        data = []
        data.append((fields.current_amperes, self.get_current_amperes()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        data.append((fields.power_watts, self.get_power_watts()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_amperes = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._voltage_volts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._power_watts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerInputMeasurement_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurement
        self._category = categories.none
        self._id = 156
        self._size = 6
        self._current_amperes = 0
        self._voltage_volts = 0
        self._power_watts = 0
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
    def set_current_amperes(self, value):
        self._current_amperes = packedFloat_to_uint(value, -15, 15, 2)
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, 0, 36, 2)
    def set_power_watts(self, value):
        self._power_watts = packedFloat_to_uint(value, -540, 540, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._current_amperes)
        buf += struct.pack("<H", self._voltage_volts)
        buf += struct.pack("<H", self._power_watts)
        return buf
    def get_current_amperes(self):
        return uint_to_packedFloat(self._current_amperes, -15, 15, 2)
    def get_voltage_volts(self):
        return uint_to_packedFloat(self._voltage_volts, 0, 36, 2)
    def get_power_watts(self):
        return uint_to_packedFloat(self._power_watts, -540, 540, 2)
    def get_all_data(self):
        data = []
        data.append((fields.current_amperes, self.get_current_amperes()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        data.append((fields.power_watts, self.get_power_watts()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_amperes = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._voltage_volts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._power_watts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerInputMeasurement_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurement
        self._category = categories.none
        self._id = 157
        self._size = 6
        self._current_amperes = 0
        self._voltage_volts = 0
        self._power_watts = 0
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
    def set_current_amperes(self, value):
        self._current_amperes = packedFloat_to_uint(value, -15, 15, 2)
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, 0, 36, 2)
    def set_power_watts(self, value):
        self._power_watts = packedFloat_to_uint(value, -540, 540, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._current_amperes)
        buf += struct.pack("<H", self._voltage_volts)
        buf += struct.pack("<H", self._power_watts)
        return buf
    def get_current_amperes(self):
        return uint_to_packedFloat(self._current_amperes, -15, 15, 2)
    def get_voltage_volts(self):
        return uint_to_packedFloat(self._voltage_volts, 0, 36, 2)
    def get_power_watts(self):
        return uint_to_packedFloat(self._power_watts, -540, 540, 2)
    def get_all_data(self):
        data = []
        data.append((fields.current_amperes, self.get_current_amperes()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        data.append((fields.power_watts, self.get_power_watts()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_amperes = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._voltage_volts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._power_watts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerInputMeasurement_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurement
        self._category = categories.none
        self._id = 158
        self._size = 6
        self._current_amperes = 0
        self._voltage_volts = 0
        self._power_watts = 0
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
    def set_current_amperes(self, value):
        self._current_amperes = packedFloat_to_uint(value, -15, 15, 2)
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, 0, 36, 2)
    def set_power_watts(self, value):
        self._power_watts = packedFloat_to_uint(value, -540, 540, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._current_amperes)
        buf += struct.pack("<H", self._voltage_volts)
        buf += struct.pack("<H", self._power_watts)
        return buf
    def get_current_amperes(self):
        return uint_to_packedFloat(self._current_amperes, -15, 15, 2)
    def get_voltage_volts(self):
        return uint_to_packedFloat(self._voltage_volts, 0, 36, 2)
    def get_power_watts(self):
        return uint_to_packedFloat(self._power_watts, -540, 540, 2)
    def get_all_data(self):
        data = []
        data.append((fields.current_amperes, self.get_current_amperes()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        data.append((fields.power_watts, self.get_power_watts()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_amperes = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._voltage_volts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._power_watts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerInputMeasurement_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurement
        self._category = categories.none
        self._id = 159
        self._size = 6
        self._current_amperes = 0
        self._voltage_volts = 0
        self._power_watts = 0
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
    def set_current_amperes(self, value):
        self._current_amperes = packedFloat_to_uint(value, -15, 15, 2)
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, 0, 36, 2)
    def set_power_watts(self, value):
        self._power_watts = packedFloat_to_uint(value, -540, 540, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._current_amperes)
        buf += struct.pack("<H", self._voltage_volts)
        buf += struct.pack("<H", self._power_watts)
        return buf
    def get_current_amperes(self):
        return uint_to_packedFloat(self._current_amperes, -15, 15, 2)
    def get_voltage_volts(self):
        return uint_to_packedFloat(self._voltage_volts, 0, 36, 2)
    def get_power_watts(self):
        return uint_to_packedFloat(self._power_watts, -540, 540, 2)
    def get_all_data(self):
        data = []
        data.append((fields.current_amperes, self.get_current_amperes()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        data.append((fields.power_watts, self.get_power_watts()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._current_amperes = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._voltage_volts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._power_watts = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class PowerInputMeasurementError_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurementError
        self._category = categories.none
        self._id = 160
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return INA260Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerInputMeasurementError_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurementError
        self._category = categories.none
        self._id = 161
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return INA260Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerInputMeasurementError_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurementError
        self._category = categories.none
        self._id = 162
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return INA260Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerInputMeasurementError_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurementError
        self._category = categories.none
        self._id = 163
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return INA260Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerInputMeasurementError_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerInputMeasurementError
        self._category = categories.none
        self._id = 164
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return INA260Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class RawTransducerVoltage_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.RawTransducerVoltage
        self._category = categories.none
        self._id = 165
        self._size = 5
        self._sensor_index = 0
        self._voltage_volts = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, -0.2, 5.2, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._voltage_volts)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_voltage_volts(self):
        return uint_to_packedFloat(self._voltage_volts, -0.2, 5.2, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._voltage_volts = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class RawTransducerVoltage_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.RawTransducerVoltage
        self._category = categories.none
        self._id = 166
        self._size = 5
        self._sensor_index = 0
        self._voltage_volts = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, -0.2, 5.2, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._voltage_volts)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_voltage_volts(self):
        return uint_to_packedFloat(self._voltage_volts, -0.2, 5.2, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._voltage_volts = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class AmbientPressure_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressure
        self._category = categories.none
        self._id = 167
        self._size = 5
        self._sensor_index = 0
        self._pressure_millibars = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_pressure_millibars(self, value):
        self._pressure_millibars = packedFloat_to_uint(value, 0, 10000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_millibars)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_millibars(self):
        return uint_to_packedFloat(self._pressure_millibars, 0, 10000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.pressure_millibars, self.get_pressure_millibars()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._pressure_millibars = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class AmbientPressure_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressure
        self._category = categories.none
        self._id = 168
        self._size = 5
        self._sensor_index = 0
        self._pressure_millibars = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_pressure_millibars(self, value):
        self._pressure_millibars = packedFloat_to_uint(value, 0, 10000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_millibars)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_millibars(self):
        return uint_to_packedFloat(self._pressure_millibars, 0, 10000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.pressure_millibars, self.get_pressure_millibars()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._pressure_millibars = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class AmbientPressure_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressure
        self._category = categories.none
        self._id = 169
        self._size = 5
        self._sensor_index = 0
        self._pressure_millibars = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_pressure_millibars(self, value):
        self._pressure_millibars = packedFloat_to_uint(value, 0, 10000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_millibars)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_millibars(self):
        return uint_to_packedFloat(self._pressure_millibars, 0, 10000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.pressure_millibars, self.get_pressure_millibars()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._pressure_millibars = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class TransducerPressure_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.TransducerPressure
        self._category = categories.none
        self._id = 170
        self._size = 5
        self._sensor_index = 0
        self._pressure_pascal = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_pressure_pascal(self, value):
        self._pressure_pascal = packedFloat_to_uint(value, 0, 10000000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_pascal)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_pascal(self):
        return uint_to_packedFloat(self._pressure_pascal, 0, 10000000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.pressure_pascal, self.get_pressure_pascal()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._pressure_pascal = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class TransducerPressure_from_Edda_Pressure_Top_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.TransducerPressure
        self._category = categories.none
        self._id = 170
        self._size = 5
        self._sensor_index = 0
        self._pressure_pascal = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_pressure_pascal(self, value):
        self._pressure_pascal = packedFloat_to_uint(value, 0, 10000000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_pascal)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_pascal(self):
        return uint_to_packedFloat(self._pressure_pascal, 0, 10000000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.pressure_pascal, self.get_pressure_pascal()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._pressure_pascal = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class TransducerPressure_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.TransducerPressure
        self._category = categories.none
        self._id = 171
        self._size = 5
        self._sensor_index = 0
        self._pressure_pascal = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_pressure_pascal(self, value):
        self._pressure_pascal = packedFloat_to_uint(value, 0, 10000000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_pascal)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_pascal(self):
        return uint_to_packedFloat(self._pressure_pascal, 0, 10000000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.pressure_pascal, self.get_pressure_pascal()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._pressure_pascal = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class TransducerPressure_from_Edda_Pressure_Bottom_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.TransducerPressure
        self._category = categories.none
        self._id = 171
        self._size = 5
        self._sensor_index = 0
        self._pressure_pascal = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_pressure_pascal(self, value):
        self._pressure_pascal = packedFloat_to_uint(value, 0, 10000000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_pascal)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_pascal(self):
        return uint_to_packedFloat(self._pressure_pascal, 0, 10000000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.pressure_pascal, self.get_pressure_pascal()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._pressure_pascal = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class TransducerPressure_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.TransducerPressure
        self._category = categories.none
        self._id = 172
        self._size = 5
        self._sensor_index = 0
        self._pressure_pascal = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_pressure_pascal(self, value):
        self._pressure_pascal = packedFloat_to_uint(value, 0, 10000000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_pascal)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_pascal(self):
        return uint_to_packedFloat(self._pressure_pascal, 0, 10000000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.pressure_pascal, self.get_pressure_pascal()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._pressure_pascal = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class TransducerPressure_from_Edda_Simulator_to_Edda_Telemetry:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Edda_Telemetry
        self._message = messages.TransducerPressure
        self._category = categories.none
        self._id = 172
        self._size = 5
        self._sensor_index = 0
        self._pressure_pascal = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_pressure_pascal(self, value):
        self._pressure_pascal = packedFloat_to_uint(value, 0, 10000000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._pressure_pascal)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_pressure_pascal(self):
        return uint_to_packedFloat(self._pressure_pascal, 0, 10000000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.pressure_pascal, self.get_pressure_pascal()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._pressure_pascal = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class TransducerError_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.TransducerError
        self._category = categories.none
        self._id = 173
        self._size = 2
        self._sensor_index = 0
        self._error = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._error)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_error(self):
        return TransducerError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class TransducerError_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.TransducerError
        self._category = categories.none
        self._id = 174
        self._size = 2
        self._sensor_index = 0
        self._error = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._error)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_error(self):
        return TransducerError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class TransducerError_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.TransducerError
        self._category = categories.none
        self._id = 175
        self._size = 2
        self._sensor_index = 0
        self._error = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._error)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_error(self):
        return TransducerError(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class AmbientPressureError_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressureError
        self._category = categories.none
        self._id = 176
        self._size = 2
        self._sensor_index = 0
        self._error = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._error)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_error(self):
        return MS5803Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class AmbientPressureError_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressureError
        self._category = categories.none
        self._id = 177
        self._size = 2
        self._sensor_index = 0
        self._error = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._error)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_error(self):
        return MS5803Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class AmbientPressureError_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressureError
        self._category = categories.none
        self._id = 178
        self._size = 2
        self._sensor_index = 0
        self._error = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._error)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_error(self):
        return MS5803Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class AmbientPressureCoefficient_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressureCoefficient
        self._category = categories.none
        self._id = 179
        self._size = 4
        self._sensor_index = 0
        self._coefficient_index = 0
        self._coefficient_value = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_coefficient_index(self, value):
        self._coefficient_index = value
    def set_coefficient_value(self, value):
        self._coefficient_value = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._coefficient_index)
        buf += struct.pack("<H", self._coefficient_value)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_coefficient_index(self):
        return self._coefficient_index
    def get_coefficient_value(self):
        return self._coefficient_value
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.coefficient_index, self.get_coefficient_index()))
        data.append((fields.coefficient_value, self.get_coefficient_value()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._coefficient_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._coefficient_value = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class AmbientPressureCoefficient_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientPressureCoefficient
        self._category = categories.none
        self._id = 180
        self._size = 4
        self._sensor_index = 0
        self._coefficient_index = 0
        self._coefficient_value = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_coefficient_index(self, value):
        self._coefficient_index = value
    def set_coefficient_value(self, value):
        self._coefficient_value = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._coefficient_index)
        buf += struct.pack("<H", self._coefficient_value)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_coefficient_index(self):
        return self._coefficient_index
    def get_coefficient_value(self):
        return self._coefficient_value
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.coefficient_index, self.get_coefficient_index()))
        data.append((fields.coefficient_value, self.get_coefficient_value()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._coefficient_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._coefficient_value = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class ColdSideTemperature_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.ColdSideTemperature
        self._category = categories.none
        self._id = 181
        self._size = 6
        self._sensor_type = 0
        self._sensor_index = 0
        self._temperature_celsius = 0
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
    def set_sensor_type(self, value):
        self._sensor_type = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -55, 125, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_type)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_sensor_type(self):
        return ColdSideTemperatureSensorType(self._sensor_type)
    def get_sensor_index(self):
        return self._sensor_index
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -55, 125, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_type, self.get_sensor_type()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class ColdSideTemperature_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.ColdSideTemperature
        self._category = categories.none
        self._id = 182
        self._size = 6
        self._sensor_type = 0
        self._sensor_index = 0
        self._temperature_celsius = 0
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
    def set_sensor_type(self, value):
        self._sensor_type = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -55, 125, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_type)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_sensor_type(self):
        return ColdSideTemperatureSensorType(self._sensor_type)
    def get_sensor_index(self):
        return self._sensor_index
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -55, 125, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_type, self.get_sensor_type()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class ColdSideTemperature_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.ColdSideTemperature
        self._category = categories.none
        self._id = 183
        self._size = 6
        self._sensor_type = 0
        self._sensor_index = 0
        self._temperature_celsius = 0
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
    def set_sensor_type(self, value):
        self._sensor_type = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -55, 125, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_type)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_sensor_type(self):
        return ColdSideTemperatureSensorType(self._sensor_type)
    def get_sensor_index(self):
        return self._sensor_index
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -55, 125, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_type, self.get_sensor_type()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class ColdSideTemperature_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.ColdSideTemperature
        self._category = categories.none
        self._id = 184
        self._size = 6
        self._sensor_type = 0
        self._sensor_index = 0
        self._temperature_celsius = 0
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
    def set_sensor_type(self, value):
        self._sensor_type = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -55, 125, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_type)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_sensor_type(self):
        return ColdSideTemperatureSensorType(self._sensor_type)
    def get_sensor_index(self):
        return self._sensor_index
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -55, 125, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_type, self.get_sensor_type()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class ColdSideTemperature_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.ColdSideTemperature
        self._category = categories.none
        self._id = 185
        self._size = 6
        self._sensor_type = 0
        self._sensor_index = 0
        self._temperature_celsius = 0
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
    def set_sensor_type(self, value):
        self._sensor_type = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -55, 125, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_type)
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_sensor_type(self):
        return ColdSideTemperatureSensorType(self._sensor_type)
    def get_sensor_index(self):
        return self._sensor_index
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -55, 125, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_type, self.get_sensor_type()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class PlatinumSensorTemperature_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PlatinumSensorTemperature
        self._category = categories.none
        self._id = 186
        self._size = 5
        self._sensor_index = 0
        self._temperature_celsius = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -200, 850, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -200, 850, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class PlatinumSensorResistance_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PlatinumSensorResistance
        self._category = categories.none
        self._id = 187
        self._size = 5
        self._sensor_index = 0
        self._resistance_ohms = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_resistance_ohms(self, value):
        self._resistance_ohms = packedFloat_to_uint(value, 0, 5000, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._resistance_ohms)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_resistance_ohms(self):
        return uint_to_packedFloat(self._resistance_ohms, 0, 5000, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.resistance_ohms, self.get_resistance_ohms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._resistance_ohms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class PlatinumSensorRatio_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PlatinumSensorRatio
        self._category = categories.none
        self._id = 188
        self._size = 5
        self._sensor_index = 0
        self._ratio_fraction = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_ratio_fraction(self, value):
        self._ratio_fraction = packedFloat_to_uint(value, 0, 1, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._ratio_fraction)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_ratio_fraction(self):
        return uint_to_packedFloat(self._ratio_fraction, 0, 1, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.ratio_fraction, self.get_ratio_fraction()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._ratio_fraction = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class ThermocoupleTypeKTemperature_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.ThermocoupleTypeKTemperature
        self._category = categories.none
        self._id = 189
        self._size = 5
        self._sensor_index = 0
        self._temperature_celsius = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -200, 1350, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -200, 1350, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class ThermocoupleTypeKTemperature_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.ThermocoupleTypeKTemperature
        self._category = categories.none
        self._id = 190
        self._size = 5
        self._sensor_index = 0
        self._temperature_celsius = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -200, 1350, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<L", self._temperature_celsius)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -200, 1350, 4)
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class Humidity_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.Humidity
        self._category = categories.none
        self._id = 192
        self._size = 3
        self._relative_humidity = 0
        self._is_heater_on = 0
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
    def set_relative_humidity(self, value):
        self._relative_humidity = packedFloat_to_uint(value, 0, 100, 2)
    def set_is_heater_on(self, value):
        self._is_heater_on = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._relative_humidity)
        buf += struct.pack("<B", self._is_heater_on)
        return buf
    def get_relative_humidity(self):
        return uint_to_packedFloat(self._relative_humidity, 0, 100, 2)
    def get_is_heater_on(self):
        return self._is_heater_on
    def get_all_data(self):
        data = []
        data.append((fields.relative_humidity, self.get_relative_humidity()))
        data.append((fields.is_heater_on, self.get_is_heater_on()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._relative_humidity = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._is_heater_on = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class HumidityError_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.HumidityError
        self._category = categories.none
        self._id = 193
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return SHT31Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class Acceleration_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.Acceleration
        self._category = categories.none
        self._id = 194
        self._size = 8
        self._acceleration_x_gforce = 0
        self._acceleration_y_gforce = 0
        self._acceleration_z_gforce = 0
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
    def set_acceleration_x_gforce(self, value):
        self._acceleration_x_gforce = packedFloat_to_uint(value, -20, 20, 2)
    def set_acceleration_y_gforce(self, value):
        self._acceleration_y_gforce = packedFloat_to_uint(value, -20, 20, 2)
    def set_acceleration_z_gforce(self, value):
        self._acceleration_z_gforce = packedFloat_to_uint(value, -20, 20, 4)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._acceleration_x_gforce)
        buf += struct.pack("<H", self._acceleration_y_gforce)
        buf += struct.pack("<L", self._acceleration_z_gforce)
        return buf
    def get_acceleration_x_gforce(self):
        return uint_to_packedFloat(self._acceleration_x_gforce, -20, 20, 2)
    def get_acceleration_y_gforce(self):
        return uint_to_packedFloat(self._acceleration_y_gforce, -20, 20, 2)
    def get_acceleration_z_gforce(self):
        return uint_to_packedFloat(self._acceleration_z_gforce, -20, 20, 4)
    def get_all_data(self):
        data = []
        data.append((fields.acceleration_x_gforce, self.get_acceleration_x_gforce()))
        data.append((fields.acceleration_y_gforce, self.get_acceleration_y_gforce()))
        data.append((fields.acceleration_z_gforce, self.get_acceleration_z_gforce()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._acceleration_x_gforce = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._acceleration_y_gforce = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._acceleration_z_gforce = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class AccelerationSelfTest_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.AccelerationSelfTest
        self._category = categories.none
        self._id = 195
        self._size = 8
        self._sign = 0
        self._result = 0
        self._acceleration_x_gforce = 0
        self._acceleration_y_gforce = 0
        self._acceleration_z_gforce = 0
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
    def set_sign(self, value):
        self._sign = value.value
    def set_result(self, value):
        self._result = value.value
    def set_acceleration_x_gforce(self, value):
        self._acceleration_x_gforce = packedFloat_to_uint(value, -20, 20, 2)
    def set_acceleration_y_gforce(self, value):
        self._acceleration_y_gforce = packedFloat_to_uint(value, -20, 20, 2)
    def set_acceleration_z_gforce(self, value):
        self._acceleration_z_gforce = packedFloat_to_uint(value, -20, 20, 2)
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sign)
        buf += struct.pack("<B", self._result)
        buf += struct.pack("<H", self._acceleration_x_gforce)
        buf += struct.pack("<H", self._acceleration_y_gforce)
        buf += struct.pack("<H", self._acceleration_z_gforce)
        return buf
    def get_sign(self):
        return AccelerationSelfTestDirection(self._sign)
    def get_result(self):
        return AccelerationSelfTestResult(self._result)
    def get_acceleration_x_gforce(self):
        return uint_to_packedFloat(self._acceleration_x_gforce, -20, 20, 2)
    def get_acceleration_y_gforce(self):
        return uint_to_packedFloat(self._acceleration_y_gforce, -20, 20, 2)
    def get_acceleration_z_gforce(self):
        return uint_to_packedFloat(self._acceleration_z_gforce, -20, 20, 2)
    def get_all_data(self):
        data = []
        data.append((fields.sign, self.get_sign()))
        data.append((fields.result, self.get_result()))
        data.append((fields.acceleration_x_gforce, self.get_acceleration_x_gforce()))
        data.append((fields.acceleration_y_gforce, self.get_acceleration_y_gforce()))
        data.append((fields.acceleration_z_gforce, self.get_acceleration_z_gforce()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sign = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._result = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._acceleration_x_gforce = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._acceleration_y_gforce = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._acceleration_z_gforce = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class AccelerationError_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.AccelerationError
        self._category = categories.none
        self._id = 196
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return LIS331Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class AmbientLight_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientLight
        self._category = categories.none
        self._id = 197
        self._size = 4
        self._ambientLight_lux = 0
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
    def set_ambientLight_lux(self, value):
        self._ambientLight_lux = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<f", self._ambientLight_lux)
        return buf
    def get_ambientLight_lux(self):
        return self._ambientLight_lux
    def get_all_data(self):
        data = []
        data.append((fields.ambientLight_lux, self.get_ambientLight_lux()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._ambientLight_lux = struct.unpack_from("<f", buf, index)[0]
        index += 4
        return
class AmbientLightError_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.AmbientLightError
        self._category = categories.none
        self._id = 198
        self._size = 1
        self._error = 0
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
    def set_error(self, value):
        self._error = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        return buf
    def get_error(self):
        return LTR303Error(self._error)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class OneWireSearchFamilyMismatch_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireSearchFamilyMismatch
        self._category = categories.none
        self._id = 206
        self._size = 8
        self._bus = 0
        self._serial_byte0 = 0
        self._serial_byte1 = 0
        self._serial_byte2 = 0
        self._serial_byte3 = 0
        self._serial_byte4 = 0
        self._serial_byte5 = 0
        self._found_family_code = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_serial_byte0(self, value):
        self._serial_byte0 = value
    def set_serial_byte1(self, value):
        self._serial_byte1 = value
    def set_serial_byte2(self, value):
        self._serial_byte2 = value
    def set_serial_byte3(self, value):
        self._serial_byte3 = value
    def set_serial_byte4(self, value):
        self._serial_byte4 = value
    def set_serial_byte5(self, value):
        self._serial_byte5 = value
    def set_found_family_code(self, value):
        self._found_family_code = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._serial_byte0)
        buf += struct.pack("<B", self._serial_byte1)
        buf += struct.pack("<B", self._serial_byte2)
        buf += struct.pack("<B", self._serial_byte3)
        buf += struct.pack("<B", self._serial_byte4)
        buf += struct.pack("<B", self._serial_byte5)
        buf += struct.pack("<B", self._found_family_code)
        return buf
    def get_bus(self):
        return OneWireBus(self._bus)
    def get_serial_byte0(self):
        return self._serial_byte0
    def get_serial_byte1(self):
        return self._serial_byte1
    def get_serial_byte2(self):
        return self._serial_byte2
    def get_serial_byte3(self):
        return self._serial_byte3
    def get_serial_byte4(self):
        return self._serial_byte4
    def get_serial_byte5(self):
        return self._serial_byte5
    def get_found_family_code(self):
        return self._found_family_code
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.serial_byte0, self.get_serial_byte0()))
        data.append((fields.serial_byte1, self.get_serial_byte1()))
        data.append((fields.serial_byte2, self.get_serial_byte2()))
        data.append((fields.serial_byte3, self.get_serial_byte3()))
        data.append((fields.serial_byte4, self.get_serial_byte4()))
        data.append((fields.serial_byte5, self.get_serial_byte5()))
        data.append((fields.found_family_code, self.get_found_family_code()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._found_family_code = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class OneWireSearchCRCMismatch_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireSearchCRCMismatch
        self._category = categories.none
        self._id = 207
        self._size = 8
        self._bus = 0
        self._serial_byte0 = 0
        self._serial_byte1 = 0
        self._serial_byte2 = 0
        self._serial_byte3 = 0
        self._serial_byte4 = 0
        self._serial_byte5 = 0
        self._found_crc = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_serial_byte0(self, value):
        self._serial_byte0 = value
    def set_serial_byte1(self, value):
        self._serial_byte1 = value
    def set_serial_byte2(self, value):
        self._serial_byte2 = value
    def set_serial_byte3(self, value):
        self._serial_byte3 = value
    def set_serial_byte4(self, value):
        self._serial_byte4 = value
    def set_serial_byte5(self, value):
        self._serial_byte5 = value
    def set_found_crc(self, value):
        self._found_crc = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._serial_byte0)
        buf += struct.pack("<B", self._serial_byte1)
        buf += struct.pack("<B", self._serial_byte2)
        buf += struct.pack("<B", self._serial_byte3)
        buf += struct.pack("<B", self._serial_byte4)
        buf += struct.pack("<B", self._serial_byte5)
        buf += struct.pack("<B", self._found_crc)
        return buf
    def get_bus(self):
        return OneWireBus(self._bus)
    def get_serial_byte0(self):
        return self._serial_byte0
    def get_serial_byte1(self):
        return self._serial_byte1
    def get_serial_byte2(self):
        return self._serial_byte2
    def get_serial_byte3(self):
        return self._serial_byte3
    def get_serial_byte4(self):
        return self._serial_byte4
    def get_serial_byte5(self):
        return self._serial_byte5
    def get_found_crc(self):
        return self._found_crc
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.serial_byte0, self.get_serial_byte0()))
        data.append((fields.serial_byte1, self.get_serial_byte1()))
        data.append((fields.serial_byte2, self.get_serial_byte2()))
        data.append((fields.serial_byte3, self.get_serial_byte3()))
        data.append((fields.serial_byte4, self.get_serial_byte4()))
        data.append((fields.serial_byte5, self.get_serial_byte5()))
        data.append((fields.found_crc, self.get_found_crc()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._found_crc = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class OneWireSearchFoundDevice_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireSearchFoundDevice
        self._category = categories.none
        self._id = 208
        self._size = 7
        self._bus = 0
        self._serial_byte0 = 0
        self._serial_byte1 = 0
        self._serial_byte2 = 0
        self._serial_byte3 = 0
        self._serial_byte4 = 0
        self._serial_byte5 = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_serial_byte0(self, value):
        self._serial_byte0 = value
    def set_serial_byte1(self, value):
        self._serial_byte1 = value
    def set_serial_byte2(self, value):
        self._serial_byte2 = value
    def set_serial_byte3(self, value):
        self._serial_byte3 = value
    def set_serial_byte4(self, value):
        self._serial_byte4 = value
    def set_serial_byte5(self, value):
        self._serial_byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._serial_byte0)
        buf += struct.pack("<B", self._serial_byte1)
        buf += struct.pack("<B", self._serial_byte2)
        buf += struct.pack("<B", self._serial_byte3)
        buf += struct.pack("<B", self._serial_byte4)
        buf += struct.pack("<B", self._serial_byte5)
        return buf
    def get_bus(self):
        return OneWireBus(self._bus)
    def get_serial_byte0(self):
        return self._serial_byte0
    def get_serial_byte1(self):
        return self._serial_byte1
    def get_serial_byte2(self):
        return self._serial_byte2
    def get_serial_byte3(self):
        return self._serial_byte3
    def get_serial_byte4(self):
        return self._serial_byte4
    def get_serial_byte5(self):
        return self._serial_byte5
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.serial_byte0, self.get_serial_byte0()))
        data.append((fields.serial_byte1, self.get_serial_byte1()))
        data.append((fields.serial_byte2, self.get_serial_byte2()))
        data.append((fields.serial_byte3, self.get_serial_byte3()))
        data.append((fields.serial_byte4, self.get_serial_byte4()))
        data.append((fields.serial_byte5, self.get_serial_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_SetDebugMode_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_SetDebugMode
        self._category = categories.none
        self._id = 209
        self._size = 2
        self._debug_mode = 0
        self._powercan_channel = 0
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
    def set_debug_mode(self, value):
        self._debug_mode = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debug_mode)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_debug_mode(self):
        return PowerCAN_DebugMode(self._debug_mode)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.debug_mode, self.get_debug_mode()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debug_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_GetState_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_GetState
        self._category = categories.none
        self._id = 210
        self._size = 1
        self._powercan_channel = 0
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
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_TransitionRequest_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_TransitionRequest
        self._category = categories.none
        self._id = 211
        self._size = 4
        self._edda_signature = 0
        self._request = 0
        self._powercan_channel = 0
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
    def set_edda_signature(self, value):
        self._edda_signature = value
    def set_request(self, value):
        self._request = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._edda_signature)
        buf += struct.pack("<B", self._request)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_edda_signature(self):
        return self._edda_signature
    def get_request(self):
        return PowerCAN_TransitionRequest(self._request)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.edda_signature, self.get_edda_signature()))
        data.append((fields.request, self.get_request()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._edda_signature = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._request = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_Hello_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_Hello
        self._category = categories.none
        self._id = 212
        self._size = 2
        self._debug_mode = 0
        self._powercan_channel = 0
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
    def set_debug_mode(self, value):
        self._debug_mode = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._debug_mode)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_debug_mode(self):
        return PowerCAN_DebugMode(self._debug_mode)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.debug_mode, self.get_debug_mode()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._debug_mode = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_CurrentState_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_CurrentState
        self._category = categories.none
        self._id = 213
        self._size = 3
        self._system_state = 0
        self._gate_state = 0
        self._powercan_channel = 0
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
    def set_system_state(self, value):
        self._system_state = value.value
    def set_gate_state(self, value):
        self._gate_state = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._system_state)
        buf += struct.pack("<B", self._gate_state)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_system_state(self):
        return PowerCAN_SystemState(self._system_state)
    def get_gate_state(self):
        return PowerCAN_GateState(self._gate_state)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.system_state, self.get_system_state()))
        data.append((fields.gate_state, self.get_gate_state()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._system_state = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._gate_state = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_Temperature_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_Temperature
        self._category = categories.none
        self._id = 214
        self._size = 6
        self._kind = 0
        self._temperature_celsius = 0
        self._powercan_channel = 0
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
    def set_kind(self, value):
        self._kind = value.value
    def set_temperature_celsius(self, value):
        self._temperature_celsius = packedFloat_to_uint(value, -100, 300, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._kind)
        buf += struct.pack("<L", self._temperature_celsius)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_kind(self):
        return PowerCAN_TemperatureKind(self._kind)
    def get_temperature_celsius(self):
        return uint_to_packedFloat(self._temperature_celsius, -100, 300, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.kind, self.get_kind()))
        data.append((fields.temperature_celsius, self.get_temperature_celsius()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._kind = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._temperature_celsius = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_Voltage_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_Voltage
        self._category = categories.none
        self._id = 215
        self._size = 6
        self._kind = 0
        self._voltage_volts = 0
        self._powercan_channel = 0
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
    def set_kind(self, value):
        self._kind = value.value
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, -30, 30, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._kind)
        buf += struct.pack("<L", self._voltage_volts)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_kind(self):
        return PowerCAN_VoltageKind(self._kind)
    def get_voltage_volts(self):
        return uint_to_packedFloat(self._voltage_volts, -30, 30, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.kind, self.get_kind()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._kind = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._voltage_volts = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ChannelMeasurementPower_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ChannelMeasurementPower
        self._category = categories.none
        self._id = 216
        self._size = 6
        self._channel = 0
        self._power_watts = 0
        self._powercan_channel = 0
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
    def set_channel(self, value):
        self._channel = value.value
    def set_power_watts(self, value):
        self._power_watts = packedFloat_to_uint(value, 0, 1000, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._channel)
        buf += struct.pack("<L", self._power_watts)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_channel(self):
        return PowerCAN_MeasurementChannel(self._channel)
    def get_power_watts(self):
        return uint_to_packedFloat(self._power_watts, 0, 1000, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.channel, self.get_channel()))
        data.append((fields.power_watts, self.get_power_watts()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._power_watts = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ChannelMeasurementVoltage_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ChannelMeasurementVoltage
        self._category = categories.none
        self._id = 217
        self._size = 6
        self._channel = 0
        self._voltage_volts = 0
        self._powercan_channel = 0
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
    def set_channel(self, value):
        self._channel = value.value
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, -30, 30, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._channel)
        buf += struct.pack("<L", self._voltage_volts)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_channel(self):
        return PowerCAN_MeasurementChannel(self._channel)
    def get_voltage_volts(self):
        return uint_to_packedFloat(self._voltage_volts, -30, 30, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.channel, self.get_channel()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._voltage_volts = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ChannelMeasurementCurrent_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ChannelMeasurementCurrent
        self._category = categories.none
        self._id = 218
        self._size = 6
        self._channel = 0
        self._current_amperes = 0
        self._powercan_channel = 0
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
    def set_channel(self, value):
        self._channel = value.value
    def set_current_amperes(self, value):
        self._current_amperes = packedFloat_to_uint(value, 0, 30, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._channel)
        buf += struct.pack("<L", self._current_amperes)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_channel(self):
        return PowerCAN_MeasurementChannel(self._channel)
    def get_current_amperes(self):
        return uint_to_packedFloat(self._current_amperes, 0, 30, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.channel, self.get_channel()))
        data.append((fields.current_amperes, self.get_current_amperes()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._current_amperes = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_LoadMeasurementResistance_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_LoadMeasurementResistance
        self._category = categories.none
        self._id = 219
        self._size = 7
        self._measurement_reference = 0
        self._result = 0
        self._resistance_ohms = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_result(self, value):
        self._result = value.value
    def set_resistance_ohms(self, value):
        self._resistance_ohms = packedFloat_to_uint(value, 0, 100000, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._result)
        buf += struct.pack("<L", self._resistance_ohms)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_MeasurementReference(self._measurement_reference)
    def get_result(self):
        return PowerCAN_LoadMeasurementResult(self._result)
    def get_resistance_ohms(self):
        return uint_to_packedFloat(self._resistance_ohms, 0, 100000, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.result, self.get_result()))
        data.append((fields.resistance_ohms, self.get_resistance_ohms()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._result = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._resistance_ohms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_LoadMeasurementVoltage_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_LoadMeasurementVoltage
        self._category = categories.none
        self._id = 220
        self._size = 7
        self._measurement_reference = 0
        self._result = 0
        self._voltage_volts = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_result(self, value):
        self._result = value.value
    def set_voltage_volts(self, value):
        self._voltage_volts = packedFloat_to_uint(value, -30, 30, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._result)
        buf += struct.pack("<L", self._voltage_volts)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_MeasurementReference(self._measurement_reference)
    def get_result(self):
        return PowerCAN_LoadMeasurementResult(self._result)
    def get_voltage_volts(self):
        return uint_to_packedFloat(self._voltage_volts, -30, 30, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.result, self.get_result()))
        data.append((fields.voltage_volts, self.get_voltage_volts()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._result = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._voltage_volts = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_LoadMeasurementPower_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_LoadMeasurementPower
        self._category = categories.none
        self._id = 221
        self._size = 7
        self._measurement_reference = 0
        self._result = 0
        self._power_watts = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_result(self, value):
        self._result = value.value
    def set_power_watts(self, value):
        self._power_watts = packedFloat_to_uint(value, 0, 1000, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._result)
        buf += struct.pack("<L", self._power_watts)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_MeasurementReference(self._measurement_reference)
    def get_result(self):
        return PowerCAN_LoadMeasurementResult(self._result)
    def get_power_watts(self):
        return uint_to_packedFloat(self._power_watts, 0, 1000, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.result, self.get_result()))
        data.append((fields.power_watts, self.get_power_watts()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._result = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._power_watts = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_LoadMeasurementCurrent_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_LoadMeasurementCurrent
        self._category = categories.none
        self._id = 222
        self._size = 7
        self._measurement_reference = 0
        self._result = 0
        self._current_amperes = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_result(self, value):
        self._result = value.value
    def set_current_amperes(self, value):
        self._current_amperes = packedFloat_to_uint(value, 0, 30, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._result)
        buf += struct.pack("<L", self._current_amperes)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_MeasurementReference(self._measurement_reference)
    def get_result(self):
        return PowerCAN_LoadMeasurementResult(self._result)
    def get_current_amperes(self):
        return uint_to_packedFloat(self._current_amperes, 0, 30, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.result, self.get_result()))
        data.append((fields.current_amperes, self.get_current_amperes()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._result = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._current_amperes = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_FailedLoadMeasurementValue_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_FailedLoadMeasurementValue
        self._category = categories.none
        self._id = 223
        self._size = 7
        self._measurement_reference = 0
        self._failure_reason = 0
        self._value = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_failure_reason(self, value):
        self._failure_reason = value.value
    def set_value(self, value):
        self._value = packedFloat_to_uint(value, 0, 1000000, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._failure_reason)
        buf += struct.pack("<L", self._value)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_MeasurementReference(self._measurement_reference)
    def get_failure_reason(self):
        return PowerCAN_MeasurementFailureReason(self._failure_reason)
    def get_value(self):
        return uint_to_packedFloat(self._value, 0, 1000000, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.failure_reason, self.get_failure_reason()))
        data.append((fields.value, self.get_value()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._failure_reason = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._value = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_FailedLoadMeasurementThreshold_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_FailedLoadMeasurementThreshold
        self._category = categories.none
        self._id = 224
        self._size = 7
        self._measurement_reference = 0
        self._failure_reason = 0
        self._threshold = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_failure_reason(self, value):
        self._failure_reason = value.value
    def set_threshold(self, value):
        self._threshold = packedFloat_to_uint(value, 0, 1000000, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._failure_reason)
        buf += struct.pack("<L", self._threshold)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_MeasurementReference(self._measurement_reference)
    def get_failure_reason(self):
        return PowerCAN_MeasurementFailureReason(self._failure_reason)
    def get_threshold(self):
        return uint_to_packedFloat(self._threshold, 0, 1000000, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.failure_reason, self.get_failure_reason()))
        data.append((fields.threshold, self.get_threshold()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._failure_reason = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._threshold = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ResistanceMeasurementResistance_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ResistanceMeasurementResistance
        self._category = categories.none
        self._id = 225
        self._size = 7
        self._measurement_reference = 0
        self._validity = 0
        self._resistance_ohms = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_validity(self, value):
        self._validity = value.value
    def set_resistance_ohms(self, value):
        self._resistance_ohms = packedFloat_to_uint(value, 0, 100000, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._validity)
        buf += struct.pack("<L", self._resistance_ohms)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_ResistanceMeasurementReference(self._measurement_reference)
    def get_validity(self):
        return PowerCAN_ResistanceMeasurementValidity(self._validity)
    def get_resistance_ohms(self):
        return uint_to_packedFloat(self._resistance_ohms, 0, 100000, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.validity, self.get_validity()))
        data.append((fields.resistance_ohms, self.get_resistance_ohms()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._validity = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._resistance_ohms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ResistanceMeasurementReferenceVoltage_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ResistanceMeasurementReferenceVoltage
        self._category = categories.none
        self._id = 226
        self._size = 7
        self._measurement_reference = 0
        self._validity = 0
        self._reference_voltage_volts = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_validity(self, value):
        self._validity = value.value
    def set_reference_voltage_volts(self, value):
        self._reference_voltage_volts = packedFloat_to_uint(value, 0, 5, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._validity)
        buf += struct.pack("<L", self._reference_voltage_volts)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_ResistanceMeasurementReference(self._measurement_reference)
    def get_validity(self):
        return PowerCAN_ResistanceMeasurementValidity(self._validity)
    def get_reference_voltage_volts(self):
        return uint_to_packedFloat(self._reference_voltage_volts, 0, 5, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.validity, self.get_validity()))
        data.append((fields.reference_voltage_volts, self.get_reference_voltage_volts()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._validity = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._reference_voltage_volts = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ResistanceMeasurementDifferentialVoltage_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ResistanceMeasurementDifferentialVoltage
        self._category = categories.none
        self._id = 227
        self._size = 7
        self._measurement_reference = 0
        self._validity = 0
        self._differential_voltage_volts = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_validity(self, value):
        self._validity = value.value
    def set_differential_voltage_volts(self, value):
        self._differential_voltage_volts = packedFloat_to_uint(value, 0, 5, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._validity)
        buf += struct.pack("<L", self._differential_voltage_volts)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_ResistanceMeasurementReference(self._measurement_reference)
    def get_validity(self):
        return PowerCAN_ResistanceMeasurementValidity(self._validity)
    def get_differential_voltage_volts(self):
        return uint_to_packedFloat(self._differential_voltage_volts, 0, 5, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.validity, self.get_validity()))
        data.append((fields.differential_voltage_volts, self.get_differential_voltage_volts()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._validity = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._differential_voltage_volts = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ResistanceMeasurementPositiveVoltage_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ResistanceMeasurementPositiveVoltage
        self._category = categories.none
        self._id = 228
        self._size = 7
        self._measurement_reference = 0
        self._validity = 0
        self._positive_voltage_volts = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_validity(self, value):
        self._validity = value.value
    def set_positive_voltage_volts(self, value):
        self._positive_voltage_volts = packedFloat_to_uint(value, 0, 5, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._validity)
        buf += struct.pack("<L", self._positive_voltage_volts)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_ResistanceMeasurementReference(self._measurement_reference)
    def get_validity(self):
        return PowerCAN_ResistanceMeasurementValidity(self._validity)
    def get_positive_voltage_volts(self):
        return uint_to_packedFloat(self._positive_voltage_volts, 0, 5, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.validity, self.get_validity()))
        data.append((fields.positive_voltage_volts, self.get_positive_voltage_volts()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._validity = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._positive_voltage_volts = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ResistanceMeasurementNegativeVoltage_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ResistanceMeasurementNegativeVoltage
        self._category = categories.none
        self._id = 229
        self._size = 7
        self._measurement_reference = 0
        self._validity = 0
        self._negative_voltage_volts = 0
        self._powercan_channel = 0
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
    def set_measurement_reference(self, value):
        self._measurement_reference = value.value
    def set_validity(self, value):
        self._validity = value.value
    def set_negative_voltage_volts(self, value):
        self._negative_voltage_volts = packedFloat_to_uint(value, 0, 5, 4)
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._measurement_reference)
        buf += struct.pack("<B", self._validity)
        buf += struct.pack("<L", self._negative_voltage_volts)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_measurement_reference(self):
        return PowerCAN_ResistanceMeasurementReference(self._measurement_reference)
    def get_validity(self):
        return PowerCAN_ResistanceMeasurementValidity(self._validity)
    def get_negative_voltage_volts(self):
        return uint_to_packedFloat(self._negative_voltage_volts, 0, 5, 4)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.measurement_reference, self.get_measurement_reference()))
        data.append((fields.validity, self.get_validity()))
        data.append((fields.negative_voltage_volts, self.get_negative_voltage_volts()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._measurement_reference = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._validity = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._negative_voltage_volts = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_LTC2992Error_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_LTC2992Error
        self._category = categories.none
        self._id = 230
        self._size = 7
        self._error = 0
        self._location = 0
        self._register_address = 0
        self._read_data = 0
        self._write_data = 0
        self._expected_data = 0
        self._powercan_channel = 0
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
    def set_error(self, value):
        self._error = value.value
    def set_location(self, value):
        self._location = value.value
    def set_register_address(self, value):
        self._register_address = value
    def set_read_data(self, value):
        self._read_data = value
    def set_write_data(self, value):
        self._write_data = value
    def set_expected_data(self, value):
        self._expected_data = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._location)
        buf += struct.pack("<B", self._register_address)
        buf += struct.pack("<B", self._read_data)
        buf += struct.pack("<B", self._write_data)
        buf += struct.pack("<B", self._expected_data)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_error(self):
        return PowerCAN_LTC2992Error(self._error)
    def get_location(self):
        return PowerCAN_LTC2992ErrorLocation(self._location)
    def get_register_address(self):
        return self._register_address
    def get_read_data(self):
        return self._read_data
    def get_write_data(self):
        return self._write_data
    def get_expected_data(self):
        return self._expected_data
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        data.append((fields.location, self.get_location()))
        data.append((fields.register_address, self.get_register_address()))
        data.append((fields.read_data, self.get_read_data()))
        data.append((fields.write_data, self.get_write_data()))
        data.append((fields.expected_data, self.get_expected_data()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._location = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._register_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._read_data = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._write_data = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._expected_data = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ADS122C04Error_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ADS122C04Error
        self._category = categories.none
        self._id = 231
        self._size = 7
        self._error = 0
        self._location = 0
        self._register_address = 0
        self._read_data = 0
        self._write_data = 0
        self._expected_data = 0
        self._powercan_channel = 0
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
    def set_error(self, value):
        self._error = value.value
    def set_location(self, value):
        self._location = value.value
    def set_register_address(self, value):
        self._register_address = value
    def set_read_data(self, value):
        self._read_data = value
    def set_write_data(self, value):
        self._write_data = value
    def set_expected_data(self, value):
        self._expected_data = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._location)
        buf += struct.pack("<B", self._register_address)
        buf += struct.pack("<B", self._read_data)
        buf += struct.pack("<B", self._write_data)
        buf += struct.pack("<B", self._expected_data)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_error(self):
        return PowerCAN_ADS122C04Error(self._error)
    def get_location(self):
        return PowerCAN_ADS122C04ErrorLocation(self._location)
    def get_register_address(self):
        return self._register_address
    def get_read_data(self):
        return self._read_data
    def get_write_data(self):
        return self._write_data
    def get_expected_data(self):
        return self._expected_data
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        data.append((fields.location, self.get_location()))
        data.append((fields.register_address, self.get_register_address()))
        data.append((fields.read_data, self.get_read_data()))
        data.append((fields.write_data, self.get_write_data()))
        data.append((fields.expected_data, self.get_expected_data()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._location = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._register_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._read_data = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._write_data = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._expected_data = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_CheckResult_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_CheckResult
        self._category = categories.none
        self._id = 232
        self._size = 5
        self._result = 0
        self._checks_failed = 0
        self._checks_performed = 0
        self._total_checks = 0
        self._powercan_channel = 0
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
    def set_result(self, value):
        self._result = value.value
    def set_checks_failed(self, value):
        self._checks_failed = value
    def set_checks_performed(self, value):
        self._checks_performed = value
    def set_total_checks(self, value):
        self._total_checks = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._result)
        buf += struct.pack("<B", self._checks_failed)
        buf += struct.pack("<B", self._checks_performed)
        buf += struct.pack("<B", self._total_checks)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_result(self):
        return PowerCAN_CheckResult(self._result)
    def get_checks_failed(self):
        return self._checks_failed
    def get_checks_performed(self):
        return self._checks_performed
    def get_total_checks(self):
        return self._total_checks
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.result, self.get_result()))
        data.append((fields.checks_failed, self.get_checks_failed()))
        data.append((fields.checks_performed, self.get_checks_performed()))
        data.append((fields.total_checks, self.get_total_checks()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._result = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._checks_failed = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._checks_performed = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._total_checks = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_TransitionResponse_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_TransitionResponse
        self._category = categories.none
        self._id = 233
        self._size = 3
        self._request = 0
        self._response = 0
        self._powercan_channel = 0
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
    def set_request(self, value):
        self._request = value.value
    def set_response(self, value):
        self._response = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._request)
        buf += struct.pack("<B", self._response)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_request(self):
        return PowerCAN_TransitionRequest(self._request)
    def get_response(self):
        return PowerCAN_TransitionResponse(self._response)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.request, self.get_request()))
        data.append((fields.response, self.get_response()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._request = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._response = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_I2CBusStarted_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_I2CBusStarted
        self._category = categories.none
        self._id = 234
        self._size = 6
        self._bus = 0
        self._frequency_hertz = 0
        self._powercan_channel = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_frequency_hertz(self, value):
        self._frequency_hertz = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<L", self._frequency_hertz)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_bus(self):
        return PowerCAN_I2CBus(self._bus)
    def get_frequency_hertz(self):
        return self._frequency_hertz
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.frequency_hertz, self.get_frequency_hertz()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._frequency_hertz = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_I2CSearchStarted_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_I2CSearchStarted
        self._category = categories.none
        self._id = 235
        self._size = 2
        self._bus = 0
        self._powercan_channel = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_bus(self):
        return PowerCAN_I2CBus(self._bus)
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_I2CSearchError_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_I2CSearchError
        self._category = categories.none
        self._id = 236
        self._size = 4
        self._bus = 0
        self._error = 0
        self._scanned_address = 0
        self._powercan_channel = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_error(self, value):
        self._error = value.value
    def set_scanned_address(self, value):
        self._scanned_address = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._scanned_address)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_bus(self):
        return PowerCAN_I2CBus(self._bus)
    def get_error(self):
        return PowerCAN_I2CError(self._error)
    def get_scanned_address(self):
        return self._scanned_address
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.error, self.get_error()))
        data.append((fields.scanned_address, self.get_scanned_address()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._scanned_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_I2CSearchFoundDevice_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_I2CSearchFoundDevice
        self._category = categories.none
        self._id = 237
        self._size = 3
        self._bus = 0
        self._found_device_address = 0
        self._powercan_channel = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_found_device_address(self, value):
        self._found_device_address = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._found_device_address)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_bus(self):
        return PowerCAN_I2CBus(self._bus)
    def get_found_device_address(self):
        return self._found_device_address
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.found_device_address, self.get_found_device_address()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._found_device_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_I2CSearchMissingDevice_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_I2CSearchMissingDevice
        self._category = categories.none
        self._id = 238
        self._size = 3
        self._bus = 0
        self._missing_device_address = 0
        self._powercan_channel = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_missing_device_address(self, value):
        self._missing_device_address = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._missing_device_address)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_bus(self):
        return PowerCAN_I2CBus(self._bus)
    def get_missing_device_address(self):
        return self._missing_device_address
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.missing_device_address, self.get_missing_device_address()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._missing_device_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_I2CSearchEnded_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_I2CSearchEnded
        self._category = categories.none
        self._id = 239
        self._size = 8
        self._bus = 0
        self._devices_successfully_found = 0
        self._addresses_with_error = 0
        self._search_time_us = 0
        self._powercan_channel = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_devices_successfully_found(self, value):
        self._devices_successfully_found = value
    def set_addresses_with_error(self, value):
        self._addresses_with_error = value
    def set_search_time_us(self, value):
        self._search_time_us = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._devices_successfully_found)
        buf += struct.pack("<B", self._addresses_with_error)
        buf += struct.pack("<L", self._search_time_us)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_bus(self):
        return PowerCAN_I2CBus(self._bus)
    def get_devices_successfully_found(self):
        return self._devices_successfully_found
    def get_addresses_with_error(self):
        return self._addresses_with_error
    def get_search_time_us(self):
        return self._search_time_us
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.devices_successfully_found, self.get_devices_successfully_found()))
        data.append((fields.addresses_with_error, self.get_addresses_with_error()))
        data.append((fields.search_time_us, self.get_search_time_us()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._devices_successfully_found = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._addresses_with_error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._search_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PowerCAN_ErrorStatistics_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PowerCAN_ErrorStatistics
        self._category = categories.none
        self._id = 240
        self._size = 5
        self._warning_count = 0
        self._error_count = 0
        self._powercan_channel = 0
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
    def set_warning_count(self, value):
        self._warning_count = value
    def set_error_count(self, value):
        self._error_count = value
    def set_powercan_channel(self, value):
        self._powercan_channel = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<H", self._warning_count)
        buf += struct.pack("<H", self._error_count)
        buf += struct.pack("<B", self._powercan_channel)
        return buf
    def get_warning_count(self):
        return self._warning_count
    def get_error_count(self):
        return self._error_count
    def get_powercan_channel(self):
        return PowerCANChannel(self._powercan_channel)
    def get_all_data(self):
        data = []
        data.append((fields.warning_count, self.get_warning_count()))
        data.append((fields.error_count, self.get_error_count()))
        data.append((fields.powercan_channel, self.get_powercan_channel()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._warning_count = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._error_count = struct.unpack_from("<H", buf, index)[0]
        index += 2
        self._powercan_channel = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class TaskInfo_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.TaskInfo
        self._category = categories.none
        self._id = 246
        self._size = 8
        self._type = 0
        self._thread_id = 0
        self._taskTime_microseconds = 0
        self._truncated_startTime_microseconds = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread_id(self, value):
        self._thread_id = value
    def set_taskTime_microseconds(self, value):
        self._taskTime_microseconds = value
    def set_truncated_startTime_microseconds(self, value):
        self._truncated_startTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._taskTime_microseconds)
        buf += struct.pack("<H", self._truncated_startTime_microseconds)
        return buf
    def get_type(self):
        return TaskType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_taskTime_microseconds(self):
        return self._taskTime_microseconds
    def get_truncated_startTime_microseconds(self):
        return self._truncated_startTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.taskTime_microseconds, self.get_taskTime_microseconds()))
        data.append((fields.truncated_startTime_microseconds, self.get_truncated_startTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._taskTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_startTime_microseconds = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class TaskInfo_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.TaskInfo
        self._category = categories.none
        self._id = 247
        self._size = 8
        self._type = 0
        self._thread_id = 0
        self._taskTime_microseconds = 0
        self._truncated_startTime_microseconds = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread_id(self, value):
        self._thread_id = value
    def set_taskTime_microseconds(self, value):
        self._taskTime_microseconds = value
    def set_truncated_startTime_microseconds(self, value):
        self._truncated_startTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._taskTime_microseconds)
        buf += struct.pack("<H", self._truncated_startTime_microseconds)
        return buf
    def get_type(self):
        return TaskType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_taskTime_microseconds(self):
        return self._taskTime_microseconds
    def get_truncated_startTime_microseconds(self):
        return self._truncated_startTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.taskTime_microseconds, self.get_taskTime_microseconds()))
        data.append((fields.truncated_startTime_microseconds, self.get_truncated_startTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._taskTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_startTime_microseconds = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class TaskInfo_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.TaskInfo
        self._category = categories.none
        self._id = 248
        self._size = 8
        self._type = 0
        self._thread_id = 0
        self._taskTime_microseconds = 0
        self._truncated_startTime_microseconds = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread_id(self, value):
        self._thread_id = value
    def set_taskTime_microseconds(self, value):
        self._taskTime_microseconds = value
    def set_truncated_startTime_microseconds(self, value):
        self._truncated_startTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._taskTime_microseconds)
        buf += struct.pack("<H", self._truncated_startTime_microseconds)
        return buf
    def get_type(self):
        return TaskType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_taskTime_microseconds(self):
        return self._taskTime_microseconds
    def get_truncated_startTime_microseconds(self):
        return self._truncated_startTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.taskTime_microseconds, self.get_taskTime_microseconds()))
        data.append((fields.truncated_startTime_microseconds, self.get_truncated_startTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._taskTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_startTime_microseconds = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class TaskInfo_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.TaskInfo
        self._category = categories.none
        self._id = 249
        self._size = 8
        self._type = 0
        self._thread_id = 0
        self._taskTime_microseconds = 0
        self._truncated_startTime_microseconds = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread_id(self, value):
        self._thread_id = value
    def set_taskTime_microseconds(self, value):
        self._taskTime_microseconds = value
    def set_truncated_startTime_microseconds(self, value):
        self._truncated_startTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._taskTime_microseconds)
        buf += struct.pack("<H", self._truncated_startTime_microseconds)
        return buf
    def get_type(self):
        return TaskType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_taskTime_microseconds(self):
        return self._taskTime_microseconds
    def get_truncated_startTime_microseconds(self):
        return self._truncated_startTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.taskTime_microseconds, self.get_taskTime_microseconds()))
        data.append((fields.truncated_startTime_microseconds, self.get_truncated_startTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._taskTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_startTime_microseconds = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class TaskInfo_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.TaskInfo
        self._category = categories.none
        self._id = 250
        self._size = 8
        self._type = 0
        self._thread_id = 0
        self._taskTime_microseconds = 0
        self._truncated_startTime_microseconds = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread_id(self, value):
        self._thread_id = value
    def set_taskTime_microseconds(self, value):
        self._taskTime_microseconds = value
    def set_truncated_startTime_microseconds(self, value):
        self._truncated_startTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._taskTime_microseconds)
        buf += struct.pack("<H", self._truncated_startTime_microseconds)
        return buf
    def get_type(self):
        return TaskType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_taskTime_microseconds(self):
        return self._taskTime_microseconds
    def get_truncated_startTime_microseconds(self):
        return self._truncated_startTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.taskTime_microseconds, self.get_taskTime_microseconds()))
        data.append((fields.truncated_startTime_microseconds, self.get_truncated_startTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._taskTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_startTime_microseconds = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class LoopInfo_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.LoopInfo
        self._category = categories.none
        self._id = 251
        self._size = 8
        self._type = 0
        self._thread_id = 0
        self._loopTime_microseconds = 0
        self._truncated_startTime_microseconds = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread_id(self, value):
        self._thread_id = value
    def set_loopTime_microseconds(self, value):
        self._loopTime_microseconds = value
    def set_truncated_startTime_microseconds(self, value):
        self._truncated_startTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._loopTime_microseconds)
        buf += struct.pack("<H", self._truncated_startTime_microseconds)
        return buf
    def get_type(self):
        return LoopType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_loopTime_microseconds(self):
        return self._loopTime_microseconds
    def get_truncated_startTime_microseconds(self):
        return self._truncated_startTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.loopTime_microseconds, self.get_loopTime_microseconds()))
        data.append((fields.truncated_startTime_microseconds, self.get_truncated_startTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._loopTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_startTime_microseconds = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class LoopInfo_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.LoopInfo
        self._category = categories.none
        self._id = 252
        self._size = 8
        self._type = 0
        self._thread_id = 0
        self._loopTime_microseconds = 0
        self._truncated_startTime_microseconds = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread_id(self, value):
        self._thread_id = value
    def set_loopTime_microseconds(self, value):
        self._loopTime_microseconds = value
    def set_truncated_startTime_microseconds(self, value):
        self._truncated_startTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._loopTime_microseconds)
        buf += struct.pack("<H", self._truncated_startTime_microseconds)
        return buf
    def get_type(self):
        return LoopType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_loopTime_microseconds(self):
        return self._loopTime_microseconds
    def get_truncated_startTime_microseconds(self):
        return self._truncated_startTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.loopTime_microseconds, self.get_loopTime_microseconds()))
        data.append((fields.truncated_startTime_microseconds, self.get_truncated_startTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._loopTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_startTime_microseconds = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class LoopInfo_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.LoopInfo
        self._category = categories.none
        self._id = 253
        self._size = 8
        self._type = 0
        self._thread_id = 0
        self._loopTime_microseconds = 0
        self._truncated_startTime_microseconds = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread_id(self, value):
        self._thread_id = value
    def set_loopTime_microseconds(self, value):
        self._loopTime_microseconds = value
    def set_truncated_startTime_microseconds(self, value):
        self._truncated_startTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._loopTime_microseconds)
        buf += struct.pack("<H", self._truncated_startTime_microseconds)
        return buf
    def get_type(self):
        return LoopType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_loopTime_microseconds(self):
        return self._loopTime_microseconds
    def get_truncated_startTime_microseconds(self):
        return self._truncated_startTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.loopTime_microseconds, self.get_loopTime_microseconds()))
        data.append((fields.truncated_startTime_microseconds, self.get_truncated_startTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._loopTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_startTime_microseconds = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class LoopInfo_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.LoopInfo
        self._category = categories.none
        self._id = 254
        self._size = 8
        self._type = 0
        self._thread_id = 0
        self._loopTime_microseconds = 0
        self._truncated_startTime_microseconds = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread_id(self, value):
        self._thread_id = value
    def set_loopTime_microseconds(self, value):
        self._loopTime_microseconds = value
    def set_truncated_startTime_microseconds(self, value):
        self._truncated_startTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._loopTime_microseconds)
        buf += struct.pack("<H", self._truncated_startTime_microseconds)
        return buf
    def get_type(self):
        return LoopType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_loopTime_microseconds(self):
        return self._loopTime_microseconds
    def get_truncated_startTime_microseconds(self):
        return self._truncated_startTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.loopTime_microseconds, self.get_loopTime_microseconds()))
        data.append((fields.truncated_startTime_microseconds, self.get_truncated_startTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._loopTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_startTime_microseconds = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class LoopInfo_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.LoopInfo
        self._category = categories.none
        self._id = 255
        self._size = 8
        self._type = 0
        self._thread_id = 0
        self._loopTime_microseconds = 0
        self._truncated_startTime_microseconds = 0
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
    def set_type(self, value):
        self._type = value.value
    def set_thread_id(self, value):
        self._thread_id = value
    def set_loopTime_microseconds(self, value):
        self._loopTime_microseconds = value
    def set_truncated_startTime_microseconds(self, value):
        self._truncated_startTime_microseconds = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._type)
        buf += struct.pack("<B", self._thread_id)
        buf += struct.pack("<L", self._loopTime_microseconds)
        buf += struct.pack("<H", self._truncated_startTime_microseconds)
        return buf
    def get_type(self):
        return LoopType(self._type)
    def get_thread_id(self):
        return self._thread_id
    def get_loopTime_microseconds(self):
        return self._loopTime_microseconds
    def get_truncated_startTime_microseconds(self):
        return self._truncated_startTime_microseconds
    def get_all_data(self):
        data = []
        data.append((fields.type, self.get_type()))
        data.append((fields.thread_id, self.get_thread_id()))
        data.append((fields.loopTime_microseconds, self.get_loopTime_microseconds()))
        data.append((fields.truncated_startTime_microseconds, self.get_truncated_startTime_microseconds()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._type = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._thread_id = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._loopTime_microseconds = struct.unpack_from("<L", buf, index)[0]
        index += 4
        self._truncated_startTime_microseconds = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class DS28E18QError_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.DS28E18QError
        self._category = categories.none
        self._id = 447
        self._size = 2
        self._error = 0
        self._sensor_index = 0
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
    def set_error(self, value):
        self._error = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._sensor_index)
        return buf
    def get_error(self):
        return DS28E18QError(self._error)
    def get_sensor_index(self):
        return self._sensor_index
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage1_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage1
        self._category = categories.none
        self._id = 455
        self._size = 1
        self._byte0 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage1_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage1
        self._category = categories.none
        self._id = 455
        self._size = 1
        self._byte0 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage1_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage1
        self._category = categories.none
        self._id = 456
        self._size = 1
        self._byte0 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage1_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage1
        self._category = categories.none
        self._id = 456
        self._size = 1
        self._byte0 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage1_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage1
        self._category = categories.none
        self._id = 457
        self._size = 1
        self._byte0 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage1_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage1
        self._category = categories.none
        self._id = 457
        self._size = 1
        self._byte0 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage1_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage1
        self._category = categories.none
        self._id = 458
        self._size = 1
        self._byte0 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage1_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage1
        self._category = categories.none
        self._id = 458
        self._size = 1
        self._byte0 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage1_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage1
        self._category = categories.none
        self._id = 459
        self._size = 1
        self._byte0 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage1_from_Edda_Simulator_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage1
        self._category = categories.none
        self._id = 459
        self._size = 1
        self._byte0 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class OneWireSearchStarted_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireSearchStarted
        self._category = categories.none
        self._id = 460
        self._size = 5
        self._bus = 0
        self._start_time_ms = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_start_time_ms(self, value):
        self._start_time_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<L", self._start_time_ms)
        return buf
    def get_bus(self):
        return OneWireBus(self._bus)
    def get_start_time_ms(self):
        return self._start_time_ms
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.start_time_ms, self.get_start_time_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._start_time_ms = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class TemperatureBoardBridgeError_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.TemperatureBoardBridgeError
        self._category = categories.none
        self._id = 461
        self._size = 5
        self._error = 0
        self._board_index = 0
        self._sensor_board_index = 0
        self._device_index = 0
        self._sensor_index = 0
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
    def set_error(self, value):
        self._error = value.value
    def set_board_index(self, value):
        self._board_index = value
    def set_sensor_board_index(self, value):
        self._sensor_board_index = value
    def set_device_index(self, value):
        self._device_index = value
    def set_sensor_index(self, value):
        self._sensor_index = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._board_index)
        buf += struct.pack("<B", self._sensor_board_index)
        buf += struct.pack("<B", self._device_index)
        buf += struct.pack("<B", self._sensor_index)
        return buf
    def get_error(self):
        return DS2482Error(self._error)
    def get_board_index(self):
        return self._board_index
    def get_sensor_board_index(self):
        return self._sensor_board_index
    def get_device_index(self):
        return self._device_index
    def get_sensor_index(self):
        return self._sensor_index
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        data.append((fields.board_index, self.get_board_index()))
        data.append((fields.sensor_board_index, self.get_sensor_board_index()))
        data.append((fields.device_index, self.get_device_index()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._board_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_board_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._device_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CBusStarted_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CBusStarted
        self._category = categories.none
        self._id = 497
        self._size = 5
        self._bus = 0
        self._frequency_hertz = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_frequency_hertz(self, value):
        self._frequency_hertz = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<L", self._frequency_hertz)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_frequency_hertz(self):
        return self._frequency_hertz
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.frequency_hertz, self.get_frequency_hertz()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._frequency_hertz = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class I2CBusStarted_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CBusStarted
        self._category = categories.none
        self._id = 498
        self._size = 5
        self._bus = 0
        self._frequency_hertz = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_frequency_hertz(self, value):
        self._frequency_hertz = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<L", self._frequency_hertz)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_frequency_hertz(self):
        return self._frequency_hertz
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.frequency_hertz, self.get_frequency_hertz()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._frequency_hertz = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class I2CBusStarted_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CBusStarted
        self._category = categories.none
        self._id = 499
        self._size = 5
        self._bus = 0
        self._frequency_hertz = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_frequency_hertz(self, value):
        self._frequency_hertz = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<L", self._frequency_hertz)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_frequency_hertz(self):
        return self._frequency_hertz
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.frequency_hertz, self.get_frequency_hertz()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._frequency_hertz = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class I2CBusStarted_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CBusStarted
        self._category = categories.none
        self._id = 500
        self._size = 5
        self._bus = 0
        self._frequency_hertz = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_frequency_hertz(self, value):
        self._frequency_hertz = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<L", self._frequency_hertz)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_frequency_hertz(self):
        return self._frequency_hertz
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.frequency_hertz, self.get_frequency_hertz()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._frequency_hertz = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class I2CBusStarted_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CBusStarted
        self._category = categories.none
        self._id = 501
        self._size = 5
        self._bus = 0
        self._frequency_hertz = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_frequency_hertz(self, value):
        self._frequency_hertz = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<L", self._frequency_hertz)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_frequency_hertz(self):
        return self._frequency_hertz
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.frequency_hertz, self.get_frequency_hertz()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._frequency_hertz = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class MAX31850KError_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.MAX31850KError
        self._category = categories.none
        self._id = 703
        self._size = 2
        self._error = 0
        self._sensor_index = 0
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
    def set_error(self, value):
        self._error = value.value
    def set_sensor_index(self, value):
        self._sensor_index = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._sensor_index)
        return buf
    def get_error(self):
        return MAX31850KError(self._error)
    def get_sensor_index(self):
        return self._sensor_index
    def get_all_data(self):
        data = []
        data.append((fields.error, self.get_error()))
        data.append((fields.sensor_index, self.get_sensor_index()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage2_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage2
        self._category = categories.none
        self._id = 711
        self._size = 2
        self._byte0 = 0
        self._byte1 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage2_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage2
        self._category = categories.none
        self._id = 711
        self._size = 2
        self._byte0 = 0
        self._byte1 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage2_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage2
        self._category = categories.none
        self._id = 712
        self._size = 2
        self._byte0 = 0
        self._byte1 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage2_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage2
        self._category = categories.none
        self._id = 712
        self._size = 2
        self._byte0 = 0
        self._byte1 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage2_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage2
        self._category = categories.none
        self._id = 713
        self._size = 2
        self._byte0 = 0
        self._byte1 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage2_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage2
        self._category = categories.none
        self._id = 713
        self._size = 2
        self._byte0 = 0
        self._byte1 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage2_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage2
        self._category = categories.none
        self._id = 714
        self._size = 2
        self._byte0 = 0
        self._byte1 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage2_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage2
        self._category = categories.none
        self._id = 714
        self._size = 2
        self._byte0 = 0
        self._byte1 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage2_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage2
        self._category = categories.none
        self._id = 715
        self._size = 2
        self._byte0 = 0
        self._byte1 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage2_from_Edda_Simulator_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage2
        self._category = categories.none
        self._id = 715
        self._size = 2
        self._byte0 = 0
        self._byte1 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class OneWireSearchEnded_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireSearchEnded
        self._category = categories.none
        self._id = 716
        self._size = 6
        self._bus = 0
        self._searched_family_code = 0
        self._devices_successfully_found = 0
        self._devices_insuccessfully_found = 0
        self._search_time_ms = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_searched_family_code(self, value):
        self._searched_family_code = value
    def set_devices_successfully_found(self, value):
        self._devices_successfully_found = value
    def set_devices_insuccessfully_found(self, value):
        self._devices_insuccessfully_found = value
    def set_search_time_ms(self, value):
        self._search_time_ms = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._searched_family_code)
        buf += struct.pack("<B", self._devices_successfully_found)
        buf += struct.pack("<B", self._devices_insuccessfully_found)
        buf += struct.pack("<H", self._search_time_ms)
        return buf
    def get_bus(self):
        return OneWireBus(self._bus)
    def get_searched_family_code(self):
        return self._searched_family_code
    def get_devices_successfully_found(self):
        return self._devices_successfully_found
    def get_devices_insuccessfully_found(self):
        return self._devices_insuccessfully_found
    def get_search_time_ms(self):
        return self._search_time_ms
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.searched_family_code, self.get_searched_family_code()))
        data.append((fields.devices_successfully_found, self.get_devices_successfully_found()))
        data.append((fields.devices_insuccessfully_found, self.get_devices_insuccessfully_found()))
        data.append((fields.search_time_ms, self.get_search_time_ms()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._searched_family_code = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._devices_successfully_found = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._devices_insuccessfully_found = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._search_time_ms = struct.unpack_from("<H", buf, index)[0]
        index += 2
        return
class I2CSearchStarted_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchStarted
        self._category = categories.none
        self._id = 753
        self._size = 1
        self._bus = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchStarted_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchStarted
        self._category = categories.none
        self._id = 754
        self._size = 1
        self._bus = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchStarted_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchStarted
        self._category = categories.none
        self._id = 755
        self._size = 1
        self._bus = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchStarted_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchStarted
        self._category = categories.none
        self._id = 756
        self._size = 1
        self._bus = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchStarted_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchStarted
        self._category = categories.none
        self._id = 757
        self._size = 1
        self._bus = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class MAX31856Error_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.MAX31856Error
        self._category = categories.none
        self._id = 959
        self._size = 2
        self._sensor_index = 0
        self._raw_fault_register = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_raw_fault_register(self, value):
        self._raw_fault_register = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._raw_fault_register)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_raw_fault_register(self):
        return self._raw_fault_register
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.raw_fault_register, self.get_raw_fault_register()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._raw_fault_register = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage3_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage3
        self._category = categories.none
        self._id = 967
        self._size = 3
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage3_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage3
        self._category = categories.none
        self._id = 967
        self._size = 3
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage3_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage3
        self._category = categories.none
        self._id = 968
        self._size = 3
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage3_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage3
        self._category = categories.none
        self._id = 968
        self._size = 3
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage3_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage3
        self._category = categories.none
        self._id = 969
        self._size = 3
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage3_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage3
        self._category = categories.none
        self._id = 969
        self._size = 3
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage3_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage3
        self._category = categories.none
        self._id = 970
        self._size = 3
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage3_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage3
        self._category = categories.none
        self._id = 970
        self._size = 3
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage3_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage3
        self._category = categories.none
        self._id = 971
        self._size = 3
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage3_from_Edda_Simulator_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage3
        self._category = categories.none
        self._id = 971
        self._size = 3
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class OneWireDeviceStartupSuccess_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireDeviceStartupSuccess
        self._category = categories.none
        self._id = 972
        self._size = 6
        self._serial_byte0 = 0
        self._serial_byte1 = 0
        self._serial_byte2 = 0
        self._serial_byte3 = 0
        self._serial_byte4 = 0
        self._serial_byte5 = 0
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
    def set_serial_byte0(self, value):
        self._serial_byte0 = value
    def set_serial_byte1(self, value):
        self._serial_byte1 = value
    def set_serial_byte2(self, value):
        self._serial_byte2 = value
    def set_serial_byte3(self, value):
        self._serial_byte3 = value
    def set_serial_byte4(self, value):
        self._serial_byte4 = value
    def set_serial_byte5(self, value):
        self._serial_byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._serial_byte0)
        buf += struct.pack("<B", self._serial_byte1)
        buf += struct.pack("<B", self._serial_byte2)
        buf += struct.pack("<B", self._serial_byte3)
        buf += struct.pack("<B", self._serial_byte4)
        buf += struct.pack("<B", self._serial_byte5)
        return buf
    def get_serial_byte0(self):
        return self._serial_byte0
    def get_serial_byte1(self):
        return self._serial_byte1
    def get_serial_byte2(self):
        return self._serial_byte2
    def get_serial_byte3(self):
        return self._serial_byte3
    def get_serial_byte4(self):
        return self._serial_byte4
    def get_serial_byte5(self):
        return self._serial_byte5
    def get_all_data(self):
        data = []
        data.append((fields.serial_byte0, self.get_serial_byte0()))
        data.append((fields.serial_byte1, self.get_serial_byte1()))
        data.append((fields.serial_byte2, self.get_serial_byte2()))
        data.append((fields.serial_byte3, self.get_serial_byte3()))
        data.append((fields.serial_byte4, self.get_serial_byte4()))
        data.append((fields.serial_byte5, self.get_serial_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._serial_byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchError_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchError
        self._category = categories.none
        self._id = 1009
        self._size = 3
        self._bus = 0
        self._error = 0
        self._scanned_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_error(self, value):
        self._error = value.value
    def set_scanned_address(self, value):
        self._scanned_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._scanned_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_error(self):
        return I2CError(self._error)
    def get_scanned_address(self):
        return self._scanned_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.error, self.get_error()))
        data.append((fields.scanned_address, self.get_scanned_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._scanned_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchError_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchError
        self._category = categories.none
        self._id = 1010
        self._size = 3
        self._bus = 0
        self._error = 0
        self._scanned_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_error(self, value):
        self._error = value.value
    def set_scanned_address(self, value):
        self._scanned_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._scanned_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_error(self):
        return I2CError(self._error)
    def get_scanned_address(self):
        return self._scanned_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.error, self.get_error()))
        data.append((fields.scanned_address, self.get_scanned_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._scanned_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchError_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchError
        self._category = categories.none
        self._id = 1011
        self._size = 3
        self._bus = 0
        self._error = 0
        self._scanned_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_error(self, value):
        self._error = value.value
    def set_scanned_address(self, value):
        self._scanned_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._scanned_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_error(self):
        return I2CError(self._error)
    def get_scanned_address(self):
        return self._scanned_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.error, self.get_error()))
        data.append((fields.scanned_address, self.get_scanned_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._scanned_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchError_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchError
        self._category = categories.none
        self._id = 1012
        self._size = 3
        self._bus = 0
        self._error = 0
        self._scanned_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_error(self, value):
        self._error = value.value
    def set_scanned_address(self, value):
        self._scanned_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._scanned_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_error(self):
        return I2CError(self._error)
    def get_scanned_address(self):
        return self._scanned_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.error, self.get_error()))
        data.append((fields.scanned_address, self.get_scanned_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._scanned_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchError_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchError
        self._category = categories.none
        self._id = 1013
        self._size = 3
        self._bus = 0
        self._error = 0
        self._scanned_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_error(self, value):
        self._error = value.value
    def set_scanned_address(self, value):
        self._scanned_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._error)
        buf += struct.pack("<B", self._scanned_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_error(self):
        return I2CError(self._error)
    def get_scanned_address(self):
        return self._scanned_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.error, self.get_error()))
        data.append((fields.scanned_address, self.get_scanned_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._scanned_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class MAX31865Error_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.MAX31865Error
        self._category = categories.none
        self._id = 1215
        self._size = 2
        self._sensor_index = 0
        self._raw_fault_register = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_raw_fault_register(self, value):
        self._raw_fault_register = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._raw_fault_register)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_raw_fault_register(self):
        return self._raw_fault_register
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.raw_fault_register, self.get_raw_fault_register()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._raw_fault_register = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage4_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage4
        self._category = categories.none
        self._id = 1223
        self._size = 4
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage4_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage4
        self._category = categories.none
        self._id = 1223
        self._size = 4
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage4_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage4
        self._category = categories.none
        self._id = 1224
        self._size = 4
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage4_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage4
        self._category = categories.none
        self._id = 1224
        self._size = 4
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage4_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage4
        self._category = categories.none
        self._id = 1225
        self._size = 4
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage4_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage4
        self._category = categories.none
        self._id = 1225
        self._size = 4
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage4_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage4
        self._category = categories.none
        self._id = 1226
        self._size = 4
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage4_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage4
        self._category = categories.none
        self._id = 1226
        self._size = 4
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage4_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage4
        self._category = categories.none
        self._id = 1227
        self._size = 4
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage4_from_Edda_Simulator_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage4
        self._category = categories.none
        self._id = 1227
        self._size = 4
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class OneWireDeviceStartupFailure_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireDeviceStartupFailure
        self._category = categories.none
        self._id = 1228
        self._size = 6
        self._serial_byte0 = 0
        self._serial_byte1 = 0
        self._serial_byte2 = 0
        self._serial_byte3 = 0
        self._serial_byte4 = 0
        self._serial_byte5 = 0
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
    def set_serial_byte0(self, value):
        self._serial_byte0 = value
    def set_serial_byte1(self, value):
        self._serial_byte1 = value
    def set_serial_byte2(self, value):
        self._serial_byte2 = value
    def set_serial_byte3(self, value):
        self._serial_byte3 = value
    def set_serial_byte4(self, value):
        self._serial_byte4 = value
    def set_serial_byte5(self, value):
        self._serial_byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._serial_byte0)
        buf += struct.pack("<B", self._serial_byte1)
        buf += struct.pack("<B", self._serial_byte2)
        buf += struct.pack("<B", self._serial_byte3)
        buf += struct.pack("<B", self._serial_byte4)
        buf += struct.pack("<B", self._serial_byte5)
        return buf
    def get_serial_byte0(self):
        return self._serial_byte0
    def get_serial_byte1(self):
        return self._serial_byte1
    def get_serial_byte2(self):
        return self._serial_byte2
    def get_serial_byte3(self):
        return self._serial_byte3
    def get_serial_byte4(self):
        return self._serial_byte4
    def get_serial_byte5(self):
        return self._serial_byte5
    def get_all_data(self):
        data = []
        data.append((fields.serial_byte0, self.get_serial_byte0()))
        data.append((fields.serial_byte1, self.get_serial_byte1()))
        data.append((fields.serial_byte2, self.get_serial_byte2()))
        data.append((fields.serial_byte3, self.get_serial_byte3()))
        data.append((fields.serial_byte4, self.get_serial_byte4()))
        data.append((fields.serial_byte5, self.get_serial_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._serial_byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchFoundDevice_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchFoundDevice
        self._category = categories.none
        self._id = 1265
        self._size = 2
        self._bus = 0
        self._found_device_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_found_device_address(self, value):
        self._found_device_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._found_device_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_found_device_address(self):
        return self._found_device_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.found_device_address, self.get_found_device_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._found_device_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchFoundDevice_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchFoundDevice
        self._category = categories.none
        self._id = 1266
        self._size = 2
        self._bus = 0
        self._found_device_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_found_device_address(self, value):
        self._found_device_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._found_device_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_found_device_address(self):
        return self._found_device_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.found_device_address, self.get_found_device_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._found_device_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchFoundDevice_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchFoundDevice
        self._category = categories.none
        self._id = 1267
        self._size = 2
        self._bus = 0
        self._found_device_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_found_device_address(self, value):
        self._found_device_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._found_device_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_found_device_address(self):
        return self._found_device_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.found_device_address, self.get_found_device_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._found_device_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchFoundDevice_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchFoundDevice
        self._category = categories.none
        self._id = 1268
        self._size = 2
        self._bus = 0
        self._found_device_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_found_device_address(self, value):
        self._found_device_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._found_device_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_found_device_address(self):
        return self._found_device_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.found_device_address, self.get_found_device_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._found_device_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchFoundDevice_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchFoundDevice
        self._category = categories.none
        self._id = 1269
        self._size = 2
        self._bus = 0
        self._found_device_address = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_found_device_address(self, value):
        self._found_device_address = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._found_device_address)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_found_device_address(self):
        return self._found_device_address
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.found_device_address, self.get_found_device_address()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._found_device_address = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage5_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage5
        self._category = categories.none
        self._id = 1479
        self._size = 5
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage5_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage5
        self._category = categories.none
        self._id = 1479
        self._size = 5
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage5_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage5
        self._category = categories.none
        self._id = 1480
        self._size = 5
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage5_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage5
        self._category = categories.none
        self._id = 1480
        self._size = 5
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage5_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage5
        self._category = categories.none
        self._id = 1481
        self._size = 5
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage5_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage5
        self._category = categories.none
        self._id = 1481
        self._size = 5
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage5_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage5
        self._category = categories.none
        self._id = 1482
        self._size = 5
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage5_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage5
        self._category = categories.none
        self._id = 1482
        self._size = 5
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage5_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage5
        self._category = categories.none
        self._id = 1483
        self._size = 5
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage5_from_Edda_Simulator_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage5
        self._category = categories.none
        self._id = 1483
        self._size = 5
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class OneWireDevicePairedWithSensor_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.OneWireDevicePairedWithSensor
        self._category = categories.none
        self._id = 1484
        self._size = 7
        self._sensor_index = 0
        self._serial_byte0 = 0
        self._serial_byte1 = 0
        self._serial_byte2 = 0
        self._serial_byte3 = 0
        self._serial_byte4 = 0
        self._serial_byte5 = 0
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
    def set_sensor_index(self, value):
        self._sensor_index = value
    def set_serial_byte0(self, value):
        self._serial_byte0 = value
    def set_serial_byte1(self, value):
        self._serial_byte1 = value
    def set_serial_byte2(self, value):
        self._serial_byte2 = value
    def set_serial_byte3(self, value):
        self._serial_byte3 = value
    def set_serial_byte4(self, value):
        self._serial_byte4 = value
    def set_serial_byte5(self, value):
        self._serial_byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._sensor_index)
        buf += struct.pack("<B", self._serial_byte0)
        buf += struct.pack("<B", self._serial_byte1)
        buf += struct.pack("<B", self._serial_byte2)
        buf += struct.pack("<B", self._serial_byte3)
        buf += struct.pack("<B", self._serial_byte4)
        buf += struct.pack("<B", self._serial_byte5)
        return buf
    def get_sensor_index(self):
        return self._sensor_index
    def get_serial_byte0(self):
        return self._serial_byte0
    def get_serial_byte1(self):
        return self._serial_byte1
    def get_serial_byte2(self):
        return self._serial_byte2
    def get_serial_byte3(self):
        return self._serial_byte3
    def get_serial_byte4(self):
        return self._serial_byte4
    def get_serial_byte5(self):
        return self._serial_byte5
    def get_all_data(self):
        data = []
        data.append((fields.sensor_index, self.get_sensor_index()))
        data.append((fields.serial_byte0, self.get_serial_byte0()))
        data.append((fields.serial_byte1, self.get_serial_byte1()))
        data.append((fields.serial_byte2, self.get_serial_byte2()))
        data.append((fields.serial_byte3, self.get_serial_byte3()))
        data.append((fields.serial_byte4, self.get_serial_byte4()))
        data.append((fields.serial_byte5, self.get_serial_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._sensor_index = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._serial_byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class I2CSearchEnded_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchEnded
        self._category = categories.none
        self._id = 1521
        self._size = 7
        self._bus = 0
        self._devices_successfully_found = 0
        self._addresses_with_error = 0
        self._search_time_us = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_devices_successfully_found(self, value):
        self._devices_successfully_found = value
    def set_addresses_with_error(self, value):
        self._addresses_with_error = value
    def set_search_time_us(self, value):
        self._search_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._devices_successfully_found)
        buf += struct.pack("<B", self._addresses_with_error)
        buf += struct.pack("<L", self._search_time_us)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_devices_successfully_found(self):
        return self._devices_successfully_found
    def get_addresses_with_error(self):
        return self._addresses_with_error
    def get_search_time_us(self):
        return self._search_time_us
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.devices_successfully_found, self.get_devices_successfully_found()))
        data.append((fields.addresses_with_error, self.get_addresses_with_error()))
        data.append((fields.search_time_us, self.get_search_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._devices_successfully_found = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._addresses_with_error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._search_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class I2CSearchEnded_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchEnded
        self._category = categories.none
        self._id = 1522
        self._size = 7
        self._bus = 0
        self._devices_successfully_found = 0
        self._addresses_with_error = 0
        self._search_time_us = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_devices_successfully_found(self, value):
        self._devices_successfully_found = value
    def set_addresses_with_error(self, value):
        self._addresses_with_error = value
    def set_search_time_us(self, value):
        self._search_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._devices_successfully_found)
        buf += struct.pack("<B", self._addresses_with_error)
        buf += struct.pack("<L", self._search_time_us)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_devices_successfully_found(self):
        return self._devices_successfully_found
    def get_addresses_with_error(self):
        return self._addresses_with_error
    def get_search_time_us(self):
        return self._search_time_us
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.devices_successfully_found, self.get_devices_successfully_found()))
        data.append((fields.addresses_with_error, self.get_addresses_with_error()))
        data.append((fields.search_time_us, self.get_search_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._devices_successfully_found = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._addresses_with_error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._search_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class I2CSearchEnded_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchEnded
        self._category = categories.none
        self._id = 1523
        self._size = 7
        self._bus = 0
        self._devices_successfully_found = 0
        self._addresses_with_error = 0
        self._search_time_us = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_devices_successfully_found(self, value):
        self._devices_successfully_found = value
    def set_addresses_with_error(self, value):
        self._addresses_with_error = value
    def set_search_time_us(self, value):
        self._search_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._devices_successfully_found)
        buf += struct.pack("<B", self._addresses_with_error)
        buf += struct.pack("<L", self._search_time_us)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_devices_successfully_found(self):
        return self._devices_successfully_found
    def get_addresses_with_error(self):
        return self._addresses_with_error
    def get_search_time_us(self):
        return self._search_time_us
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.devices_successfully_found, self.get_devices_successfully_found()))
        data.append((fields.addresses_with_error, self.get_addresses_with_error()))
        data.append((fields.search_time_us, self.get_search_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._devices_successfully_found = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._addresses_with_error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._search_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class I2CSearchEnded_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchEnded
        self._category = categories.none
        self._id = 1524
        self._size = 7
        self._bus = 0
        self._devices_successfully_found = 0
        self._addresses_with_error = 0
        self._search_time_us = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_devices_successfully_found(self, value):
        self._devices_successfully_found = value
    def set_addresses_with_error(self, value):
        self._addresses_with_error = value
    def set_search_time_us(self, value):
        self._search_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._devices_successfully_found)
        buf += struct.pack("<B", self._addresses_with_error)
        buf += struct.pack("<L", self._search_time_us)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_devices_successfully_found(self):
        return self._devices_successfully_found
    def get_addresses_with_error(self):
        return self._addresses_with_error
    def get_search_time_us(self):
        return self._search_time_us
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.devices_successfully_found, self.get_devices_successfully_found()))
        data.append((fields.addresses_with_error, self.get_addresses_with_error()))
        data.append((fields.search_time_us, self.get_search_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._devices_successfully_found = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._addresses_with_error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._search_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class I2CSearchEnded_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.I2CSearchEnded
        self._category = categories.none
        self._id = 1525
        self._size = 7
        self._bus = 0
        self._devices_successfully_found = 0
        self._addresses_with_error = 0
        self._search_time_us = 0
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
    def set_bus(self, value):
        self._bus = value.value
    def set_devices_successfully_found(self, value):
        self._devices_successfully_found = value
    def set_addresses_with_error(self, value):
        self._addresses_with_error = value
    def set_search_time_us(self, value):
        self._search_time_us = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._bus)
        buf += struct.pack("<B", self._devices_successfully_found)
        buf += struct.pack("<B", self._addresses_with_error)
        buf += struct.pack("<L", self._search_time_us)
        return buf
    def get_bus(self):
        return I2CBus(self._bus)
    def get_devices_successfully_found(self):
        return self._devices_successfully_found
    def get_addresses_with_error(self):
        return self._addresses_with_error
    def get_search_time_us(self):
        return self._search_time_us
    def get_all_data(self):
        data = []
        data.append((fields.bus, self.get_bus()))
        data.append((fields.devices_successfully_found, self.get_devices_successfully_found()))
        data.append((fields.addresses_with_error, self.get_addresses_with_error()))
        data.append((fields.search_time_us, self.get_search_time_us()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._bus = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._devices_successfully_found = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._addresses_with_error = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._search_time_us = struct.unpack_from("<L", buf, index)[0]
        index += 4
        return
class PartialDebugMessage6_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage6
        self._category = categories.none
        self._id = 1735
        self._size = 6
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage6_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage6
        self._category = categories.none
        self._id = 1735
        self._size = 6
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage6_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage6
        self._category = categories.none
        self._id = 1736
        self._size = 6
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage6_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage6
        self._category = categories.none
        self._id = 1736
        self._size = 6
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage6_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage6
        self._category = categories.none
        self._id = 1737
        self._size = 6
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage6_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage6
        self._category = categories.none
        self._id = 1737
        self._size = 6
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage6_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage6
        self._category = categories.none
        self._id = 1738
        self._size = 6
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage6_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage6
        self._category = categories.none
        self._id = 1738
        self._size = 6
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage6_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage6
        self._category = categories.none
        self._id = 1739
        self._size = 6
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage6_from_Edda_Simulator_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage6
        self._category = categories.none
        self._id = 1739
        self._size = 6
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage7_from_Edda_Telemetry_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage7
        self._category = categories.none
        self._id = 1991
        self._size = 7
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
        self._byte6 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def set_byte6(self, value):
        self._byte6 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_byte6(self):
        return self._byte6
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        data.append((fields.byte6, self.get_byte6()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte6 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage7_from_Edda_Telemetry_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Telemetry
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage7
        self._category = categories.none
        self._id = 1991
        self._size = 7
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
        self._byte6 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def set_byte6(self, value):
        self._byte6 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_byte6(self):
        return self._byte6
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        data.append((fields.byte6, self.get_byte6()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte6 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage7_from_Edda_Controller_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage7
        self._category = categories.none
        self._id = 1992
        self._size = 7
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
        self._byte6 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def set_byte6(self, value):
        self._byte6 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_byte6(self):
        return self._byte6
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        data.append((fields.byte6, self.get_byte6()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte6 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage7_from_Edda_Controller_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Controller
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage7
        self._category = categories.none
        self._id = 1992
        self._size = 7
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
        self._byte6 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def set_byte6(self, value):
        self._byte6 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_byte6(self):
        return self._byte6
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        data.append((fields.byte6, self.get_byte6()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte6 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage7_from_Edda_Pressure_Top_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage7
        self._category = categories.none
        self._id = 1993
        self._size = 7
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
        self._byte6 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def set_byte6(self, value):
        self._byte6 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_byte6(self):
        return self._byte6
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        data.append((fields.byte6, self.get_byte6()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte6 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage7_from_Edda_Pressure_Top_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Top
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage7
        self._category = categories.none
        self._id = 1993
        self._size = 7
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
        self._byte6 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def set_byte6(self, value):
        self._byte6 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_byte6(self):
        return self._byte6
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        data.append((fields.byte6, self.get_byte6()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte6 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage7_from_Edda_Pressure_Bottom_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage7
        self._category = categories.none
        self._id = 1994
        self._size = 7
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
        self._byte6 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def set_byte6(self, value):
        self._byte6 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_byte6(self):
        return self._byte6
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        data.append((fields.byte6, self.get_byte6()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte6 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage7_from_Edda_Pressure_Bottom_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Pressure_Bottom
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage7
        self._category = categories.none
        self._id = 1994
        self._size = 7
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
        self._byte6 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def set_byte6(self, value):
        self._byte6 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_byte6(self):
        return self._byte6
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        data.append((fields.byte6, self.get_byte6()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte6 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage7_from_Edda_Simulator_to_Ground_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Ground_Controller
        self._message = messages.PartialDebugMessage7
        self._category = categories.none
        self._id = 1995
        self._size = 7
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
        self._byte6 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def set_byte6(self, value):
        self._byte6 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_byte6(self):
        return self._byte6
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        data.append((fields.byte6, self.get_byte6()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte6 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
class PartialDebugMessage7_from_Edda_Simulator_to_Flight_Controller:
    def __init__(self):
        self._sender = nodes.Edda_Simulator
        self._receiver = nodes.Flight_Controller
        self._message = messages.PartialDebugMessage7
        self._category = categories.none
        self._id = 1995
        self._size = 7
        self._byte0 = 0
        self._byte1 = 0
        self._byte2 = 0
        self._byte3 = 0
        self._byte4 = 0
        self._byte5 = 0
        self._byte6 = 0
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
    def set_byte0(self, value):
        self._byte0 = value
    def set_byte1(self, value):
        self._byte1 = value
    def set_byte2(self, value):
        self._byte2 = value
    def set_byte3(self, value):
        self._byte3 = value
    def set_byte4(self, value):
        self._byte4 = value
    def set_byte5(self, value):
        self._byte5 = value
    def set_byte6(self, value):
        self._byte6 = value
    def build_buf(self):
        buf = b""
        buf += struct.pack("<B", self._byte0)
        buf += struct.pack("<B", self._byte1)
        buf += struct.pack("<B", self._byte2)
        buf += struct.pack("<B", self._byte3)
        buf += struct.pack("<B", self._byte4)
        buf += struct.pack("<B", self._byte5)
        buf += struct.pack("<B", self._byte6)
        return buf
    def get_byte0(self):
        return self._byte0
    def get_byte1(self):
        return self._byte1
    def get_byte2(self):
        return self._byte2
    def get_byte3(self):
        return self._byte3
    def get_byte4(self):
        return self._byte4
    def get_byte5(self):
        return self._byte5
    def get_byte6(self):
        return self._byte6
    def get_all_data(self):
        data = []
        data.append((fields.byte0, self.get_byte0()))
        data.append((fields.byte1, self.get_byte1()))
        data.append((fields.byte2, self.get_byte2()))
        data.append((fields.byte3, self.get_byte3()))
        data.append((fields.byte4, self.get_byte4()))
        data.append((fields.byte5, self.get_byte5()))
        data.append((fields.byte6, self.get_byte6()))
        return data
    def parse_buf(self, buf):
        index = 0
        self._byte0 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte1 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte2 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte3 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte4 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte5 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        self._byte6 = struct.unpack_from("<B", buf, index)[0]
        index += 1
        return
def id_to_message_class(id):
    if id == 0:
        receiver = CurrentTimePing_from_Flight_Controller_to_Edda_Controller()
        return receiver
    if id == 0:
        receiver = CurrentTimePing_from_Flight_Controller_to_Edda_Telemetry()
        return receiver
    if id == 0:
        receiver = CurrentTimePing_from_Flight_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 0:
        receiver = CurrentTimePing_from_Flight_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 0:
        receiver = CurrentTimePing_from_Flight_Controller_to_Edda_Simulator()
        return receiver
    if id == 1:
        receiver = SayHi_from_Flight_Controller_to_Edda_Controller()
        return receiver
    if id == 1:
        receiver = SayHi_from_Flight_Controller_to_Edda_Telemetry()
        return receiver
    if id == 1:
        receiver = SayHi_from_Flight_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 1:
        receiver = SayHi_from_Flight_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 1:
        receiver = SayHi_from_Flight_Controller_to_Edda_Simulator()
        return receiver
    if id == 4:
        receiver = CurrentTimePong_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 5:
        receiver = CurrentTimePong_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 6:
        receiver = CurrentTimePong_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 7:
        receiver = CurrentTimePong_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 8:
        receiver = CurrentTimePong_from_Edda_Simulator_to_Flight_Controller()
        return receiver
    if id == 9:
        receiver = Hello_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 10:
        receiver = Hello_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 11:
        receiver = Hello_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 12:
        receiver = Hello_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 13:
        receiver = Hello_from_Edda_Simulator_to_Flight_Controller()
        return receiver
    if id == 48:
        receiver = SetDebugModeRequest_from_Flight_Controller_to_Edda_Controller()
        return receiver
    if id == 48:
        receiver = SetDebugModeRequest_from_Flight_Controller_to_Edda_Telemetry()
        return receiver
    if id == 48:
        receiver = SetDebugModeRequest_from_Flight_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 48:
        receiver = SetDebugModeRequest_from_Flight_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 48:
        receiver = SetDebugModeRequest_from_Flight_Controller_to_Edda_Simulator()
        return receiver
    if id == 49:
        receiver = SetPowerModeRequest_from_Flight_Controller_to_Edda_Controller()
        return receiver
    if id == 49:
        receiver = SetPowerModeRequest_from_Flight_Controller_to_Edda_Telemetry()
        return receiver
    if id == 49:
        receiver = SetPowerModeRequest_from_Flight_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 49:
        receiver = SetPowerModeRequest_from_Flight_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 49:
        receiver = SetPowerModeRequest_from_Flight_Controller_to_Edda_Simulator()
        return receiver
    if id == 50:
        receiver = PowerCAN_SetDebugMode_from_Ground_Controller_to_Edda_Controller()
        return receiver
    if id == 51:
        receiver = PowerCAN_GetState_from_Ground_Controller_to_Edda_Controller()
        return receiver
    if id == 52:
        receiver = PowerCAN_TransitionRequest_from_Ground_Controller_to_Edda_Controller()
        return receiver
    if id == 64:
        receiver = GoingToSleep_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 65:
        receiver = GoingToSleep_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 66:
        receiver = GoingToSleep_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 67:
        receiver = GoingToSleep_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 68:
        receiver = GoingToSleep_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 69:
        receiver = WokeUp_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 70:
        receiver = WokeUp_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 71:
        receiver = WokeUp_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 72:
        receiver = WokeUp_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 73:
        receiver = WokeUp_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 144:
        receiver = CanLatency_from_Flight_Controller_to_Ground_Controller()
        return receiver
    if id == 144:
        receiver = CanLatency_from_Flight_Controller_to_Edda_Controller()
        return receiver
    if id == 144:
        receiver = CanLatency_from_Flight_Controller_to_Edda_Telemetry()
        return receiver
    if id == 144:
        receiver = CanLatency_from_Flight_Controller_to_Edda_Pressure_Top()
        return receiver
    if id == 144:
        receiver = CanLatency_from_Flight_Controller_to_Edda_Pressure_Bottom()
        return receiver
    if id == 144:
        receiver = CanLatency_from_Flight_Controller_to_Edda_Simulator()
        return receiver
    if id == 145:
        receiver = CanStatistics_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 146:
        receiver = CanStatistics_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 147:
        receiver = CanStatistics_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 148:
        receiver = CanStatistics_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 149:
        receiver = CanStatistics_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 150:
        receiver = WenHop_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 151:
        receiver = WenHop_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 152:
        receiver = WenHop_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 153:
        receiver = WenHop_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 154:
        receiver = WenHop_from_Edda_Simulator_to_Flight_Controller()
        return receiver
    if id == 155:
        receiver = PowerInputMeasurement_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 156:
        receiver = PowerInputMeasurement_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 157:
        receiver = PowerInputMeasurement_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 158:
        receiver = PowerInputMeasurement_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 159:
        receiver = PowerInputMeasurement_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 160:
        receiver = PowerInputMeasurementError_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 161:
        receiver = PowerInputMeasurementError_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 162:
        receiver = PowerInputMeasurementError_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 163:
        receiver = PowerInputMeasurementError_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 164:
        receiver = PowerInputMeasurementError_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 165:
        receiver = RawTransducerVoltage_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 166:
        receiver = RawTransducerVoltage_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 167:
        receiver = AmbientPressure_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 168:
        receiver = AmbientPressure_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 169:
        receiver = AmbientPressure_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 170:
        receiver = TransducerPressure_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 170:
        receiver = TransducerPressure_from_Edda_Pressure_Top_to_Edda_Telemetry()
        return receiver
    if id == 171:
        receiver = TransducerPressure_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 171:
        receiver = TransducerPressure_from_Edda_Pressure_Bottom_to_Edda_Telemetry()
        return receiver
    if id == 172:
        receiver = TransducerPressure_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 172:
        receiver = TransducerPressure_from_Edda_Simulator_to_Edda_Telemetry()
        return receiver
    if id == 173:
        receiver = TransducerError_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 174:
        receiver = TransducerError_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 175:
        receiver = TransducerError_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 176:
        receiver = AmbientPressureError_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 177:
        receiver = AmbientPressureError_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 178:
        receiver = AmbientPressureError_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 179:
        receiver = AmbientPressureCoefficient_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 180:
        receiver = AmbientPressureCoefficient_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 181:
        receiver = ColdSideTemperature_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 182:
        receiver = ColdSideTemperature_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 183:
        receiver = ColdSideTemperature_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 184:
        receiver = ColdSideTemperature_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 185:
        receiver = ColdSideTemperature_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 186:
        receiver = PlatinumSensorTemperature_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 187:
        receiver = PlatinumSensorResistance_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 188:
        receiver = PlatinumSensorRatio_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 189:
        receiver = ThermocoupleTypeKTemperature_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 190:
        receiver = ThermocoupleTypeKTemperature_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 192:
        receiver = Humidity_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 193:
        receiver = HumidityError_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 194:
        receiver = Acceleration_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 195:
        receiver = AccelerationSelfTest_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 196:
        receiver = AccelerationError_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 197:
        receiver = AmbientLight_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 198:
        receiver = AmbientLightError_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 206:
        receiver = OneWireSearchFamilyMismatch_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 207:
        receiver = OneWireSearchCRCMismatch_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 208:
        receiver = OneWireSearchFoundDevice_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 209:
        receiver = PowerCAN_SetDebugMode_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 210:
        receiver = PowerCAN_GetState_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 211:
        receiver = PowerCAN_TransitionRequest_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 212:
        receiver = PowerCAN_Hello_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 213:
        receiver = PowerCAN_CurrentState_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 214:
        receiver = PowerCAN_Temperature_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 215:
        receiver = PowerCAN_Voltage_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 216:
        receiver = PowerCAN_ChannelMeasurementPower_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 217:
        receiver = PowerCAN_ChannelMeasurementVoltage_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 218:
        receiver = PowerCAN_ChannelMeasurementCurrent_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 219:
        receiver = PowerCAN_LoadMeasurementResistance_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 220:
        receiver = PowerCAN_LoadMeasurementVoltage_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 221:
        receiver = PowerCAN_LoadMeasurementPower_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 222:
        receiver = PowerCAN_LoadMeasurementCurrent_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 223:
        receiver = PowerCAN_FailedLoadMeasurementValue_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 224:
        receiver = PowerCAN_FailedLoadMeasurementThreshold_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 225:
        receiver = PowerCAN_ResistanceMeasurementResistance_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 226:
        receiver = PowerCAN_ResistanceMeasurementReferenceVoltage_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 227:
        receiver = PowerCAN_ResistanceMeasurementDifferentialVoltage_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 228:
        receiver = PowerCAN_ResistanceMeasurementPositiveVoltage_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 229:
        receiver = PowerCAN_ResistanceMeasurementNegativeVoltage_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 230:
        receiver = PowerCAN_LTC2992Error_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 231:
        receiver = PowerCAN_ADS122C04Error_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 232:
        receiver = PowerCAN_CheckResult_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 233:
        receiver = PowerCAN_TransitionResponse_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 234:
        receiver = PowerCAN_I2CBusStarted_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 235:
        receiver = PowerCAN_I2CSearchStarted_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 236:
        receiver = PowerCAN_I2CSearchError_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 237:
        receiver = PowerCAN_I2CSearchFoundDevice_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 238:
        receiver = PowerCAN_I2CSearchMissingDevice_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 239:
        receiver = PowerCAN_I2CSearchEnded_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 240:
        receiver = PowerCAN_ErrorStatistics_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 246:
        receiver = TaskInfo_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 247:
        receiver = TaskInfo_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 248:
        receiver = TaskInfo_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 249:
        receiver = TaskInfo_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 250:
        receiver = TaskInfo_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 251:
        receiver = LoopInfo_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 252:
        receiver = LoopInfo_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 253:
        receiver = LoopInfo_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 254:
        receiver = LoopInfo_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 255:
        receiver = LoopInfo_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 447:
        receiver = DS28E18QError_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 455:
        receiver = PartialDebugMessage1_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 455:
        receiver = PartialDebugMessage1_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 456:
        receiver = PartialDebugMessage1_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 456:
        receiver = PartialDebugMessage1_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 457:
        receiver = PartialDebugMessage1_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 457:
        receiver = PartialDebugMessage1_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 458:
        receiver = PartialDebugMessage1_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 458:
        receiver = PartialDebugMessage1_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 459:
        receiver = PartialDebugMessage1_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 459:
        receiver = PartialDebugMessage1_from_Edda_Simulator_to_Flight_Controller()
        return receiver
    if id == 460:
        receiver = OneWireSearchStarted_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 461:
        receiver = TemperatureBoardBridgeError_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 497:
        receiver = I2CBusStarted_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 498:
        receiver = I2CBusStarted_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 499:
        receiver = I2CBusStarted_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 500:
        receiver = I2CBusStarted_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 501:
        receiver = I2CBusStarted_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 703:
        receiver = MAX31850KError_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 711:
        receiver = PartialDebugMessage2_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 711:
        receiver = PartialDebugMessage2_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 712:
        receiver = PartialDebugMessage2_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 712:
        receiver = PartialDebugMessage2_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 713:
        receiver = PartialDebugMessage2_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 713:
        receiver = PartialDebugMessage2_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 714:
        receiver = PartialDebugMessage2_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 714:
        receiver = PartialDebugMessage2_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 715:
        receiver = PartialDebugMessage2_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 715:
        receiver = PartialDebugMessage2_from_Edda_Simulator_to_Flight_Controller()
        return receiver
    if id == 716:
        receiver = OneWireSearchEnded_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 753:
        receiver = I2CSearchStarted_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 754:
        receiver = I2CSearchStarted_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 755:
        receiver = I2CSearchStarted_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 756:
        receiver = I2CSearchStarted_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 757:
        receiver = I2CSearchStarted_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 959:
        receiver = MAX31856Error_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 967:
        receiver = PartialDebugMessage3_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 967:
        receiver = PartialDebugMessage3_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 968:
        receiver = PartialDebugMessage3_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 968:
        receiver = PartialDebugMessage3_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 969:
        receiver = PartialDebugMessage3_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 969:
        receiver = PartialDebugMessage3_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 970:
        receiver = PartialDebugMessage3_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 970:
        receiver = PartialDebugMessage3_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 971:
        receiver = PartialDebugMessage3_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 971:
        receiver = PartialDebugMessage3_from_Edda_Simulator_to_Flight_Controller()
        return receiver
    if id == 972:
        receiver = OneWireDeviceStartupSuccess_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 1009:
        receiver = I2CSearchError_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 1010:
        receiver = I2CSearchError_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 1011:
        receiver = I2CSearchError_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 1012:
        receiver = I2CSearchError_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 1013:
        receiver = I2CSearchError_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 1215:
        receiver = MAX31865Error_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 1223:
        receiver = PartialDebugMessage4_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 1223:
        receiver = PartialDebugMessage4_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 1224:
        receiver = PartialDebugMessage4_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 1224:
        receiver = PartialDebugMessage4_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 1225:
        receiver = PartialDebugMessage4_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 1225:
        receiver = PartialDebugMessage4_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 1226:
        receiver = PartialDebugMessage4_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 1226:
        receiver = PartialDebugMessage4_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 1227:
        receiver = PartialDebugMessage4_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 1227:
        receiver = PartialDebugMessage4_from_Edda_Simulator_to_Flight_Controller()
        return receiver
    if id == 1228:
        receiver = OneWireDeviceStartupFailure_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 1265:
        receiver = I2CSearchFoundDevice_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 1266:
        receiver = I2CSearchFoundDevice_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 1267:
        receiver = I2CSearchFoundDevice_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 1268:
        receiver = I2CSearchFoundDevice_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 1269:
        receiver = I2CSearchFoundDevice_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 1479:
        receiver = PartialDebugMessage5_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 1479:
        receiver = PartialDebugMessage5_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 1480:
        receiver = PartialDebugMessage5_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 1480:
        receiver = PartialDebugMessage5_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 1481:
        receiver = PartialDebugMessage5_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 1481:
        receiver = PartialDebugMessage5_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 1482:
        receiver = PartialDebugMessage5_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 1482:
        receiver = PartialDebugMessage5_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 1483:
        receiver = PartialDebugMessage5_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 1483:
        receiver = PartialDebugMessage5_from_Edda_Simulator_to_Flight_Controller()
        return receiver
    if id == 1484:
        receiver = OneWireDevicePairedWithSensor_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 1521:
        receiver = I2CSearchEnded_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 1522:
        receiver = I2CSearchEnded_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 1523:
        receiver = I2CSearchEnded_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 1524:
        receiver = I2CSearchEnded_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 1525:
        receiver = I2CSearchEnded_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 1735:
        receiver = PartialDebugMessage6_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 1735:
        receiver = PartialDebugMessage6_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 1736:
        receiver = PartialDebugMessage6_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 1736:
        receiver = PartialDebugMessage6_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 1737:
        receiver = PartialDebugMessage6_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 1737:
        receiver = PartialDebugMessage6_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 1738:
        receiver = PartialDebugMessage6_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 1738:
        receiver = PartialDebugMessage6_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 1739:
        receiver = PartialDebugMessage6_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 1739:
        receiver = PartialDebugMessage6_from_Edda_Simulator_to_Flight_Controller()
        return receiver
    if id == 1991:
        receiver = PartialDebugMessage7_from_Edda_Telemetry_to_Ground_Controller()
        return receiver
    if id == 1991:
        receiver = PartialDebugMessage7_from_Edda_Telemetry_to_Flight_Controller()
        return receiver
    if id == 1992:
        receiver = PartialDebugMessage7_from_Edda_Controller_to_Ground_Controller()
        return receiver
    if id == 1992:
        receiver = PartialDebugMessage7_from_Edda_Controller_to_Flight_Controller()
        return receiver
    if id == 1993:
        receiver = PartialDebugMessage7_from_Edda_Pressure_Top_to_Ground_Controller()
        return receiver
    if id == 1993:
        receiver = PartialDebugMessage7_from_Edda_Pressure_Top_to_Flight_Controller()
        return receiver
    if id == 1994:
        receiver = PartialDebugMessage7_from_Edda_Pressure_Bottom_to_Ground_Controller()
        return receiver
    if id == 1994:
        receiver = PartialDebugMessage7_from_Edda_Pressure_Bottom_to_Flight_Controller()
        return receiver
    if id == 1995:
        receiver = PartialDebugMessage7_from_Edda_Simulator_to_Ground_Controller()
        return receiver
    if id == 1995:
        receiver = PartialDebugMessage7_from_Edda_Simulator_to_Flight_Controller()
        return receiver
def is_specifier(sender, name, field):
    if (messages.CurrentTimePing == name and nodes.Flight_Controller == sender):
        if (fields.currentMillis == field):
            return False
        if (fields.currentMicros == field):
            return False
    if (messages.CurrentTimePing == name and nodes.Flight_Controller == sender):
        if (fields.currentMillis == field):
            return False
        if (fields.currentMicros == field):
            return False
    if (messages.CurrentTimePing == name and nodes.Flight_Controller == sender):
        if (fields.currentMillis == field):
            return False
        if (fields.currentMicros == field):
            return False
    if (messages.CurrentTimePing == name and nodes.Flight_Controller == sender):
        if (fields.currentMillis == field):
            return False
        if (fields.currentMicros == field):
            return False
    if (messages.CurrentTimePing == name and nodes.Flight_Controller == sender):
        if (fields.currentMillis == field):
            return False
        if (fields.currentMicros == field):
            return False
    if (messages.CurrentTimePong == name and nodes.Edda_Controller == sender):
        if (fields.currentMillis == field):
            return False
        if (fields.currentMicros == field):
            return False
    if (messages.CurrentTimePong == name and nodes.Edda_Telemetry == sender):
        if (fields.currentMillis == field):
            return False
        if (fields.currentMicros == field):
            return False
    if (messages.CurrentTimePong == name and nodes.Edda_Pressure_Top == sender):
        if (fields.currentMillis == field):
            return False
        if (fields.currentMicros == field):
            return False
    if (messages.CurrentTimePong == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.currentMillis == field):
            return False
        if (fields.currentMicros == field):
            return False
    if (messages.CurrentTimePong == name and nodes.Edda_Simulator == sender):
        if (fields.currentMillis == field):
            return False
        if (fields.currentMicros == field):
            return False
    if (messages.Hello == name and nodes.Edda_Controller == sender):
        if (fields.debugMessagesMode == field):
            return False
        if (fields.debugStatusLedsMode == field):
            return False
        if (fields.powerMode == field):
            return False
        if (fields.uptime_ms == field):
            return False
    if (messages.Hello == name and nodes.Edda_Telemetry == sender):
        if (fields.debugMessagesMode == field):
            return False
        if (fields.debugStatusLedsMode == field):
            return False
        if (fields.powerMode == field):
            return False
        if (fields.uptime_ms == field):
            return False
    if (messages.Hello == name and nodes.Edda_Pressure_Top == sender):
        if (fields.debugMessagesMode == field):
            return False
        if (fields.debugStatusLedsMode == field):
            return False
        if (fields.powerMode == field):
            return False
        if (fields.uptime_ms == field):
            return False
    if (messages.Hello == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.debugMessagesMode == field):
            return False
        if (fields.debugStatusLedsMode == field):
            return False
        if (fields.powerMode == field):
            return False
        if (fields.uptime_ms == field):
            return False
    if (messages.Hello == name and nodes.Edda_Simulator == sender):
        if (fields.debugMessagesMode == field):
            return False
        if (fields.debugStatusLedsMode == field):
            return False
        if (fields.powerMode == field):
            return False
        if (fields.uptime_ms == field):
            return False
    if (messages.SetDebugModeRequest == name and nodes.Flight_Controller == sender):
        if (fields.receiver_node_id == field):
            return True
        if (fields.messages == field):
            return False
        if (fields.statusLeds == field):
            return False
    if (messages.SetDebugModeRequest == name and nodes.Flight_Controller == sender):
        if (fields.receiver_node_id == field):
            return True
        if (fields.messages == field):
            return False
        if (fields.statusLeds == field):
            return False
    if (messages.SetDebugModeRequest == name and nodes.Flight_Controller == sender):
        if (fields.receiver_node_id == field):
            return True
        if (fields.messages == field):
            return False
        if (fields.statusLeds == field):
            return False
    if (messages.SetDebugModeRequest == name and nodes.Flight_Controller == sender):
        if (fields.receiver_node_id == field):
            return True
        if (fields.messages == field):
            return False
        if (fields.statusLeds == field):
            return False
    if (messages.SetDebugModeRequest == name and nodes.Flight_Controller == sender):
        if (fields.receiver_node_id == field):
            return True
        if (fields.messages == field):
            return False
        if (fields.statusLeds == field):
            return False
    if (messages.SetPowerModeRequest == name and nodes.Flight_Controller == sender):
        if (fields.receiver_node_id == field):
            return True
        if (fields.mode == field):
            return True
    if (messages.SetPowerModeRequest == name and nodes.Flight_Controller == sender):
        if (fields.receiver_node_id == field):
            return True
        if (fields.mode == field):
            return True
    if (messages.SetPowerModeRequest == name and nodes.Flight_Controller == sender):
        if (fields.receiver_node_id == field):
            return True
        if (fields.mode == field):
            return True
    if (messages.SetPowerModeRequest == name and nodes.Flight_Controller == sender):
        if (fields.receiver_node_id == field):
            return True
        if (fields.mode == field):
            return True
    if (messages.SetPowerModeRequest == name and nodes.Flight_Controller == sender):
        if (fields.receiver_node_id == field):
            return True
        if (fields.mode == field):
            return True
    if (messages.PowerCAN_SetDebugMode == name and nodes.Ground_Controller == sender):
        if (fields.debug_mode == field):
            return True
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_GetState == name and nodes.Ground_Controller == sender):
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_TransitionRequest == name and nodes.Ground_Controller == sender):
        if (fields.edda_signature == field):
            return False
        if (fields.request == field):
            return True
        if (fields.powercan_channel == field):
            return True
    if (messages.GoingToSleep == name and nodes.Edda_Telemetry == sender):
        if (fields.timeSpentAwake_ms == field):
            return False
    if (messages.GoingToSleep == name and nodes.Edda_Controller == sender):
        if (fields.timeSpentAwake_ms == field):
            return False
    if (messages.GoingToSleep == name and nodes.Edda_Pressure_Top == sender):
        if (fields.timeSpentAwake_ms == field):
            return False
    if (messages.GoingToSleep == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.timeSpentAwake_ms == field):
            return False
    if (messages.GoingToSleep == name and nodes.Edda_Simulator == sender):
        if (fields.timeSpentAwake_ms == field):
            return False
    if (messages.WokeUp == name and nodes.Edda_Telemetry == sender):
        if (fields.timeSpentSleeping_us == field):
            return False
    if (messages.WokeUp == name and nodes.Edda_Controller == sender):
        if (fields.timeSpentSleeping_us == field):
            return False
    if (messages.WokeUp == name and nodes.Edda_Pressure_Top == sender):
        if (fields.timeSpentSleeping_us == field):
            return False
    if (messages.WokeUp == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.timeSpentSleeping_us == field):
            return False
    if (messages.WokeUp == name and nodes.Edda_Simulator == sender):
        if (fields.timeSpentSleeping_us == field):
            return False
    if (messages.CanLatency == name and nodes.Flight_Controller == sender):
        if (fields.roundTripTime_us == field):
            return False
        if (fields.destination_node_id == field):
            return True
    if (messages.CanLatency == name and nodes.Flight_Controller == sender):
        if (fields.roundTripTime_us == field):
            return False
        if (fields.destination_node_id == field):
            return True
    if (messages.CanLatency == name and nodes.Flight_Controller == sender):
        if (fields.roundTripTime_us == field):
            return False
        if (fields.destination_node_id == field):
            return True
    if (messages.CanLatency == name and nodes.Flight_Controller == sender):
        if (fields.roundTripTime_us == field):
            return False
        if (fields.destination_node_id == field):
            return True
    if (messages.CanLatency == name and nodes.Flight_Controller == sender):
        if (fields.roundTripTime_us == field):
            return False
        if (fields.destination_node_id == field):
            return True
    if (messages.CanLatency == name and nodes.Flight_Controller == sender):
        if (fields.roundTripTime_us == field):
            return False
        if (fields.destination_node_id == field):
            return True
    if (messages.CanStatistics == name and nodes.Edda_Controller == sender):
        if (fields.maxTxQueueSize == field):
            return False
        if (fields.maxRxQueueSize == field):
            return False
        if (fields.meanTxQueueSize == field):
            return False
        if (fields.meanRxQueueSize == field):
            return False
    if (messages.CanStatistics == name and nodes.Edda_Telemetry == sender):
        if (fields.maxTxQueueSize == field):
            return False
        if (fields.maxRxQueueSize == field):
            return False
        if (fields.meanTxQueueSize == field):
            return False
        if (fields.meanRxQueueSize == field):
            return False
    if (messages.CanStatistics == name and nodes.Edda_Pressure_Top == sender):
        if (fields.maxTxQueueSize == field):
            return False
        if (fields.maxRxQueueSize == field):
            return False
        if (fields.meanTxQueueSize == field):
            return False
        if (fields.meanRxQueueSize == field):
            return False
    if (messages.CanStatistics == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.maxTxQueueSize == field):
            return False
        if (fields.maxRxQueueSize == field):
            return False
        if (fields.meanTxQueueSize == field):
            return False
        if (fields.meanRxQueueSize == field):
            return False
    if (messages.CanStatistics == name and nodes.Edda_Simulator == sender):
        if (fields.maxTxQueueSize == field):
            return False
        if (fields.maxRxQueueSize == field):
            return False
        if (fields.meanTxQueueSize == field):
            return False
        if (fields.meanRxQueueSize == field):
            return False
    if (messages.WenHop == name and nodes.Edda_Controller == sender):
        if (fields.w == field):
            return False
        if (fields.e == field):
            return False
        if (fields.n == field):
            return False
        if (fields.h == field):
            return False
        if (fields.o == field):
            return False
        if (fields.p == field):
            return False
    if (messages.WenHop == name and nodes.Edda_Telemetry == sender):
        if (fields.w == field):
            return False
        if (fields.e == field):
            return False
        if (fields.n == field):
            return False
        if (fields.h == field):
            return False
        if (fields.o == field):
            return False
        if (fields.p == field):
            return False
    if (messages.WenHop == name and nodes.Edda_Pressure_Top == sender):
        if (fields.w == field):
            return False
        if (fields.e == field):
            return False
        if (fields.n == field):
            return False
        if (fields.h == field):
            return False
        if (fields.o == field):
            return False
        if (fields.p == field):
            return False
    if (messages.WenHop == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.w == field):
            return False
        if (fields.e == field):
            return False
        if (fields.n == field):
            return False
        if (fields.h == field):
            return False
        if (fields.o == field):
            return False
        if (fields.p == field):
            return False
    if (messages.WenHop == name and nodes.Edda_Simulator == sender):
        if (fields.w == field):
            return False
        if (fields.e == field):
            return False
        if (fields.n == field):
            return False
        if (fields.h == field):
            return False
        if (fields.o == field):
            return False
        if (fields.p == field):
            return False
    if (messages.PowerInputMeasurement == name and nodes.Edda_Controller == sender):
        if (fields.current_amperes == field):
            return False
        if (fields.voltage_volts == field):
            return False
        if (fields.power_watts == field):
            return False
    if (messages.PowerInputMeasurement == name and nodes.Edda_Telemetry == sender):
        if (fields.current_amperes == field):
            return False
        if (fields.voltage_volts == field):
            return False
        if (fields.power_watts == field):
            return False
    if (messages.PowerInputMeasurement == name and nodes.Edda_Pressure_Top == sender):
        if (fields.current_amperes == field):
            return False
        if (fields.voltage_volts == field):
            return False
        if (fields.power_watts == field):
            return False
    if (messages.PowerInputMeasurement == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.current_amperes == field):
            return False
        if (fields.voltage_volts == field):
            return False
        if (fields.power_watts == field):
            return False
    if (messages.PowerInputMeasurement == name and nodes.Edda_Simulator == sender):
        if (fields.current_amperes == field):
            return False
        if (fields.voltage_volts == field):
            return False
        if (fields.power_watts == field):
            return False
    if (messages.PowerInputMeasurementError == name and nodes.Edda_Controller == sender):
        if (fields.error == field):
            return True
    if (messages.PowerInputMeasurementError == name and nodes.Edda_Telemetry == sender):
        if (fields.error == field):
            return True
    if (messages.PowerInputMeasurementError == name and nodes.Edda_Pressure_Top == sender):
        if (fields.error == field):
            return True
    if (messages.PowerInputMeasurementError == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.error == field):
            return True
    if (messages.PowerInputMeasurementError == name and nodes.Edda_Simulator == sender):
        if (fields.error == field):
            return True
    if (messages.RawTransducerVoltage == name and nodes.Edda_Pressure_Top == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.voltage_volts == field):
            return False
    if (messages.RawTransducerVoltage == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.voltage_volts == field):
            return False
    if (messages.AmbientPressure == name and nodes.Edda_Pressure_Top == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.pressure_millibars == field):
            return False
    if (messages.AmbientPressure == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.pressure_millibars == field):
            return False
    if (messages.AmbientPressure == name and nodes.Edda_Simulator == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.pressure_millibars == field):
            return False
    if (messages.TransducerPressure == name and nodes.Edda_Pressure_Top == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.pressure_pascal == field):
            return False
    if (messages.TransducerPressure == name and nodes.Edda_Pressure_Top == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.pressure_pascal == field):
            return False
    if (messages.TransducerPressure == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.pressure_pascal == field):
            return False
    if (messages.TransducerPressure == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.pressure_pascal == field):
            return False
    if (messages.TransducerPressure == name and nodes.Edda_Simulator == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.pressure_pascal == field):
            return False
    if (messages.TransducerPressure == name and nodes.Edda_Simulator == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.pressure_pascal == field):
            return False
    if (messages.TransducerError == name and nodes.Edda_Pressure_Top == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.error == field):
            return True
    if (messages.TransducerError == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.error == field):
            return True
    if (messages.TransducerError == name and nodes.Edda_Simulator == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.error == field):
            return True
    if (messages.AmbientPressureError == name and nodes.Edda_Pressure_Top == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.error == field):
            return True
    if (messages.AmbientPressureError == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.error == field):
            return True
    if (messages.AmbientPressureError == name and nodes.Edda_Simulator == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.error == field):
            return True
    if (messages.AmbientPressureCoefficient == name and nodes.Edda_Pressure_Top == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.coefficient_index == field):
            return True
        if (fields.coefficient_value == field):
            return False
    if (messages.AmbientPressureCoefficient == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.coefficient_index == field):
            return True
        if (fields.coefficient_value == field):
            return False
    if (messages.ColdSideTemperature == name and nodes.Edda_Telemetry == sender):
        if (fields.sensor_type == field):
            return True
        if (fields.sensor_index == field):
            return True
        if (fields.temperature_celsius == field):
            return False
    if (messages.ColdSideTemperature == name and nodes.Edda_Controller == sender):
        if (fields.sensor_type == field):
            return True
        if (fields.sensor_index == field):
            return True
        if (fields.temperature_celsius == field):
            return False
    if (messages.ColdSideTemperature == name and nodes.Edda_Pressure_Top == sender):
        if (fields.sensor_type == field):
            return True
        if (fields.sensor_index == field):
            return True
        if (fields.temperature_celsius == field):
            return False
    if (messages.ColdSideTemperature == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.sensor_type == field):
            return True
        if (fields.sensor_index == field):
            return True
        if (fields.temperature_celsius == field):
            return False
    if (messages.ColdSideTemperature == name and nodes.Edda_Simulator == sender):
        if (fields.sensor_type == field):
            return True
        if (fields.sensor_index == field):
            return True
        if (fields.temperature_celsius == field):
            return False
    if (messages.PlatinumSensorTemperature == name and nodes.Edda_Telemetry == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.temperature_celsius == field):
            return False
    if (messages.PlatinumSensorResistance == name and nodes.Edda_Telemetry == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.resistance_ohms == field):
            return False
    if (messages.PlatinumSensorRatio == name and nodes.Edda_Telemetry == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.ratio_fraction == field):
            return False
    if (messages.ThermocoupleTypeKTemperature == name and nodes.Edda_Telemetry == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.temperature_celsius == field):
            return False
    if (messages.ThermocoupleTypeKTemperature == name and nodes.Edda_Simulator == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.temperature_celsius == field):
            return False
    if (messages.Humidity == name and nodes.Edda_Controller == sender):
        if (fields.relative_humidity == field):
            return False
        if (fields.is_heater_on == field):
            return False
    if (messages.HumidityError == name and nodes.Edda_Controller == sender):
        if (fields.error == field):
            return True
    if (messages.Acceleration == name and nodes.Edda_Controller == sender):
        if (fields.acceleration_x_gforce == field):
            return False
        if (fields.acceleration_y_gforce == field):
            return False
        if (fields.acceleration_z_gforce == field):
            return False
    if (messages.AccelerationSelfTest == name and nodes.Edda_Controller == sender):
        if (fields.sign == field):
            return True
        if (fields.result == field):
            return False
        if (fields.acceleration_x_gforce == field):
            return False
        if (fields.acceleration_y_gforce == field):
            return False
        if (fields.acceleration_z_gforce == field):
            return False
    if (messages.AccelerationError == name and nodes.Edda_Controller == sender):
        if (fields.error == field):
            return True
    if (messages.AmbientLight == name and nodes.Edda_Controller == sender):
        if (fields.ambientLight_lux == field):
            return False
    if (messages.AmbientLightError == name and nodes.Edda_Controller == sender):
        if (fields.error == field):
            return True
    if (messages.OneWireSearchFamilyMismatch == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.serial_byte0 == field):
            return False
        if (fields.serial_byte1 == field):
            return False
        if (fields.serial_byte2 == field):
            return False
        if (fields.serial_byte3 == field):
            return False
        if (fields.serial_byte4 == field):
            return False
        if (fields.serial_byte5 == field):
            return False
        if (fields.found_family_code == field):
            return False
    if (messages.OneWireSearchCRCMismatch == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.serial_byte0 == field):
            return False
        if (fields.serial_byte1 == field):
            return False
        if (fields.serial_byte2 == field):
            return False
        if (fields.serial_byte3 == field):
            return False
        if (fields.serial_byte4 == field):
            return False
        if (fields.serial_byte5 == field):
            return False
        if (fields.found_crc == field):
            return False
    if (messages.OneWireSearchFoundDevice == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.serial_byte0 == field):
            return False
        if (fields.serial_byte1 == field):
            return False
        if (fields.serial_byte2 == field):
            return False
        if (fields.serial_byte3 == field):
            return False
        if (fields.serial_byte4 == field):
            return False
        if (fields.serial_byte5 == field):
            return False
    if (messages.PowerCAN_SetDebugMode == name and nodes.Edda_Controller == sender):
        if (fields.debug_mode == field):
            return True
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_GetState == name and nodes.Edda_Controller == sender):
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_TransitionRequest == name and nodes.Edda_Controller == sender):
        if (fields.edda_signature == field):
            return False
        if (fields.request == field):
            return True
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_Hello == name and nodes.Edda_Controller == sender):
        if (fields.debug_mode == field):
            return True
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_CurrentState == name and nodes.Edda_Controller == sender):
        if (fields.system_state == field):
            return True
        if (fields.gate_state == field):
            return True
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_Temperature == name and nodes.Edda_Controller == sender):
        if (fields.kind == field):
            return True
        if (fields.temperature_celsius == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_Voltage == name and nodes.Edda_Controller == sender):
        if (fields.kind == field):
            return True
        if (fields.voltage_volts == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ChannelMeasurementPower == name and nodes.Edda_Controller == sender):
        if (fields.channel == field):
            return True
        if (fields.power_watts == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ChannelMeasurementVoltage == name and nodes.Edda_Controller == sender):
        if (fields.channel == field):
            return True
        if (fields.voltage_volts == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ChannelMeasurementCurrent == name and nodes.Edda_Controller == sender):
        if (fields.channel == field):
            return True
        if (fields.current_amperes == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_LoadMeasurementResistance == name and nodes.Edda_Controller == sender):
        if (fields.measurement_reference == field):
            return True
        if (fields.result == field):
            return True
        if (fields.resistance_ohms == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_LoadMeasurementVoltage == name and nodes.Edda_Controller == sender):
        if (fields.measurement_reference == field):
            return True
        if (fields.result == field):
            return True
        if (fields.voltage_volts == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_LoadMeasurementPower == name and nodes.Edda_Controller == sender):
        if (fields.measurement_reference == field):
            return True
        if (fields.result == field):
            return True
        if (fields.power_watts == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_LoadMeasurementCurrent == name and nodes.Edda_Controller == sender):
        if (fields.measurement_reference == field):
            return True
        if (fields.result == field):
            return True
        if (fields.current_amperes == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_FailedLoadMeasurementValue == name and nodes.Edda_Controller == sender):
        if (fields.measurement_reference == field):
            return True
        if (fields.failure_reason == field):
            return True
        if (fields.value == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_FailedLoadMeasurementThreshold == name and nodes.Edda_Controller == sender):
        if (fields.measurement_reference == field):
            return True
        if (fields.failure_reason == field):
            return True
        if (fields.threshold == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ResistanceMeasurementResistance == name and nodes.Edda_Controller == sender):
        if (fields.measurement_reference == field):
            return True
        if (fields.validity == field):
            return True
        if (fields.resistance_ohms == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ResistanceMeasurementReferenceVoltage == name and nodes.Edda_Controller == sender):
        if (fields.measurement_reference == field):
            return True
        if (fields.validity == field):
            return True
        if (fields.reference_voltage_volts == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ResistanceMeasurementDifferentialVoltage == name and nodes.Edda_Controller == sender):
        if (fields.measurement_reference == field):
            return True
        if (fields.validity == field):
            return True
        if (fields.differential_voltage_volts == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ResistanceMeasurementPositiveVoltage == name and nodes.Edda_Controller == sender):
        if (fields.measurement_reference == field):
            return True
        if (fields.validity == field):
            return True
        if (fields.positive_voltage_volts == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ResistanceMeasurementNegativeVoltage == name and nodes.Edda_Controller == sender):
        if (fields.measurement_reference == field):
            return True
        if (fields.validity == field):
            return True
        if (fields.negative_voltage_volts == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_LTC2992Error == name and nodes.Edda_Controller == sender):
        if (fields.error == field):
            return True
        if (fields.location == field):
            return True
        if (fields.register_address == field):
            return False
        if (fields.read_data == field):
            return False
        if (fields.write_data == field):
            return False
        if (fields.expected_data == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ADS122C04Error == name and nodes.Edda_Controller == sender):
        if (fields.error == field):
            return True
        if (fields.location == field):
            return True
        if (fields.register_address == field):
            return False
        if (fields.read_data == field):
            return False
        if (fields.write_data == field):
            return False
        if (fields.expected_data == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_CheckResult == name and nodes.Edda_Controller == sender):
        if (fields.result == field):
            return True
        if (fields.checks_failed == field):
            return False
        if (fields.checks_performed == field):
            return False
        if (fields.total_checks == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_TransitionResponse == name and nodes.Edda_Controller == sender):
        if (fields.request == field):
            return True
        if (fields.response == field):
            return True
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_I2CBusStarted == name and nodes.Edda_Controller == sender):
        if (fields.bus == field):
            return True
        if (fields.frequency_hertz == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_I2CSearchStarted == name and nodes.Edda_Controller == sender):
        if (fields.bus == field):
            return True
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_I2CSearchError == name and nodes.Edda_Controller == sender):
        if (fields.bus == field):
            return True
        if (fields.error == field):
            return True
        if (fields.scanned_address == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_I2CSearchFoundDevice == name and nodes.Edda_Controller == sender):
        if (fields.bus == field):
            return True
        if (fields.found_device_address == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_I2CSearchMissingDevice == name and nodes.Edda_Controller == sender):
        if (fields.bus == field):
            return True
        if (fields.missing_device_address == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_I2CSearchEnded == name and nodes.Edda_Controller == sender):
        if (fields.bus == field):
            return True
        if (fields.devices_successfully_found == field):
            return False
        if (fields.addresses_with_error == field):
            return False
        if (fields.search_time_us == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.PowerCAN_ErrorStatistics == name and nodes.Edda_Controller == sender):
        if (fields.warning_count == field):
            return False
        if (fields.error_count == field):
            return False
        if (fields.powercan_channel == field):
            return True
    if (messages.TaskInfo == name and nodes.Edda_Telemetry == sender):
        if (fields.type == field):
            return True
        if (fields.thread_id == field):
            return True
        if (fields.taskTime_microseconds == field):
            return False
        if (fields.truncated_startTime_microseconds == field):
            return False
    if (messages.TaskInfo == name and nodes.Edda_Controller == sender):
        if (fields.type == field):
            return True
        if (fields.thread_id == field):
            return True
        if (fields.taskTime_microseconds == field):
            return False
        if (fields.truncated_startTime_microseconds == field):
            return False
    if (messages.TaskInfo == name and nodes.Edda_Pressure_Top == sender):
        if (fields.type == field):
            return True
        if (fields.thread_id == field):
            return True
        if (fields.taskTime_microseconds == field):
            return False
        if (fields.truncated_startTime_microseconds == field):
            return False
    if (messages.TaskInfo == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.type == field):
            return True
        if (fields.thread_id == field):
            return True
        if (fields.taskTime_microseconds == field):
            return False
        if (fields.truncated_startTime_microseconds == field):
            return False
    if (messages.TaskInfo == name and nodes.Edda_Simulator == sender):
        if (fields.type == field):
            return True
        if (fields.thread_id == field):
            return True
        if (fields.taskTime_microseconds == field):
            return False
        if (fields.truncated_startTime_microseconds == field):
            return False
    if (messages.LoopInfo == name and nodes.Edda_Telemetry == sender):
        if (fields.type == field):
            return True
        if (fields.thread_id == field):
            return True
        if (fields.loopTime_microseconds == field):
            return False
        if (fields.truncated_startTime_microseconds == field):
            return False
    if (messages.LoopInfo == name and nodes.Edda_Controller == sender):
        if (fields.type == field):
            return True
        if (fields.thread_id == field):
            return True
        if (fields.loopTime_microseconds == field):
            return False
        if (fields.truncated_startTime_microseconds == field):
            return False
    if (messages.LoopInfo == name and nodes.Edda_Pressure_Top == sender):
        if (fields.type == field):
            return True
        if (fields.thread_id == field):
            return True
        if (fields.loopTime_microseconds == field):
            return False
        if (fields.truncated_startTime_microseconds == field):
            return False
    if (messages.LoopInfo == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.type == field):
            return True
        if (fields.thread_id == field):
            return True
        if (fields.loopTime_microseconds == field):
            return False
        if (fields.truncated_startTime_microseconds == field):
            return False
    if (messages.LoopInfo == name and nodes.Edda_Simulator == sender):
        if (fields.type == field):
            return True
        if (fields.thread_id == field):
            return True
        if (fields.loopTime_microseconds == field):
            return False
        if (fields.truncated_startTime_microseconds == field):
            return False
    if (messages.DS28E18QError == name and nodes.Edda_Telemetry == sender):
        if (fields.error == field):
            return True
        if (fields.sensor_index == field):
            return True
    if (messages.PartialDebugMessage1 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
    if (messages.PartialDebugMessage1 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
    if (messages.PartialDebugMessage1 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
    if (messages.PartialDebugMessage1 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
    if (messages.PartialDebugMessage1 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
    if (messages.PartialDebugMessage1 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
    if (messages.PartialDebugMessage1 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
    if (messages.PartialDebugMessage1 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
    if (messages.PartialDebugMessage1 == name and nodes.Edda_Simulator == sender):
        if (fields.byte0 == field):
            return False
    if (messages.PartialDebugMessage1 == name and nodes.Edda_Simulator == sender):
        if (fields.byte0 == field):
            return False
    if (messages.OneWireSearchStarted == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.start_time_ms == field):
            return False
    if (messages.TemperatureBoardBridgeError == name and nodes.Edda_Telemetry == sender):
        if (fields.error == field):
            return True
        if (fields.board_index == field):
            return True
        if (fields.sensor_board_index == field):
            return True
        if (fields.device_index == field):
            return True
        if (fields.sensor_index == field):
            return True
    if (messages.I2CBusStarted == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.frequency_hertz == field):
            return False
    if (messages.I2CBusStarted == name and nodes.Edda_Controller == sender):
        if (fields.bus == field):
            return True
        if (fields.frequency_hertz == field):
            return False
    if (messages.I2CBusStarted == name and nodes.Edda_Pressure_Top == sender):
        if (fields.bus == field):
            return True
        if (fields.frequency_hertz == field):
            return False
    if (messages.I2CBusStarted == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.bus == field):
            return True
        if (fields.frequency_hertz == field):
            return False
    if (messages.I2CBusStarted == name and nodes.Edda_Simulator == sender):
        if (fields.bus == field):
            return True
        if (fields.frequency_hertz == field):
            return False
    if (messages.MAX31850KError == name and nodes.Edda_Telemetry == sender):
        if (fields.error == field):
            return True
        if (fields.sensor_index == field):
            return True
    if (messages.PartialDebugMessage2 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
    if (messages.PartialDebugMessage2 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
    if (messages.PartialDebugMessage2 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
    if (messages.PartialDebugMessage2 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
    if (messages.PartialDebugMessage2 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
    if (messages.PartialDebugMessage2 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
    if (messages.PartialDebugMessage2 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
    if (messages.PartialDebugMessage2 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
    if (messages.PartialDebugMessage2 == name and nodes.Edda_Simulator == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
    if (messages.PartialDebugMessage2 == name and nodes.Edda_Simulator == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
    if (messages.OneWireSearchEnded == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.searched_family_code == field):
            return False
        if (fields.devices_successfully_found == field):
            return False
        if (fields.devices_insuccessfully_found == field):
            return False
        if (fields.search_time_ms == field):
            return False
    if (messages.I2CSearchStarted == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
    if (messages.I2CSearchStarted == name and nodes.Edda_Controller == sender):
        if (fields.bus == field):
            return True
    if (messages.I2CSearchStarted == name and nodes.Edda_Pressure_Top == sender):
        if (fields.bus == field):
            return True
    if (messages.I2CSearchStarted == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.bus == field):
            return True
    if (messages.I2CSearchStarted == name and nodes.Edda_Simulator == sender):
        if (fields.bus == field):
            return True
    if (messages.MAX31856Error == name and nodes.Edda_Telemetry == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.raw_fault_register == field):
            return False
    if (messages.PartialDebugMessage3 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
    if (messages.PartialDebugMessage3 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
    if (messages.PartialDebugMessage3 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
    if (messages.PartialDebugMessage3 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
    if (messages.PartialDebugMessage3 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
    if (messages.PartialDebugMessage3 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
    if (messages.PartialDebugMessage3 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
    if (messages.PartialDebugMessage3 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
    if (messages.PartialDebugMessage3 == name and nodes.Edda_Simulator == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
    if (messages.PartialDebugMessage3 == name and nodes.Edda_Simulator == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
    if (messages.OneWireDeviceStartupSuccess == name and nodes.Edda_Telemetry == sender):
        if (fields.serial_byte0 == field):
            return False
        if (fields.serial_byte1 == field):
            return False
        if (fields.serial_byte2 == field):
            return False
        if (fields.serial_byte3 == field):
            return False
        if (fields.serial_byte4 == field):
            return False
        if (fields.serial_byte5 == field):
            return False
    if (messages.I2CSearchError == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.error == field):
            return True
        if (fields.scanned_address == field):
            return False
    if (messages.I2CSearchError == name and nodes.Edda_Controller == sender):
        if (fields.bus == field):
            return True
        if (fields.error == field):
            return True
        if (fields.scanned_address == field):
            return False
    if (messages.I2CSearchError == name and nodes.Edda_Pressure_Top == sender):
        if (fields.bus == field):
            return True
        if (fields.error == field):
            return True
        if (fields.scanned_address == field):
            return False
    if (messages.I2CSearchError == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.bus == field):
            return True
        if (fields.error == field):
            return True
        if (fields.scanned_address == field):
            return False
    if (messages.I2CSearchError == name and nodes.Edda_Simulator == sender):
        if (fields.bus == field):
            return True
        if (fields.error == field):
            return True
        if (fields.scanned_address == field):
            return False
    if (messages.MAX31865Error == name and nodes.Edda_Telemetry == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.raw_fault_register == field):
            return False
    if (messages.PartialDebugMessage4 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
    if (messages.PartialDebugMessage4 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
    if (messages.PartialDebugMessage4 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
    if (messages.PartialDebugMessage4 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
    if (messages.PartialDebugMessage4 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
    if (messages.PartialDebugMessage4 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
    if (messages.PartialDebugMessage4 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
    if (messages.PartialDebugMessage4 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
    if (messages.PartialDebugMessage4 == name and nodes.Edda_Simulator == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
    if (messages.PartialDebugMessage4 == name and nodes.Edda_Simulator == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
    if (messages.OneWireDeviceStartupFailure == name and nodes.Edda_Telemetry == sender):
        if (fields.serial_byte0 == field):
            return False
        if (fields.serial_byte1 == field):
            return False
        if (fields.serial_byte2 == field):
            return False
        if (fields.serial_byte3 == field):
            return False
        if (fields.serial_byte4 == field):
            return False
        if (fields.serial_byte5 == field):
            return False
    if (messages.I2CSearchFoundDevice == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.found_device_address == field):
            return False
    if (messages.I2CSearchFoundDevice == name and nodes.Edda_Controller == sender):
        if (fields.bus == field):
            return True
        if (fields.found_device_address == field):
            return False
    if (messages.I2CSearchFoundDevice == name and nodes.Edda_Pressure_Top == sender):
        if (fields.bus == field):
            return True
        if (fields.found_device_address == field):
            return False
    if (messages.I2CSearchFoundDevice == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.bus == field):
            return True
        if (fields.found_device_address == field):
            return False
    if (messages.I2CSearchFoundDevice == name and nodes.Edda_Simulator == sender):
        if (fields.bus == field):
            return True
        if (fields.found_device_address == field):
            return False
    if (messages.PartialDebugMessage5 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
    if (messages.PartialDebugMessage5 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
    if (messages.PartialDebugMessage5 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
    if (messages.PartialDebugMessage5 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
    if (messages.PartialDebugMessage5 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
    if (messages.PartialDebugMessage5 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
    if (messages.PartialDebugMessage5 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
    if (messages.PartialDebugMessage5 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
    if (messages.PartialDebugMessage5 == name and nodes.Edda_Simulator == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
    if (messages.PartialDebugMessage5 == name and nodes.Edda_Simulator == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
    if (messages.OneWireDevicePairedWithSensor == name and nodes.Edda_Telemetry == sender):
        if (fields.sensor_index == field):
            return True
        if (fields.serial_byte0 == field):
            return False
        if (fields.serial_byte1 == field):
            return False
        if (fields.serial_byte2 == field):
            return False
        if (fields.serial_byte3 == field):
            return False
        if (fields.serial_byte4 == field):
            return False
        if (fields.serial_byte5 == field):
            return False
    if (messages.I2CSearchEnded == name and nodes.Edda_Telemetry == sender):
        if (fields.bus == field):
            return True
        if (fields.devices_successfully_found == field):
            return False
        if (fields.addresses_with_error == field):
            return False
        if (fields.search_time_us == field):
            return False
    if (messages.I2CSearchEnded == name and nodes.Edda_Controller == sender):
        if (fields.bus == field):
            return True
        if (fields.devices_successfully_found == field):
            return False
        if (fields.addresses_with_error == field):
            return False
        if (fields.search_time_us == field):
            return False
    if (messages.I2CSearchEnded == name and nodes.Edda_Pressure_Top == sender):
        if (fields.bus == field):
            return True
        if (fields.devices_successfully_found == field):
            return False
        if (fields.addresses_with_error == field):
            return False
        if (fields.search_time_us == field):
            return False
    if (messages.I2CSearchEnded == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.bus == field):
            return True
        if (fields.devices_successfully_found == field):
            return False
        if (fields.addresses_with_error == field):
            return False
        if (fields.search_time_us == field):
            return False
    if (messages.I2CSearchEnded == name and nodes.Edda_Simulator == sender):
        if (fields.bus == field):
            return True
        if (fields.devices_successfully_found == field):
            return False
        if (fields.addresses_with_error == field):
            return False
        if (fields.search_time_us == field):
            return False
    if (messages.PartialDebugMessage6 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
    if (messages.PartialDebugMessage6 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
    if (messages.PartialDebugMessage6 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
    if (messages.PartialDebugMessage6 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
    if (messages.PartialDebugMessage6 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
    if (messages.PartialDebugMessage6 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
    if (messages.PartialDebugMessage6 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
    if (messages.PartialDebugMessage6 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
    if (messages.PartialDebugMessage6 == name and nodes.Edda_Simulator == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
    if (messages.PartialDebugMessage6 == name and nodes.Edda_Simulator == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
    if (messages.PartialDebugMessage7 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
        if (fields.byte6 == field):
            return False
    if (messages.PartialDebugMessage7 == name and nodes.Edda_Telemetry == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
        if (fields.byte6 == field):
            return False
    if (messages.PartialDebugMessage7 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
        if (fields.byte6 == field):
            return False
    if (messages.PartialDebugMessage7 == name and nodes.Edda_Controller == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
        if (fields.byte6 == field):
            return False
    if (messages.PartialDebugMessage7 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
        if (fields.byte6 == field):
            return False
    if (messages.PartialDebugMessage7 == name and nodes.Edda_Pressure_Top == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
        if (fields.byte6 == field):
            return False
    if (messages.PartialDebugMessage7 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
        if (fields.byte6 == field):
            return False
    if (messages.PartialDebugMessage7 == name and nodes.Edda_Pressure_Bottom == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
        if (fields.byte6 == field):
            return False
    if (messages.PartialDebugMessage7 == name and nodes.Edda_Simulator == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
        if (fields.byte6 == field):
            return False
    if (messages.PartialDebugMessage7 == name and nodes.Edda_Simulator == sender):
        if (fields.byte0 == field):
            return False
        if (fields.byte1 == field):
            return False
        if (fields.byte2 == field):
            return False
        if (fields.byte3 == field):
            return False
        if (fields.byte4 == field):
            return False
        if (fields.byte5 == field):
            return False
        if (fields.byte6 == field):
            return False
    return False
def is_extended_id(id):
    if 1 == id:
        return null
    if 1 == id:
        return null
    if 1 == id:
        return null
    if 1 == id:
        return null
    if 1 == id:
        return null
    if 4 == id:
        return null
    if 5 == id:
        return null
    if 6 == id:
        return null
    if 7 == id:
        return null
    if 8 == id:
        return null
    if 9 == id:
        return null
    if 10 == id:
        return null
    if 11 == id:
        return null
    if 12 == id:
        return null
    if 13 == id:
        return null
    if 48 == id:
        return null
    if 48 == id:
        return null
    if 48 == id:
        return null
    if 48 == id:
        return null
    if 48 == id:
        return null
    if 49 == id:
        return null
    if 49 == id:
        return null
    if 49 == id:
        return null
    if 49 == id:
        return null
    if 49 == id:
        return null
    if 50 == id:
        return null
    if 51 == id:
        return null
    if 52 == id:
        return null
    if 64 == id:
        return null
    if 65 == id:
        return null
    if 66 == id:
        return null
    if 67 == id:
        return null
    if 68 == id:
        return null
    if 69 == id:
        return null
    if 70 == id:
        return null
    if 71 == id:
        return null
    if 72 == id:
        return null
    if 73 == id:
        return null
    if 144 == id:
        return null
    if 144 == id:
        return null
    if 144 == id:
        return null
    if 144 == id:
        return null
    if 144 == id:
        return null
    if 144 == id:
        return null
    if 145 == id:
        return null
    if 146 == id:
        return null
    if 147 == id:
        return null
    if 148 == id:
        return null
    if 149 == id:
        return null
    if 150 == id:
        return null
    if 151 == id:
        return null
    if 152 == id:
        return null
    if 153 == id:
        return null
    if 154 == id:
        return null
    if 155 == id:
        return null
    if 156 == id:
        return null
    if 157 == id:
        return null
    if 158 == id:
        return null
    if 159 == id:
        return null
    if 160 == id:
        return null
    if 161 == id:
        return null
    if 162 == id:
        return null
    if 163 == id:
        return null
    if 164 == id:
        return null
    if 165 == id:
        return null
    if 166 == id:
        return null
    if 167 == id:
        return null
    if 168 == id:
        return null
    if 169 == id:
        return null
    if 170 == id:
        return null
    if 170 == id:
        return null
    if 171 == id:
        return null
    if 171 == id:
        return null
    if 172 == id:
        return null
    if 172 == id:
        return null
    if 173 == id:
        return null
    if 174 == id:
        return null
    if 175 == id:
        return null
    if 176 == id:
        return null
    if 177 == id:
        return null
    if 178 == id:
        return null
    if 179 == id:
        return null
    if 180 == id:
        return null
    if 181 == id:
        return null
    if 182 == id:
        return null
    if 183 == id:
        return null
    if 184 == id:
        return null
    if 185 == id:
        return null
    if 186 == id:
        return null
    if 187 == id:
        return null
    if 188 == id:
        return null
    if 189 == id:
        return null
    if 190 == id:
        return null
    if 192 == id:
        return null
    if 193 == id:
        return null
    if 194 == id:
        return null
    if 195 == id:
        return null
    if 196 == id:
        return null
    if 197 == id:
        return null
    if 198 == id:
        return null
    if 206 == id:
        return null
    if 207 == id:
        return null
    if 208 == id:
        return null
    if 209 == id:
        return null
    if 210 == id:
        return null
    if 211 == id:
        return null
    if 212 == id:
        return null
    if 213 == id:
        return null
    if 214 == id:
        return null
    if 215 == id:
        return null
    if 216 == id:
        return null
    if 217 == id:
        return null
    if 218 == id:
        return null
    if 219 == id:
        return null
    if 220 == id:
        return null
    if 221 == id:
        return null
    if 222 == id:
        return null
    if 223 == id:
        return null
    if 224 == id:
        return null
    if 225 == id:
        return null
    if 226 == id:
        return null
    if 227 == id:
        return null
    if 228 == id:
        return null
    if 229 == id:
        return null
    if 230 == id:
        return null
    if 231 == id:
        return null
    if 232 == id:
        return null
    if 233 == id:
        return null
    if 234 == id:
        return null
    if 235 == id:
        return null
    if 236 == id:
        return null
    if 237 == id:
        return null
    if 238 == id:
        return null
    if 239 == id:
        return null
    if 240 == id:
        return null
    if 246 == id:
        return null
    if 247 == id:
        return null
    if 248 == id:
        return null
    if 249 == id:
        return null
    if 250 == id:
        return null
    if 251 == id:
        return null
    if 252 == id:
        return null
    if 253 == id:
        return null
    if 254 == id:
        return null
    if 255 == id:
        return null
    if 191 == id:
        return 1
    if 199 == id:
        return 1
    if 199 == id:
        return 1
    if 200 == id:
        return 1
    if 200 == id:
        return 1
    if 201 == id:
        return 1
    if 201 == id:
        return 1
    if 202 == id:
        return 1
    if 202 == id:
        return 1
    if 203 == id:
        return 1
    if 203 == id:
        return 1
    if 204 == id:
        return 1
    if 205 == id:
        return 1
    if 241 == id:
        return 1
    if 242 == id:
        return 1
    if 243 == id:
        return 1
    if 244 == id:
        return 1
    if 245 == id:
        return 1
    if 191 == id:
        return 2
    if 199 == id:
        return 2
    if 199 == id:
        return 2
    if 200 == id:
        return 2
    if 200 == id:
        return 2
    if 201 == id:
        return 2
    if 201 == id:
        return 2
    if 202 == id:
        return 2
    if 202 == id:
        return 2
    if 203 == id:
        return 2
    if 203 == id:
        return 2
    if 204 == id:
        return 2
    if 241 == id:
        return 2
    if 242 == id:
        return 2
    if 243 == id:
        return 2
    if 244 == id:
        return 2
    if 245 == id:
        return 2
    if 191 == id:
        return 3
    if 199 == id:
        return 3
    if 199 == id:
        return 3
    if 200 == id:
        return 3
    if 200 == id:
        return 3
    if 201 == id:
        return 3
    if 201 == id:
        return 3
    if 202 == id:
        return 3
    if 202 == id:
        return 3
    if 203 == id:
        return 3
    if 203 == id:
        return 3
    if 204 == id:
        return 3
    if 241 == id:
        return 3
    if 242 == id:
        return 3
    if 243 == id:
        return 3
    if 244 == id:
        return 3
    if 245 == id:
        return 3
    if 191 == id:
        return 4
    if 199 == id:
        return 4
    if 199 == id:
        return 4
    if 200 == id:
        return 4
    if 200 == id:
        return 4
    if 201 == id:
        return 4
    if 201 == id:
        return 4
    if 202 == id:
        return 4
    if 202 == id:
        return 4
    if 203 == id:
        return 4
    if 203 == id:
        return 4
    if 204 == id:
        return 4
    if 241 == id:
        return 4
    if 242 == id:
        return 4
    if 243 == id:
        return 4
    if 244 == id:
        return 4
    if 245 == id:
        return 4
    if 199 == id:
        return 5
    if 199 == id:
        return 5
    if 200 == id:
        return 5
    if 200 == id:
        return 5
    if 201 == id:
        return 5
    if 201 == id:
        return 5
    if 202 == id:
        return 5
    if 202 == id:
        return 5
    if 203 == id:
        return 5
    if 203 == id:
        return 5
    if 204 == id:
        return 5
    if 241 == id:
        return 5
    if 242 == id:
        return 5
    if 243 == id:
        return 5
    if 244 == id:
        return 5
    if 245 == id:
        return 5
    if 199 == id:
        return 6
    if 199 == id:
        return 6
    if 200 == id:
        return 6
    if 200 == id:
        return 6
    if 201 == id:
        return 6
    if 201 == id:
        return 6
    if 202 == id:
        return 6
    if 202 == id:
        return 6
    if 203 == id:
        return 6
    if 203 == id:
        return 6
    if 199 == id:
        return 7
    if 199 == id:
        return 7
    if 200 == id:
        return 7
    if 200 == id:
        return 7
    if 201 == id:
        return 7
    if 201 == id:
        return 7
    if 202 == id:
        return 7
    if 202 == id:
        return 7
    if 203 == id:
        return 7
    if 203 == id:
        return 7
    return
