#include <stdio.h>
#include "firePacket.h"

int main() {
    DataPacket data_packet;
    CommandPacket command_packet;
    HeartbeatPacket heartbeat_packet;
    
    // Construct Data Packet
    construct_data_packet(&data_packet, 120, 130, 80, 2500);
    printf("Data Packet: ");
    for (int i = 0; i < sizeof(data_packet); i++) {
        printf("%02X ", ((uint8_t*)&data_packet)[i]);
    }
    printf("\n");
    
    // Construct Command Packet
    construct_command_packet(&command_packet, 10, 5);
    printf("Command Packet: ");
    for (int i = 0; i < sizeof(command_packet); i++) {
        printf("%02X ", ((uint8_t*)&command_packet)[i]);
    }
    printf("\n");
    
    // Construct Heartbeat Packet
    construct_heartbeat_packet(&heartbeat_packet);
    printf("Heartbeat Packet: ");
    for (int i = 0; i < sizeof(heartbeat_packet); i++) {
        printf("%02X ", ((uint8_t*)&heartbeat_packet)[i]);
    }
    printf("\n");
    
    // Simulate receiving a command packet and parsing it
    uint8_t received_command_packet[] = {START_BYTE, COMMAND_PACKET, 10, 5, 0x00, END_BYTE};
    received_command_packet[4] = calculate_checksum(received_command_packet, sizeof(received_command_packet) - 2);
    
    if (parse_command_packet(received_command_packet, sizeof(received_command_packet), &command_packet) == 0) {
        printf("Parsed Command Packet: Forward/Backward: %d, Left/Right: %d\n", command_packet.forward_backward, command_packet.left_right);
    } else {
        printf("Invalid Command Packet\n");
    }
    
    return 0;
}
