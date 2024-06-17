---

# RC Caterpillar Fire Extinguisher Robot Packet Handling Library

This library provides functionalities to construct and deconstruct packets for communication within an RC caterpillar fire extinguisher robot system. It includes packet structures for data transmission, command execution, and system heartbeat monitoring.

## Features

- **DataPacket**: Structure for transmitting motor speeds, fuel level, and temperature data.
- **CommandPacket**: Structure for sending commands to control robot movements.
- **HeartbeatPacket**: Structure for monitoring the operational status of the robot.
- **Checksum Calculation**: Function to compute checksums for data integrity.

## Packet Structures

### DataPacket Structure

```c
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
```

### CommandPacket Structure

```c
typedef struct {
    uint8_t start_byte;
    uint8_t data_type;
    int8_t forward_backward;
    int8_t left_right;
    uint8_t checksum;
    uint8_t end_byte;
} CommandPacket;
```

### HeartbeatPacket Structure

```c
typedef struct {
    uint8_t start_byte;
    uint8_t data_type;
    uint8_t checksum;
    uint8_t end_byte;
} HeartbeatPacket;
```

## Functions Provided

- **calculate_checksum**: Calculates checksum for a given data array.
- **construct_data_packet**: Constructs a DataPacket with specified parameters.
- **construct_command_packet**: Constructs a CommandPacket with specified parameters.
- **construct_heartbeat_packet**: Constructs a HeartbeatPacket.
- **parse_command_packet**: Parses a received CommandPacket and validates checksum.

## Example Usage

Below is an example demonstrating the usage of the provided functions:

```c
#include <stdio.h>
#include "packet.h"

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
```

## Getting Started

1. **Include Header**: Include `packet.h` in your C file.
2. **Construct Packets**: Use `construct_data_packet`, `construct_command_packet`, and `construct_heartbeat_packet` functions to build packets.
3. **Parse Packets**: Use `parse_command_packet` to validate and extract data from received command packets.

## License

This library is licensed under the GPL-3.0 license. See `LICENSE` for more information.

---

Save this content in a file named `README.md` in the root directory of your project. This README file provides a comprehensive overview of your C packet handling library, its structures, functions, usage instructions, and an example to help users get started quickly with integrating and using the library in their projects.