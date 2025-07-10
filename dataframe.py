
#create a dataframe from tow series:
import pandas as pd
a={
   "calories":[420,380,390],
   "duration":[50,40,45]
}

b=pd.DataFrame(a)
print(b)