import sklearn
from sklearn import preprocessing
import numpy as np
import pandas
from sklearn.feature_selection import mutual_info_classif
attribute_names=['age','duration','campaign','pdays','previous','emp.var.rate','cons.price.idx','cons.conf.idx','euribor3m','nr.employed']
f = open('bank-additional-full.csv','r')
col_dict = {}
col_names = []
for line in f:
	array = line.split(';')
	col_names.extend(array)
	break
#Get numerical attributes and class
classification_class=[]
for line in f:
	array = line.split(';')
	for i in range(len(array)):
		if i==20:
			classification_class.append(array[i])
		try: 
			float(array[i])
		except ValueError:
			continue
		if i in col_dict:
			col_dict[i].append(float(array[i]))
		else:
			col_dict[i] = [(float(array[i]))]
le = preprocessing.LabelEncoder()
le.fit(classification_class)
classvec = le.transform(classification_class).tolist()
x=[[]]
for each in col_dict:
	x.append(col_dict[each])
x.pop(0)
x=map(list, zip(*x))
a=mutual_info_classif(x,classvec)
for each in a:
	print("%s:%f"%(attribute_names.pop(0),each))

