#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:

import pandas as pd
import plotly.offline as pyo 
import plotly.graph_objs as go 
import numpy as np


# create a DataFrame from the .csv file:
df= pd.read_csv('Data/abalone.csv')
print(df)

# take two random samples of different sizes:

ring1= np.random.choice(df['rings'], 10, replace=False)

ring2= np.random.choice(df['rings'], 10, replace=False)

data= [
    go.Box(y= ring1, boxpoints='all', pointpos=0), 
    go.Box(y= ring2, boxpoints='all', pointpos=0)
]

# create a data variable with two Box plots:

pyo.plot(data)









# add a layout




# create a fig from data & layout, and plot the fig
