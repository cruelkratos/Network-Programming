import socket
import os
import time
import struct
HOST = '127.0.0.1'
PORT = 12345
# socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# socket.bind((HOST, PORT))

PACKET_FORMAT = "!IIB"
HEADER_SIZE = struct.calcsize(PACKET_FORMAT)

def create_packet(seq_num, ack_num, flags, data):
    return struct.pack(PACKET_FORMAT, seq_num, ack_num, flags) + data

def unpack_packet(packet):
    header = packet[:HEADER_SIZE]
    seq_num, ack_num, flags = struct.unpack(PACKET_FORMAT, header)
    data = packet[HEADER_SIZE:]
    return seq_num, ack_num, flags, data

class TCPSender:
  def __init__(self,host,port):
    self.host = host
    self.port = port
    self.buffer = {}
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # self.socket.bind((self.host, self.port))
    self.sequence_number = 0
    self.timeout = 2.1
  def send(self,message,client_address): #assume already byte sized
    print("Sending message")
    for i in range (0,len(message),512):
      chunk = create_packet(self.sequence_number,0,0,message[i:i+512])
      self.socket.sendto(chunk,client_address)
      self.buffer[self.sequence_number] = chunk
      self.sequence_number += 1
    self.socket.sendto(create_packet(self.sequence_number,0,1,b''),client_address)
    self.buffer[self.sequence_number] = create_packet(self.sequence_number,0,1,b'')
  def wait_for_ack(self,client_address):
     while self.buffer:
        try:
           self.socket.settimeout(self.timeout)
           ACK , addr = self.socket.recvfrom(1024)
           ack_num = unpack_packet(ACK)[1]
           if ack_num in self.buffer:
            del self.buffer[ack_num]
           print(f"Received ACK {ack_num}")
        except socket.timeout:
           print("Timeout")
           for a,b in self.buffer.items():
              self.socket.sendto(b,client_address)
                       
large_data = "Hello, world! " * 150
sender = TCPSender(HOST,PORT)
sender.send(b"hello world",(HOST,PORT))
sender.wait_for_ack((HOST,PORT))

