#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:
import pandas as pd

import plotly.offline as pyo
import plotly.graph_objs as go 



# create a DataFrame from the .csv file:

df= pd.DataFrame(pd.read_csv('Data/mocksurvey.csv'))
print(df)
print(df.columns)
# create traces using a list comprehension:
question = [df['Unnamed: 0']]
for q in question: 
    trace1= go.Bar(x= q, y=df['Strongly Disagree'], name='Strongly disagree')
    trace2= go.Bar(x= q, y=df['Somewhat Disagree'], name='somewhat disagree')
    trace3= go.Bar(x= q, y=df['Neutral'], name='neutral')
    trace4= go.Bar(x= q, y=df['Somewhat Agree'],name='somewhat agree')
    trace5= go.Bar(x= q, y=df['Strongly Agree'], name='strongly agree')
    
data= [trace1, trace2, trace3, trace4, trace5]
layout= go.Layout(title='survey', barmode='stack')
fig= go.Figure(data=data, layout=layout)

pyo.plot(fig)






# create a layout, remember to set the barmode here





# create a fig from data & layout, and plot the fig.
