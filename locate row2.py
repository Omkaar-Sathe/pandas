
import pandas as pd

data={
"om":[400,500,600],
"nikhil":[50,40,20]

}
#load data into a dataframe object
df=pd.DataFrame(data)
print(df.loc[[0,1]])