from network import LoRa
import ubinascii

lora = LoRa(mode=LoRa.LORAWAN)
print('Device EUI:' + ubinascii.hexlify(lora.mac()).upper().decode('utf-8'))
