#!/usr/bin/python
#with open(r"TCMG412Lab3.txt", 'r') as fp:
#	lines = len(fp.readlines())
#	print('Total Number of lines:', lines)

#from cgitb import lookup
#import re


#for search_name in ['Oct', 'Sep', 'Aug', 'Jul', 'Jun', 'May']:
 ##print(f"Search Result for {search_name}")
  #if found:
   # name = found
   # print(f"Name: {name}")
 # else:
  #  print(f"{search_name} not found")

 # print("")

file = open('TCMG412Lab3.txt','r')

#word1 = 'Oct'
#word2 = 'Sep'
#combined = word1 and word2

words = ["Oct", "Sep"]
count=0
lines=file.readlines()
for line in lines:
    if any(word in line for word in words):
        count+=1 
print(count)