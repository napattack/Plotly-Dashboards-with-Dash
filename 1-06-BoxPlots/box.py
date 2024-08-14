import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go 

y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

#data = [go.Box(y=y, boxpoints= 'all', jitter = 0.3, pointpos=0)]
data = [go.Box(y=y, boxpoints= 'outliers')]
pyo.plot(data)

#jitter to make the point more spread over each other 

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data1= [go.Box(y=snodgrass, name='sondgrass'), 
        go.Box(y=twain, name='twain')]
pyo.plot(data1)

