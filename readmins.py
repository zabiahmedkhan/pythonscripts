#!/usr/bin/python

with open("/var/tmp/zabi.log", "r") as f:
     reading=f.readlines()


for h in range(23):
	if len(str(h))==1:
		h="0"+str(h)
	for m in range(60):
		if len(str(m))==1:
			m="0"+str(m)
		z=str(h)+":"+str(m)
		#print "z value : %s" %z
		count = 0
		for line in reading:
			#print "each line : %s" %line

			if z in line:
				count = count + 1
		print "%s is counted so many times %s times" % (z,count) 
			