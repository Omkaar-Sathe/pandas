
import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('data (4).csv')

df["Duration"].plot(kind = 'hist')

plt.show()
