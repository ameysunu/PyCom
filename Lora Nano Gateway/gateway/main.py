from pycom import heartbeat
heartbeat(False)
print ("Heartbeat off")


import utime
from machine import RTC
rtc = RTC()
rtc.ntp_sync("pool.ntp.org")
utime.sleep_ms(750)
t = rtc.now()
with open("bootlog.txt", "a") as f:
   f.write(repr(utime.time()) + " " + repr(t) + "\n")

def reload(mod):
    import sys
    mod_name = mod.__name__
    del sys.modules[mod_name]
    return __import__(mod_name)

from machine import reset

""" LoPy LoRaWAN Nano Gateway example usage """

import config
from nanogateway import NanoGateway

if True: #__name__ == '__main__':
    nanogw = NanoGateway(
        id=config.GATEWAY_ID,
        frequency=config.LORA_FREQUENCY,
        datarate=config.LORA_GW_DR,
        ssid=config.WIFI_SSID,
        password=config.WIFI_PASS,
        server=config.SERVER,
        port=config.PORT,
        ntp_server=config.NTP,
        ntp_period=config.NTP_PERIOD_S
        )

    nanogw.start()
