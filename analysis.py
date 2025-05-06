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

# output the summary into a single text file

summary = df.describe() # should give me the contents of the dataset

# turns out it doesn't load the classes
class_count = df['class'].value_counts()

# open file
with open("summary.txt", "w") as file: # w is to write in the file
    file.write("Summary of the Iris Dataset\n")
    file.write(summary.to_string()) # convert dataframe to string
    file.write("\n\n") # creates space in text file
    file.write("Class Distribution:\n")
    file.write(class_count.to_string()) # success - everything is displayed


