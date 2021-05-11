import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv('Iris_data_sample.csv')
print(df.head(10).to_string(), '\n\n')

# Remove missing values
df = df.replace('###', np.nan)
df = df.replace('??', np.nan)
df = df.dropna()
print(df.head(10).to_string(), '\n\n')

# Group by counts of each species
df = df.groupby('Species').count()
print(df.to_string())

# Plot the count of each species
plt.bar(df.index, df['Unnamed: 0'])
plt.show()