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

#Py0272e61

py = Pysense()
si = SI7006A20(py)

start_time = time.time()

#(time awake * current awake + time sleeping * current sleeping) / (time awake + time sleeping)
time_awake = time.time() - start_time
current_awake = time.time()
time_sleeping = 10
current_sleeping = 10

power_consumption = (time_awake * current_awake + time_sleeping * current_sleeping) / (time_awake + time_sleeping)

# Please pick the region that matches where you are using the device

temp = str(si.temperature())
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868, sf=7)

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
i = 0
nvs_obj = Nvs(',', 512) # Initialize the buffer to write to LoPy's flash

devEUI = ubinascii.hexlify(lora.mac()).upper().decode('utf-8')
sendMessage = True

# SNCF  --> attach the device EUI while sending the message. if device EUI exists in the list then do not send the data to the device EUI.

deviceList = []

while sendMessage:
    # s.send('Hi this is Node 1. My temperature is ' + temp)
    # nvs_obj.store(s.recv(64).decode('utf-8'))
    buf = nvs_obj.read_all()
    deviceList.append(devEUI);
    print(deviceList)

    if devEUI == '70B3D54991C35D8D':
        print(s.recv(64))
        # nvs_obj.store(s.recv(64).decode('utf-8'))
        print('Data saved to LoPy: {}'.format(buf))
        s.send('Message Recieved')

        if s.recv(64) == b'Acknowledged':
            print("--- %s seconds ---" % (time.time() - start_time))
            print("%s uA" % power_consumption)
            sendMessage = False

    else:
        s.send(s.recv(64))
    i= i+1
    time.sleep(5)
