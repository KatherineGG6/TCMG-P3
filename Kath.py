#Marketing wants to know two things: 
#How many total requests have been made in the 6 months?
#How many total requests were made in the time period represented by the log?

import requests

#downloadUrl = "https://s3.amazonaws.com/tcmg476/http_access_log"
#eq = requests.get(downloadUrl)

#response = requests.get("https://s3.amazonaws.com/tcmg476/http_access_log")

#with open(r"TCMG412Lab3.txt", 'r') as fp:
	#lines = len(fp.readlines())
	#print('Total Number of lines:', lines)

import re

file = open ("TCMG412Lab3.txt", 'r')
text = file.read()

lsm = re.findall(r'Oct', text)

print(lsm)

