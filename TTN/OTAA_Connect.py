from network import LoRa
import socket
import time
import ubinascii

# Initialize LoRa, and set region to Europe
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# Create OTAA authentication params
app_eui = ubinascii.unhexlify('0000000000000000')
app_key = ubinascii.unhexlify('FCC4C1FF241151EC6CACBA01EA14B058')

# Join network using OTAA
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# While until module has joined network
while not lora.has_joined();
    time.sleep(2.5)
    print('Waiting to join')

# Create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# Set the LoRaWAN data rate
s = setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# Wait for data to be sent and for the recieve windows to expire
s.setblocking(True)

# Send sample data
s.send(bytes([0x01, 0x02, 0x03]))

# Set non-blocking for socket, if no data received then block will be forever
s.setblocking(False)

# Get data if recieved
data = s.recv(64)
print(data)
