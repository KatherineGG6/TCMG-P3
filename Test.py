#!/usr/bin/python
with open(r"TCMG412Lab3.txt", 'r') as fp:
	lines = len(fp.readlines())
	print('Total Number of lines:', lines)

from cgitb import lookup
import re


for search_name in ['Oct', 'Sep', 'Aug', 'Jul', 'Jun', 'May']:
  found = lookup('TCMG412Lab3.txt', search_name)
  print(f"Search Result for {search_name}")
  if found:
    name = found
    print(f"Name: {name}")
  else:
    print(f"{search_name} not found")

  print("")