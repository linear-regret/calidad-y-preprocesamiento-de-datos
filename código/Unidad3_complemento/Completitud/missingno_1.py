import pandas as pd
import numpy as np
import missingno as msno
import matplotlib.pyplot as plt

# Crear un DataFrame con valores faltantes
data = {'Nombre': ['Ana', 'Luis', 'Maria', np.nan], 'Edad': [25, np.nan, 30, 22]}
df = pd.DataFrame(data)

# Visualizar valores faltantes
msno.bar(df)
plt.show()

msno.matrix(df)
plt.show()