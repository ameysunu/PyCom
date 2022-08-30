from network import LoRa
import socket
import time

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868, tx_iq=True)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

i = 0
s.setblocking(True)

breakOut = True

while breakOut:
    # send some data
    message = 'Node A: Hello ' + str(i)
    print(message)
    s.send(message)
    i = i + 1
    if i == 1000:
        breakOut = False
    time.sleep(0.1)
