from network import LoRa
import socket
import time
import ubinascii
import struct
import machine
import uos
import pycom
import sys

from pysense import Pysense
from SI7006A20 import SI7006A20 # Temperature sensor

#Pyc237b91

py = Pysense()
si = SI7006A20(py)

# Please pick the region that matches where you are using the device

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
humidity = str(si.humidity())

# destination id: 70B3D54997DB6CCE, source id: 70B3D54995ABD672
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
devEUI = ubinascii.hexlify(lora.mac()).upper().decode('utf-8')
i = 0
while True:
    i = i+1
    if i == 8:

        start_time = time.time()
        time_awake = time.time() - start_time
        current_awake = time.time()
        time_sleeping = 10
        current_sleeping = 10

        power_consumption = (time_awake * current_awake + time_sleeping * current_sleeping) / (time_awake + time_sleeping)

        print('Node going to sleep')
        print("%s uA" % power_consumption)
        machine.deepsleep(1000)
    if s.recv(64) == b'':
        print('No message recieved')
    else:
        if devEUI == '70B3D54991C35D8D':
            print(s.recv(64))
            i = 0
        else:
            # check if data exists and then timeout closing the connection.
            print('Forwarded message successfully')
            i = 0
    # if s.recv(64) == b'Ping':
    #     s.send('Pong')
    #     print('Pong {}'.format(i))
    #     i = i+1
    time.sleep(5)
