import pandas as pd
import numpy as np

# Crear un DataFrame con valores faltantes
data = {'Nombre': ['Ana', 'Luis', 'Maria', np.nan], 'Edad': [25, np.nan, 30, 22]}
df = pd.DataFrame(data)

# Contar valores faltantes por columna
print(df.isnull())
print(df.isnull().sum())