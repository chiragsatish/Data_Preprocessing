f = open('bank-additional-full.csv','r')
col_dict = {}
col_names = []
for line in f:
	array = line.split(';')
	col_names.extend(array)
	break
#Get numerical attributes
for line in f:
	array = line.split(';')
	for i in range(len(array)-1):
		try: 
			float(array[i])
		except ValueError:
			continue
		if i in col_dict:
			col_dict[i].append(float(array[i]))
		else:
			col_dict[i] = [(float(array[i]))]
#Perform Normalization
print("Old Range:")
for key in col_dict:
	maxval = max(col_dict[key])
	minval = min(col_dict[key])
	print("%s:[%f,%f]"%(col_names[key],minval,maxval))
	flag=-999
	if maxval>0 and minval>=0:
		flag=1
	elif maxval<=0 and minval<0:
		flag=2
	elif maxval<0 and minval>0:
		flag=0
	if flag==0:
		templist=[]
		for each in col_dict[key]:
			if each<0:
				each=float(each)/float(minval)
				templist.append(each)
			elif each>0:
				each=float(each)/float(maxval)
				templist.append(each)
		col_dict[key]=templist
	elif flag==1:
		templist=[]
		for each in col_dict[key]:
			each=float(each)/float(maxval)
			templist.append(each)
		col_dict[key]=templist
	else:
		templist=[]
		for each in col_dict[key]:
			each=float(each)/float(minval)
			templist.append(each)
		col_dict[key]=templist
#Print normalized columns
for each in col_dict:
	print(col_names[each],len(col_dict[each]))
	print('----------------------------------')
	for item in col_dict[each]:
		print(item)
	

