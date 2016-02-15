# hirespicar

This is the code required to control a RC car over the internet, provided you connected the engines to a Raspberry Pi which is in turn connected to the internet.

## Installation

Clone the code to your Pi and run `install.sh`.

Edit your wpa-supplicant (`/etc/wpa_supplicant/wpa_supplicant.conf`) file so that the Wifi dongle will connect to your network immediately upon startup.

```
network={
        ssid="yolo"
        psk="h0h0h0h0ctopus"
        key_mgmt=WPA-PSK
}
```

Add the following to your crontab file:

```
@reboot sudo python /path/to/car_main.py > /path/to/car_log.txt
```
