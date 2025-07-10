
import pandas as pd

df=pd.read_csv('fitness_data.csv')

x=df["Calories"].mode()[0]

df.fillna({"Calories":x},inplace=True)

print(df)