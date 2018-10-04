import sklearn
from sklearn import preprocessing
import numpy as np
import pandas
from sklearn.feature_selection import chi2
filepath = 'bank-additional-full.csv'
col_dict = {}
classification_class=[]
f = open('bank-additional-full.csv','r')
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
		if i==20:
			classification_class.append(array[i])
le = preprocessing.LabelEncoder()
le.fit(classification_class)
classvec = le.transform(classification_class).tolist()
x=[[]]
i=0
for each in col_dict:
	le.fit(col_dict[each])
	temp=le.transform(col_dict[each]).tolist()
	x.append(temp)
x.pop(0)
x=map(list, zip(*x))
a,b=chi2(x,classvec)
attribute_names = ['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
for each in a:
	print("%s:%f"%(attribute_names.pop(0),each))


