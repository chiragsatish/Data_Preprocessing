import sklearn
from sklearn import preprocessing
import numpy as np
f = open('bank-additional-full.csv','r')
col_dict={}
col_names = []
for line in f:
	array = line.split(';')
	col_names.extend(array)
	break
for line in f:
	array = line.split(';')
	if array[0]=='"age"':
		continue
	for i in range(len(array)):
		if i in range(1,10) or i==14:
			if i in col_dict:
				col_dict[i].append(array[i])
			else:
				col_dict[i] = [array[i]]
le = preprocessing.LabelEncoder()
for each in col_dict:
	le.fit(col_dict[each])
	temp=le.transform(col_dict[each]).tolist()
	d={}
	for ele in temp:
		if ele in d:
			d[ele]+=1
		else:
			d[ele]=1
	for i in d:
		print("%s:%d" %(le.inverse_transform([i])[0][0:],d[i]))
	print("------------------------------")
	break