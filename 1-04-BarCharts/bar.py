import plotly.offline as pyo
import plotly.graph_objs as go 
import pandas as pd

df= pd.read_csv('Data/2018WinterOlympics.csv')
#print(df)
trace1= go.Bar(x=df['NOC'], y=df['Gold'], marker=dict(color='#FFD700'), name='Gold')
trace2= go.Bar(x=df['NOC'], y=df['Silver'] , marker=dict(color='#9EA0A1'), name='Silver')
trace3= go.Bar(x=df['NOC'], y=df['Bronze'] , marker=dict(color='#CD7F32'), name='bronze')

data=[trace1, trace2, trace3]
#data = [go.Bar(x=df['NOC'],y=df['Total'])]
layout = go.Layout(title='Medals', barmode='stack')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)
