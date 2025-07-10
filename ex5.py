
import pandas as pd

df=pd.read_csv('fitness_data.csv')

x=df["Calories"].mean()

df.fillna({"Calories":x},inplace=True)

print(df)