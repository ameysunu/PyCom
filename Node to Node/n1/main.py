from network import LoRa
import socket
import time

# Please pick the region that matches where you are using the device

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
i = 0
while True:
    s.send('Hi, This is Node 1')
    print(s.recv(64))
    i= i+1
    time.sleep(5)
