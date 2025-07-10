
import pandas as pd
data={
    "om":[10,20,30],
    "nil":[1,2,3]

}

df=pd.DataFrame(data,index=["day1","day2","day3"])
print(df.loc["day2"])