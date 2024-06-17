import paket
import struct
import time
import random

# Constants
START_BYTE = 0xAA
END_BYTE = 0x55

# Simulated robot state
left_motor_speed = 0
right_motor_speed = 0
fuel_level = 100  # 100%
temperature = 25.0  # Celsius

# Function to create data packet
def create_data_packet():
    global left_motor_speed, right_motor_speed, fuel_level, temperature
    packet = struct.pack('>BBHHBHB', START_BYTE, 0x01, left_motor_speed, right_motor_speed, fuel_level, int(temperature * 100), 0, END_BYTE)
    checksum = sum(packet[:-2]) & 0xFF
    packet = packet[:-2] + bytes([checksum]) + packet[-1:]
    return packet

# Function to create heartbeat packet
def create_heartbeat_packet():
    packet = struct.pack('>BBB', START_BYTE, 0x03, 0)
    checksum = sum(packet[:-2]) & 0xFF
    packet = packet[:-2] + bytes([checksum]) + packet[-1:]
    return packet

# Function to parse command packet
def parse_command_packet(packet):
    global left_motor_speed, right_motor_speed
    if len(packet) == 6 and packet[0] == START_BYTE and packet[-1] == END_BYTE:
        data_type, forward_backward, left_right, checksum = struct.unpack('>BBBB', packet[1:])
        if data_type == 0x02:
            # Update motor speeds based on joystick input
            left_motor_speed = forward_backward + left_right
            right_motor_speed = forward_backward - left_right

	# Simulate sending data packets and heartbeat
while True:
    # Simulate sending data packet
    data_packet = create_data_packet()
    print("Sending Data Packet:", data_packet.hex())
    
    # Simulate receiving command packet
    # Here we would normally receive data from the controller
    command_packet = struct.pack('>BBBBB', START_BYTE, 0x02, 10, 5, 0) + bytes([END_BYTE])
    print("Receiving Command Packet:", command_packet.hex())
    parse_command_packet(command_packet)
    
    # Simulate sensor data updates
    fuel_level = max(0, fuel_level - 0.1)  # Decrease fuel level
    temperature += random.uniform(-0.1, 0.1)  # Random temperature fluctuation
    
    # Wait before next iteration
    time.sleep(1)