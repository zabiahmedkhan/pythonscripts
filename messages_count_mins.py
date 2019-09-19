#!/usr/bin/python
import collections, re

apphour=[]

with open("log") as f:
	lines=f.readlines()

for line in lines:
	apphour.append(re.findall(r"[\w]+",line)[2] + "th hour and "+ re.findall("[\w]+",line)[3] + "th minute " + re.findall(r"[\w]+",line)[6] + " coming")

print apphour
result_dict=collections.Counter(apphour)
print result_dict

for result in result_dict:
	print result + " " + str(result_dict[result]) + " times"
