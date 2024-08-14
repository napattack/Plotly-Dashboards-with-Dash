#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

import plotly.offline as pyo
import plotly.graph_objs as go 
import pandas as pd

df=pd.read_csv('Data/mpg.csv')
print(df)



# create a DataFrame from the .csv file:


# create data by choosing fields for x, y and marker size attributes

data = [
    go.Scatter(
        x=df['weight'], 
        y=df['displacement'], 
        mode='markers', 
        marker=dict(
            size= df['model_year']/5,
            color= df['origin'],
            showscale= True
        )

    )
]
layout= go.Layout(
    title='mybubble'
)

fig= go.Figure(
    data, layout
)

pyo.plot(fig)





# create a layout with a title and axis labels







# create a fig from data & layout, and plot the fig
