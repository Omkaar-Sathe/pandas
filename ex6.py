import pandas as pd

df=pd.read_csv('fitness_data.csv')

x=df["Calories"].median()

df.fillna({"Calories":x},inplace=True)

print(df)