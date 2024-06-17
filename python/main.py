import paket as pk
import struct
import time
import random

# Constants
START_BYTE = 0xAA
DATA_PACKET = 0x01
END_BYTE = 0x55

# Simulated robot state
left_motor_speed = 1000
right_motor_speed = 950
fuel_level = 100  # 100%
temperature = 25.4  # Celsius

	# Simulate sending data packets and heartbeat
while True:
    # Simulate sending data packet
    data_packet = pk.construct_data_packet(left_motor_speed,right_motor_speed,fuel_level,temperature)
    print("Sending Data Packet:", data_packet.hex())
	
    temperature_int = int(temperature * 100)
    fl_int = int(fuel_level)
    command_packet = struct.pack('>BBHHBHB', START_BYTE, DATA_PACKET, left_motor_speed, right_motor_speed, fl_int, temperature_int,0)
	# Add checksum
    checksum = sum(command_packet) & 0xFF
    command_packet = command_packet[:-1] + bytes([checksum]) + bytes([END_BYTE])
    print("Receiving Command Packet:", command_packet.hex())
    pk.parse_command_packet(command_packet)

    # Simulate receiving command packet
    # Here we would normally receive data from the controller
    command_packet = struct.pack('>BBBBB', START_BYTE, 0x02, 10, 5, 0) + bytes([END_BYTE])

    
    # Simulate sensor data updates
    fuel_level = max(0, fuel_level - 0.1)  # Decrease fuel level
    temperature += random.uniform(-0.1, 0.1)  # Random temperature fluctuation
    print("fuel level: ", fuel_level)
    print("temperature: ", temperature)
    
    # Wait before next iteration
    time.sleep(1)