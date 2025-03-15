from defs import *
rec = TCPReceiver(HOST,PORT)
rec.receive()
message = b''.join([rec.buff[i] for i in sorted(rec.buff.keys())])
print("Final received message:")
print(message.decode())