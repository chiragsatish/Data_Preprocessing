import pandas
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot
#import matplotlib.plotly as plt 

f='bank-additional-full.csv'
col_name = raw_input("Enter col name:")
dataframe = pandas.read_csv(f,';')
contactvsy = pandas.crosstab(index=dataframe[col_name],columns=dataframe["y"])
print(contactvsy)
xaxis = contactvsy.index.get_values().tolist()
contactvsy=np.array(contactvsy)
trace1 = go.Bar(
    x=xaxis,
    y=list(contactvsy[:,0]),
    name='No'
)
trace2 = go.Bar(
    x=xaxis,
    y=list(contactvsy[:,1]),
    name='Yes'
)
data = [trace1, trace2]
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
plot(fig)
