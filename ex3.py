#replace null values with the number 130:
import pandas as pd

df = pd.read_csv('fitness_data.csv')

df.fillna(130, inplace=True)

print(df)