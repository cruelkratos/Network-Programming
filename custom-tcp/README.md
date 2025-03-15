# TCP Over UDP Implementation

A lightweight implementation of TCP-like reliability features built on top of UDP sockets. This project demonstrates fundamental networking concepts by implementing reliable data transfer mechanisms over an unreliable protocol.

## Features

- **Reliable Data Transfer**: Ensures all packets are delivered successfully despite UDP's unreliable nature
- **Packet Sequencing**: Assigns sequence numbers to track packet order
- **Acknowledgment System**: Confirms packet receipt through ACK messages
- **Packet Retransmission**: Automatically resends unacknowledged packets
- **Out-of-Order Handling**: Correctly reassembles messages regardless of arrival order
- **Timeout Mechanism**: Detects lost packets and triggers retransmission

## Components

### TCPSender

Responsible for:
- Breaking messages into smaller chunks (512 bytes)
- Assigning sequence numbers to packets
- Sending packets to the receiver
- Storing unacknowledged packets for potential retransmission
- Monitoring for acknowledgments
- Handling timeouts and retransmitting as needed

### TCPReceiver

Responsible for:
- Receiving incoming packets
- Storing packets in the correct order
- Sending acknowledgments back to the sender
- Reassembling the complete message

## Packet Structure

Each packet consists of:
- **Header**:
  - Sequence Number (4 bytes): Identifies the packet's position in the sequence
  - Acknowledgment Number (4 bytes): Used in ACK packets
  - Flags (1 byte): Indicates special packets (e.g., end of transmission)
- **Data**: The actual payload

## Usage Example

### Receiver
```python
from tcp_over_udp import TCPReceiver

HOST = '127.0.0.1'
PORT = 12345

# Initialize receiver
receiver = TCPReceiver(HOST, PORT)

# Receive message
receiver.receive()

# Reassemble and display message
message = b''.join([receiver.buff[i] for i in sorted(receiver.buff.keys())])
print("Received message:", message.decode())
```

### Sender
```python
from tcp_over_udp import TCPSender

HOST = '127.0.0.1'
PORT = 12345

# Initialize sender
sender = TCPSender(HOST, PORT)

# Send message
sender.send(b"Hello, world!", (HOST, PORT))

# Wait for acknowledgments
sender.wait_for_ack((HOST, PORT))
```

## Future Improvements

- **Flow Control**: Adjust transmission rate based on network conditions
- **Dynamic Window Size**: Optimize buffer management based on network performance
- **Variable Chunk Size**: Currently fixed at 512 bytes
- **Code Refactoring**: Improve structure and readability
- **Connection Setup/Teardown**: Implement proper handshake and connection termination
- **Congestion Control**: Detect and adapt to network congestion

## Requirements

- Python 3.6+
- Standard library modules only (socket, struct, time, os)

## Notes

This implementation is educational and demonstrates core networking concepts. It is not intended for production use where established TCP implementations would be more appropriate.
