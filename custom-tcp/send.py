from defs import *

large_data = "Hello, world! " * 150
sender = TCPSender(HOST,PORT)
sender.send(b"hello world",(HOST,PORT))
sender.wait_for_ack((HOST,PORT))
