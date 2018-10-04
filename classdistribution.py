import matplotlib.pyplot as mpl; mpl.rcdefaults()
import numpy as np
import csv,sys,argparse
yes_count=0
no_count=0
with open('bank-additional-full.csv','rt') as inputfile:
	for line in inputfile.readlines():
		array = line.split(';')
		item = str(array[20])
		print(item)
		if item == '"yes"\n':
			yes_count+=1
		elif item == '"no"\n':
			no_count+=1
print(yes_count)
print(no_count)
objects=('Yes','No')
y_pos = np.arange(len(objects))
performance = (yes_count,no_count)
mpl.bar(y_pos,performance,align='center',alpha=0.5)
mpl.xticks(y_pos,objects)
mpl.ylabel('Frequency')
mpl.title('Data distribution of Class attribute')
mpl.show()
