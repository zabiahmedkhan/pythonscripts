#!/usr/bin/python
import collections, re

apphour=[]

with open("log") as f:
	lines=f.readlines()

for line in lines:
	apphour.append(re.findall(r"[\w]+",line)[2] + "th hour has app " + re.findall(r"[\w]+",line)[6] + " coming")

result_dict=collections.Counter(apphour)

for result in result_dict:
	print result + " " + str(result_dict[result]) + " times"