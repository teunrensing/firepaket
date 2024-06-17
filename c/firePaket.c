#include "firePacket.h"
#include <string.h>

// Function to calculate checksum
uint8_t calculate_checksum(uint8_t* data, size_t length) {
    uint8_t checksum = 0;
    for (size_t i = 0; i < length; i++) {
        checksum ^= data[i];
    }
    return checksum;
}

// Function to construct data packet
void construct_data_packet(DataPacket* packet, uint16_t left_motor_speed, uint16_t right_motor_speed, uint8_t fuel_level, uint16_t temperature) {
    packet->start_byte = START_BYTE;
    packet->data_type = DATA_PACKET;
    packet->left_motor_speed = left_motor_speed;
    packet->right_motor_speed = right_motor_speed;
    packet->fuel_level = fuel_level;
    packet->temperature = temperature;
    packet->checksum = calculate_checksum((uint8_t*)packet, sizeof(DataPacket) - 2);
    packet->end_byte = END_BYTE;
}

// Function to construct command packet
void construct_command_packet(CommandPacket* packet, int8_t forward_backward, int8_t left_right) {
    packet->start_byte = START_BYTE;
    packet->data_type = COMMAND_PACKET;
    packet->forward_backward = forward_backward;
    packet->left_right = left_right;
    packet->checksum = calculate_checksum((uint8_t*)packet, sizeof(CommandPacket) - 2);
    packet->end_byte = END_BYTE;
}

// Function to construct heartbeat packet
void construct_heartbeat_packet(HeartbeatPacket* packet) {
    packet->start_byte = START_BYTE;
    packet->data_type = HEARTBEAT_PACKET;
    packet->checksum = calculate_checksum((uint8_t*)packet, sizeof(HeartbeatPacket) - 2);
    packet->end_byte = END_BYTE;
}

// Function to parse command packet
int parse_command_packet(uint8_t* data, size_t length, CommandPacket* packet) {
    if (length != sizeof(CommandPacket) || data[0] != START_BYTE || data[length - 1] != END_BYTE) {
        return -1; // Invalid packet
    }
    
    memcpy(packet, data, sizeof(CommandPacket));
    uint8_t calculated_checksum = calculate_checksum(data, sizeof(CommandPacket) - 2);
    if (calculated_checksum != packet->checksum) {
        return -1; // Checksum mismatch
    }
    
    return 0; // Valid packet
}
