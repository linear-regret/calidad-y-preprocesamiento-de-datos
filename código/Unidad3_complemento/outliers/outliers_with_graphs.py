import numpy as np
import matplotlib.pyplot as plt

# Generamos datos con algunos outliers
np.random.seed(42)
datos = np.append(np.random.normal(50, 10, 100), [120, 130, 140])

# Graficamos el histograma
plt.hist(datos, bins=15, edgecolor='black')
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.title("Histograma de Datos")
plt.show()

plt.boxplot(datos, vert=False)
plt.xlabel("Valor")
plt.title("Boxplot de Datos")
plt.show()