import sys
import subprocess
import os
from decouple import config

IP_NETWORK = "192.168.1.1"
IP_DEVICE  = "192.168.1.2"


variable_count = 0
proc = subprocess.Popen(["ping", IP_DEVICE], stdout=subprocess.PIPE)
while True:
	line = proc.stdout.readline()
	if not line:
		break
	connected_ip = line.decode('utf-8').split()[3]
	print(connected_ip)
	if "192.168.1.2:" in connected_ip:
		if variable_count == 0:
			os.system("espeak 'Father has just came'")
			variable_count += 1
