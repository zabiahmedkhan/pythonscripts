#!/usr/bin/python
import requests

website=raw_input("Enter the website you want to get response code from")
r = requests.get(website)
x=r.status_code
if x==200:
	print "OK"
else:
	print "Bad"
