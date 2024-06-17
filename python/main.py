import struct
import time
import random
import serial
import paket as pk  # Assuming 'paket' is the module containing packet functions

# Constants
START_BYTE = 0xAA
DATA_PACKET = 0x01
COMMAND_PACKET = 0x02
END_BYTE = 0x55

# Serial port setup (adjust 'COM3' to your port)
ser = serial.Serial('COM3', 9600, timeout=1)

# Simulated robot state
speed = 950
fuel_level = 100  # 100%
temperature = 25.4  # Celsius

def send_packet(packet):
    ser.write(packet)

def receive_packet():
    packet = ser.read(7)  # Adjust the packet length if needed
    return packet

while True:
    # Simulate sending data packet
    data_packet = pk.construct_data_packet(speed, speed, fuel_level, temperature)
    print("Sending Data Packet:", data_packet.hex())
    send_packet(data_packet)

    # Simulate receiving command packet
    received_packet = receive_packet()
    if received_packet:
        print("Received Packet:", received_packet.hex())
        forward_backward, left_right = pk.parse_command_packet(received_packet)
        if forward_backward is not None and left_right is not None:
            # Update robot state based on received command
            speed = forward_backward
            print(f"Updated speed: {speed}, turning: {left_right}")

    # Simulate sensor data updates
    fuel_level = max(0, fuel_level - 0.1)  # Decrease fuel level
    temperature += random.uniform(-0.1, 0.1)  # Random temperature fluctuation
    print("Fuel level: ", fuel_level)
    print("Temperature: ", temperature)
    
    # Wait before next iteration
    time.sleep(1)
