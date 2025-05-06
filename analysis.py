# analysis.py
# a program intended to investigate and summarise the Iris dataset
# author: Dave Byrne :)

# import necessary libraries
import pandas as pd 
import numpy as np 
import sklearn as skl 
import matplotlib.pyplot as plt 
import seaborn as sns

# load dataset
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df = pd.read_csv('data/iris.data', header=None, names=column_names)

# checking if it works

print("First 5 rows of the data set:")
print(df.head())

print("\nLast 5 rows of the data set:")
print(df.tail()) # it works!


