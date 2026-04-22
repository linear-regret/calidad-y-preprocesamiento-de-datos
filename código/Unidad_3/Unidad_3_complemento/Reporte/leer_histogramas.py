
import pandas as pd
import matplotlib.pyplot as plt

data = {
     "length": [1.5, 0.5, 1.2, 0.9, 3],
     "width": [0.7, 0.2, 0.15, 0.2, 1.1],
 }
index = ["pig", "rabbit", "duck", "chicken", "horse"]
df = pd.DataFrame(data, index=index)
print(df)
hist = df.hist(bins=3)
plt.show()