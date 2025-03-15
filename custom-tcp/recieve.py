import socket
import os
import time
import struct
PACKET_FORMAT = "!IIB"
HEADER_SIZE = struct.calcsize(PACKET_FORMAT)
def create_packet(seq_num, ack_num, flags, data):
    return struct.pack(PACKET_FORMAT, seq_num, ack_num, flags) + data

def unpack_packet(packet):
    header = packet[:HEADER_SIZE]
    seq_num, ack_num, flags = struct.unpack(PACKET_FORMAT, header)
    data = packet[HEADER_SIZE:]
    return seq_num, ack_num, flags, data
class TCPReceiver:
   def __init__(self,host,port):
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      self.socket.bind((host,port))
      self.R = 1000000000000
      self.buff = {}
   def receive(self):
      print("Receiving message")
      while True:
         chunk , addr = self.socket.recvfrom(1024)
        #  print(chunk)
         seq_num, ack_num, flags, data = unpack_packet(chunk)  
         if flags == 1 and seq_num-self.R == len(self.buff):
            self.socket.sendto(create_packet(0,seq_num,0,b''),addr)
            break
         self.R = min(self.R,seq_num)
         # print(f"recived data: {data.decode()}")
         self.socket.sendto(create_packet(0,seq_num,0,b''),addr)
         self.buff[seq_num] = data

HOST = '127.0.0.1'
PORT = 12345
rec = TCPReceiver(HOST,PORT)
rec.receive()
message = b''.join([rec.buff[i] for i in sorted(rec.buff.keys())])
print("Final received message:")
print(message.decode())