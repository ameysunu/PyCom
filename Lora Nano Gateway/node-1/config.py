""" LoPy LoRaWAN Nano Gateway configuration options """

import machine
import ubinascii

WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()
# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
# GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]
GATEWAY_ID = WIFI_MAC[:6] + "FFFF" + WIFI_MAC[6:12]
SERVER = 'eu1.cloud.thethings.network'
PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

WIFI_SSID = 'VM7828838'
WIFI_PASS = 'ff5fmHnpNrrx'


# for EU868
LORA_FREQUENCY = 868100000
LORA_GW_DR = "SF12BW125" # DR_5
LORA_NODE_DR = 5
