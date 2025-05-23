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


# plot histograms of dataset
sns.histplot(data=df, x='sepal_length', hue='class', bins=10, kde=True, multiple='stack')
plt.title('Sepal Length Distribution') 
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')

# save png
plt.savefig('sepal_length_distribution.png')
plt.close() 

# create histograms for all features
for column in df.columns[:-1]: # negative indexing to exclude the last column (class)
    sns.histplot(data=df, x=column, hue='class', bins=10, kde=True, multiple='stack')
    plt.title(f'{column} Distribution')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.savefig(f'{column}_distribution.png')
    plt.close()

# create scatterplot for first pair of features
sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='class')
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.savefig('sepal_length_vs_sepal_width.png')
plt.close()

# create scatterplot for second pair
sns.scatterplot(data=df, x='petal_length', y='petal_width', hue='class')
plt.title('Petal Length vs Petal Width')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.savefig('petal_length_vs_petal_width.png')
plt.close()


# perform any other analysis I think is appropriate

# pairplot of all features

# create pairplot
plot = sns.pairplot(df, hue='class')
plot.fig.suptitle('Pairplot of Iris Dataset', y=1.02) # adjust title position
plt.savefig('pairplot.png', bbox_inches='tight') # save the figure with tight layout
plt.close()

# create boxplot
sns.boxplot(data=df, x='class', y='petal_length', hue='class')
plt.title('Boxplot of Petal Length by Class')
plt.xlabel('Class')
plt.ylabel('Petal Length (cm)')
plt.savefig('boxplot_petal_length.png')
plt.close()







