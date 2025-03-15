# Network Programming

An educational repository for learning and exploring network programming concepts through practical implementations (LLM generated ahh readme, ts basic networking pmo icl, so my ahh tried to make some shi)

## Overview

This repository contains my **attempts** to do some network programming

## Projects

### 1. TCP Over UDP Implementation

A custom implementation that demonstrates TCP reliability features built on top of UDP sockets. This project shows how reliable transmission can be achieved even with an unreliable underlying protocol.

**Key Features:**
- Packet sequencing and acknowledgment
- Reliable data transfer through retransmission
- Out-of-order packet handling
- Timeout detection and recovery

[View TCP Over UDP Project](./custom-tcp/)

### 2. Simple HTTP File Server

A basic HTTP server that allows browsing and downloading files from the host directory. This project demonstrates the fundamentals of the HTTP protocol and socket-based web servers.

**Key Features:**
- Directory listing via HTML interface
- File download functionality
- Basic HTTP request/response handling
- TCP socket programming

[View HTTP Server Project](./custom-http_server-fileshare/)

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/cruelkratos/network-programming.git
   cd network-programming
   ```

2. Explore the individual project directories to learn about specific implementations

3. Run the examples to see networking concepts in action:
   ```bash
   # For the HTTP server
   cd http_server
   python main.py
   
   # For the TCP over UDP implementation
   # Terminal 1 (receiver)
   cd tcp_over_udp
   python receiver.py
   
   # Terminal 2 (sender)
   cd tcp_over_udp
   python sender.py
   ```

## Future Additions

Future projects planned for this repository include:
- DNS resolver implementation
- WebSocket server and client
- Simple load balancer
- Network protocol analyzers
- Distributed systems concepts

## Learning Resources

If you're new to network programming, these resources might be helpful:

- [Computer Networking: A Top-Down Approach](https://gaia.cs.umass.edu/kurose_ross/index.php)
- [Python Socket Programming Documentation](https://docs.python.org/3/library/socket.html)

## Contributing

This is an educational repository, and contributions that add new networking concepts or improve existing implementations are welcome! (👅)
