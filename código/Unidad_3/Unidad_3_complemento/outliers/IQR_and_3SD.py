import numpy as np

# Generamos datos con algunos outliers
np.random.seed(42)
datos = np.append(np.random.normal(50, 10, 100), [120, 130, 140])
Q1 = np.percentile(datos, 25)
Q3 = np.percentile(datos, 75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = datos[(datos < limite_inferior) | (datos > limite_superior)]
print("Outliers detectados:", outliers)

media = np.mean(datos)
desviacion = np.std(datos)

outliers = datos[datos > media + 3 * desviacion]
print("Outliers detectados:", outliers)