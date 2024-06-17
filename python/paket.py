import struct

START_BYTE = 0xAA
END_BYTE = 0x55

# Packet Types
DATA_PACKET = 0x01
COMMAND_PACKET = 0x02
HEARTBEAT_PACKET = 0x03

# Calculate checksum
def calculate_checksum(data):
    checksum = 0
    for byte in data:
        checksum ^= byte
    return checksum

# Construct Data Packet
def construct_data_packet(left_motor_speed, right_motor_speed, fuel_level, temperature):
    temperature_int = int(temperature * 100)
    fl_int = int(fuel_level)
    packet = struct.pack('>BBHHBHB', START_BYTE, DATA_PACKET, left_motor_speed, right_motor_speed, fl_int, temperature_int, 0)
    checksum = calculate_checksum(packet[:-1])
    packet = packet[:-1] + bytes([checksum]) + bytes([END_BYTE])
    return packet

# Construct Command Packet
def construct_command_packet(forward_backward, left_right):
    packet = struct.pack('>BBB', START_BYTE, COMMAND_PACKET, forward_backward, left_right, 0)
    checksum = calculate_checksum(packet[:-1])
    packet = packet[:-1] + bytes([checksum]) + bytes([END_BYTE])
    return packet

# Construct Heartbeat Packet
def construct_heartbeat_packet():
    packet = struct.pack('>BBB', START_BYTE, HEARTBEAT_PACKET, 0)
    checksum = calculate_checksum(packet[:-1])
    packet = packet[:-1] + bytes([checksum]) + bytes([END_BYTE])
    return packet

# Parse Command Packet
def parse_command_packet(packet):
    if len(packet) == 6 and packet[0] == START_BYTE and packet[-1] == END_BYTE:
        data_type, forward_backward, left_right, checksum = struct.unpack('>BBB', packet[1:-1])
        calculated_checksum = calculate_checksum(packet[:-2])
        if calculated_checksum == checksum and data_type == COMMAND_PACKET:
            return forward_backward, left_right
    return None, None
