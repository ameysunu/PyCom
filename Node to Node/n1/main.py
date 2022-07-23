from network import LoRa
import socket
import time
import ubinascii
import struct
import machine
import uos
import pycom
import sys
from nvs import Nvs

from pysense import Pysense
from SI7006A20 import SI7006A20 # Temperature sensor

py = Pysense()
si = SI7006A20(py)

# Please pick the region that matches where you are using the device

temp = str(si.temperature())
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
i = 0
nvs_obj = Nvs(',', 512) # Initialize the buffer to write to LoPy's flash


devEUI = ubinascii.hexlify(lora.mac()).upper().decode('utf-8')
while True:
    # s.send('Hi this is Node 1. My temperature is ' + temp)
    # nvs_obj.store(s.recv(64).decode('utf-8'))
    buf = nvs_obj.read_all()
    
    print('Data read from file: {}'.format(buf))
    if devEUI == '70B3D54997DB6CCE':
        print(s.recv(64))
    else:
        s.send(s.recv(64))
    i= i+1
    time.sleep(5)
