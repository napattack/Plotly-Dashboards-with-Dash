#######
# Objective: Create a scatterplot of 1000 random data points.
# x-axis values should come from a normal distribution using
# np.random.randn(1000)
# y-axis values should come from a uniform distribution over [0,1) using
# np.random.rand(1000)
######

# Perform imports here:

import numpy as np 
import plotly.offline as pyo
import plotly.graph_objs as go


# Define a data variable
x_axis = np.random.randn(1000)
y_axis = np.random.rand(1000)





# Define the layout

data= [go.Scatter(
    x=x_axis, 
    y=y_axis, 
    mode='markers'

)]
layout = go.Layout(
   title= 'Random Data Scatterplot',
   yaxis= dict(title= 'Uniform distribution'),
   xaxis= dict(title= 'Normal distribution'), 
   hovermode ='closest'
   )
fig= go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='firstry.html')



# Create a fig from data and layout, and plot the fig
