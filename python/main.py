import packet

# Construct Data Packet
data_packet = packet.construct_data_packet(120, 130, 80, 25.00)
print("Data Packet:", data_packet)

# Construct Command Packet
command_packet = packet.construct_command_packet(10, 5)
print("Command Packet:", command_packet)

# Construct Heartbeat Packet
heartbeat_packet = packet.construct_heartbeat_packet()
print("Heartbeat Packet:", heartbeat_packet)

# Simulate receiving a command packet and parsing it
received_command_packet = bytearray([packet.START_BYTE, packet.COMMAND_PACKET, 10, 5, 0x00, packet.END_BYTE])
received_command_packet[4] = packet.calculate_checksum(received_command_packet[:-2])
print("Received Command Packet:", received_command_packet)

forward_backward, left_right = packet.parse_command_packet(received_command_packet)
if forward_backward is not None and left_right is not None:
    print(f"Parsed Command Packet: Forward/Backward: {forward_backward}, Left/Right: {left_right}")
else:
    print("Invalid Command Packet")
