
import pandas as pd

data={
"om":[420,450,430],
"kaar":[20,30,40]

}

#load data into a dataframe object:
df=pd.DataFrame(data)
print(df.loc[0])