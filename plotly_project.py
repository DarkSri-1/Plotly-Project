# Import necessary libraries
import pandas as pd
import plotly.express as px

# Step 1: Download the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_data = pd.read_csv(url, header=None, names=column_names)

# Save the dataset to a CSV file
iris_data.to_csv('iris_dataset.csv', index=False)

# Step 2: Load the dataset
data = pd.read_csv('iris_dataset.csv')
print("Dataset loaded successfully:")
print(data.head())

# Step 3: Create Various Plots

# Bar Plot
fig_bar = px.bar(data, x='species', y='sepal_length', title='Average Sepal Length by Species')
fig_bar.show()

# Line Plot
fig_line = px.line(data, x='sepal_length', y='sepal_width', color='species', title='Sepal Length vs Sepal Width')
fig_line.show()

# Scatter Plot
fig_scatter = px.scatter(data, x='petal_length', y='petal_width', color='species', title='Petal Length vs Petal Width')
fig_scatter.show()

# Histogram
fig_histogram = px.histogram(data, x='sepal_length', color='species', title='Distribution of Sepal Length')
fig_histogram.show()

# Box Plot
fig_box = px.box(data, x='species', y='petal_length', title='Box Plot of Petal Length by Species')
fig_box.show()

# Violin Plot
fig_violin = px.violin(data, y='petal_length', x='species', box=True, points='all', title='Violin Plot of Petal Length by Species')
fig_violin.show()