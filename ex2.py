#remove all rows with null values:
import pandas as pd
df=pd.read_csv('fitness_data.csv')
df.dropna(inplace=True)
print(df.to_string())