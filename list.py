#!/usr/bin/python
list1=[4,2,3,1]
list2=['four','two','three','one']
def arrangement(list):
	for j in range(len(list)):
		for i in range(len(list)):
			#print list[i]
			if i==len(list)-1:
				break
			if list[i] > list[i+1]:
	#			print "hi"
				temp=list[i]
				list[i]=list[i+1]
				list[i+1]=temp
			


#list1.sort()
#list2.sort()

#arrangement(list1)
#arrangement(list2)
#print list1
#print list2

list3=[]

for j in range(len(list2)):
	list3.append((list1[j],list2[j]))
#	print list3[j]		


arrangement(list3)
#print list3[0]

#list3.split(',')

print list3
