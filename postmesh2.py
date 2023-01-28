# Python script based on a PHP script sent to me from N2MH
# Reads contents of 'readme.txt' and posts to MeshChat
# Edit callsign, channel, MeshChat_IP and name of textfile as required
# K1YMI 27/1/2023
#
import requests
import time

from pathlib import Path
txt = Path('<TEXTFILE>.txt').read_text()

payload = {'action': 'send_message',
           'message': txt,
           'call_sign': '<YourCallsign>',
           'epoch': int(time.time()),
           'channel': 'test'}

url = "http://<MeshChat_IP>/cgi-bin/meshchat"

response = requests.post(url, data=payload)

print(response.text)
