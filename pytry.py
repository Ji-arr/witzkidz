import pandas as pd

# Sample data
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 15, 25, 12, 18]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by 'Category' and calculate the mean for each group
grouped_data = df.groupby('Category').mean()

print(grouped_data)
