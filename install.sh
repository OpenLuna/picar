#!/bin/bash
apt-get update -y
apt-get upgrade -y
apt-get install -y python-dev python-pip ppp wvdial usb-modeswitch
pip install twisted autobahn
