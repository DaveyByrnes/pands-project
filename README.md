# pands-project

## **Introduction**

Hi there, I'm David - and you're currently reading my README.md file regarding my pands-project for 2025, centered around the Iris dataset.

I am comfortable writing markdown files because I use [Obsidian](https://obsidian.md/) as one of my primary notetaking sources, both for personal use and for use throughout this college course.

### **Project Parameters**

- [x] Research the dataset online and write a summary about it in your README.
- [x] Download the dataset and add it to your repository.
- [x] Write a program called analysis.py that:
  - [x] Outputs a summary of each variable to a single text file
  - [x] Saves a histogram of each variable to .png files
  - [x] Outputs a scatter plot of each variables
  - [x] Performs any other analysis you think is appropriate.

I will also produce a Jupyter notebook containing extra comments about the process and my code that is not mentioned here. We'll start at the beginning.

## **Research**

### **Introduction to the Iris Dataset**

The Iris dataset was created and used by Ronald Fisher, first published in 1936 in his paper [*The use of multiple measurements in taxonomic problems*](https://lgross.utk.edu/Math589Fall2020/RAFisher1936measurementsFlowerTaxa.pdf).

It was created by Fisher so that he could utilise linear discriminant analysis - a method used to find linear combinations between features of different Iris speicies. Doing this was to help Fisher identify commonanlities between the different classes an help make each feature class more distinguishable.

The dataset is now famed for its use as a case study for data analytics and computer science, with a primary source of this being this very project.

### **A Look at the Statistics**

With this being a project weighted towards an analytical view of the dataset, it is important to look at the actual dataset itself.

#### **Summary**

In `analysis.py`, I created a text file which could summarise all of the various features and classes within the dataset into [summary.text](./summary.txt).

The summary statistics are useful at a glance as it sums up most of everything I need to know about the dataset. I can see the outliers easily with the minimum and maximum, and mean and standard deviation gives me insight on where the data clustes and by how much.

However - if I was to research these features in greater depth, a brief text summary of everything isn't suitable. Getting the data in a visual form can help me identify patterns easier, as differentiating patterns from raw numbers isn't intuitive to me.

#### **The Basic Visuals**

##### **Histograms**

The first visualisation step is perhaps the most familiar to me - the histogram. I decided to generate a histogram for each feature: [sepal length](./pngs/sepal_length_distribution.png), [sepal width](./pngs/sepal_width_distribution.png), [petal length](./pngs/petal_length_distribution.png) and [petal width](./pngs/petal_width_distribution.png). These were created using the `seaborn` library.

I created these so that I could visually identify the distribution shape of each of the features. This is useful as I can see how separable and identifiable each of the species are within just one feature.

With these histograms, I can interpret the following for each of the features:

**Sepal Length:**

The separation of the species is clear - with Setosa being predominantly shorter, between 4.5 and 5.5 cm, peaking at 6.0. Versicolor is within the middle range, with slight overlap with Virginica, with the latter being the most dominant in length. This means that sepal length is okay for distinguishing Setosa as it is clearly separated, but much less useful for the other classes.

**Sepal Width:**

There is much more overlap with the sepal width - with a large cluster of all three classes between 2.5 and 3.5 cm. We can see immediately that sepal width is ineffective for discriminating between the classes - and may require better investigation alongside other features; see [scatterplots.](#scatterplots).

**Petal Length:**

Here is the clearest separation so far - with Setosa being clearly distinct with no overlap, and the latter classes having very little overlap. This will most likely be the best feature to distinguish between the species

**Petal Width:**

Observing the last of the four features, the separation here is also excellent. It seems the petal length and width seem much better suited for distinguishing the separate classes from each other. I want to create a scatterplot for the petals and the sepals to see how the features line up against each other.


##### **Scatterplots**

I created scatterplots contrasting two features against each other - [petal comparison](./pngs/petal_length_vs_petal_width.png) and [sepal comparison](./pngs/sepal_length_vs_sepal_width.png). 

The petal comparison is visually very distinct and separates the species very well. They seemed to be grouped by class with minimal overlap. It seems that the clusters are mostly linear.

The sepal comparison has much more overlap between species, particularly versicolor and virginica. Setosa remains distinct, which seems to be uniform across the dataset. The sepal comparison seems to be not as strong for separation as the petal comparison. 

##### **Box plots**

The box plots show that Setosa has a narrow range in petal length, while Versicolor and Virginica have wider ranges. I am inclined to believe that this suggests that petal length is one of the clearest features that distinguishes between species.

##### **Pairplot**

The pairplot shows the dataset in its entirity and shows me how the differt features interact and are separated. Petal length and petal width are the most clear features when it comes to distinguishing between the species, a conclusion I already came to investigating throughout the project so far.

Setosa is the easiest to separate, whereas Versicolor and Virginica are much more similiar, due to the overlaps that we can see in the pairplot.

## **Conclusion**

In my examination of the Iris dataset, a number of things became clear to me while coding the various visual graphs.

The histograms provided an early insight into the fact that the petal length and width were clearly separated - and that Setosa was easily distinguishable. Sepal length and width was less useful with the amount of overlap that was presented, but all data is useful data.

The scatterplots showed a direct relationship between paired features. Again, Setosa was the most distinct when it came to the petal comparison, with both Versicolor and Virginica having a small bit of overlap. Again, the sepal comparison had much more overlap with the latter species, making it a poorly distinguished feature.

The boxplot was my final confirmation that Setosa had the most narrow range of features - indicating that Setosa was the most reliable species to analyse were I examining this dataset in much greater detail.

The pairplot I find fitting to end the analysis as it provides an overhead view of the entire dataset into one graph, showing the interaction between the different features. Setosa, as stated before, was by far the easiest to separate and identify, whereas the other classes continued to overlap throughout the other features.


