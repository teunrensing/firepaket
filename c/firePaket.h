#ifndef FIREPACKET_H
#define FIREPACKET_H

#include <stdint.h>
#include <stddef.h>

// Constants
#define START_BYTE 0xAA
#define END_BYTE 0x55

// Packet Types
#define DATA_PACKET 0x01
#define COMMAND_PACKET 0x02
#define HEARTBEAT_PACKET 0x03

// Data Packet Structure
typedef struct {
    uint8_t start_byte;
    uint8_t data_type;
    uint16_t left_motor_speed;
    uint16_t right_motor_speed;
    uint8_t fuel_level;
    uint16_t temperature;
    uint8_t checksum;
    uint8_t end_byte;
} DataPacket;

// Command Packet Structure
typedef struct {
    uint8_t start_byte;
    uint8_t data_type;
    int8_t forward_backward;
    int8_t left_right;
    uint8_t checksum;
    uint8_t end_byte;
} CommandPacket;

// Heartbeat Packet Structure
typedef struct {
    uint8_t start_byte;
    uint8_t data_type;
    uint8_t checksum;
    uint8_t end_byte;
} HeartbeatPacket;

// Function Prototypes
uint8_t calculate_checksum(uint8_t* data, size_t length);
void construct_data_packet(DataPacket* packet, uint16_t left_motor_speed, uint16_t right_motor_speed, uint8_t fuel_level, uint16_t temperature);
void construct_command_packet(CommandPacket* packet, int8_t forward_backward, int8_t left_right);
void construct_heartbeat_packet(HeartbeatPacket* packet);
int parse_command_packet(uint8_t* data, size_t length, CommandPacket* packet);

#endif // FIREPACKET_H
