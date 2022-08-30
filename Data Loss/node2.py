from network import LoRa
import socket
import time

lora = LoRa(mode=LoRa.LORA, rx_iq=True, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(True)

print('Start')
print(lora.stats())
while True:
    data = s.recv(64)
    if (len(data) > 0):
        print(data)
