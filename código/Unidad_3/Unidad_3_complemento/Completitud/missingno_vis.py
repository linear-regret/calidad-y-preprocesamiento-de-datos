import pandas as pd
import numpy as np
import missingno as msno
import matplotlib.pyplot as plt


# Cargar el dataset
file_path = "heart_disease_uci.csv"
df = pd.read_csv(file_path)

# Visualizar valores faltantes
msno.bar(df)
plt.show()

msno.matrix(df)
plt.show()