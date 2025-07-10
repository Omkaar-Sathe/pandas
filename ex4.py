
import pandas as pd

df=pd.read_csv('fitness_data.csv')

df.fillna({"Calories":130},inplace=True)

print(df)