import pandas as pd
import numpy as np


archivo = pd.read_csv("penguins.csv")

# dimensionalidad
# print(archivo.shape)

# primeros elementos
# print(archivo.head())

# descripción de los datos del csv
# print(archivo.info())

# información más estadística
# print(archivo.describe())

islas = archivo["island"]
# print(islas)


var = archivo[["island", "species"]]
# print(var)

filtro1 = archivo[(archivo["flipper_length_mm"] > 200) & (archivo["sex"] == "male")]
# print(filtro1)


archivo = archivo.drop("id", axis=1)


archivo.to_csv("archivo_modificadoPinguinos.csv", index=False)

archivo["bill_length_mm"] = archivo["bill_length_mm"].fillna(
    archivo["bill_length_mm"].mean()
)
archivo["sex"] = archivo["sex"].fillna(archivo["sex"].mode()[0])

# borrar registros
"""
archivo = archivo.drop(2)
archivo = archivo.drop([0, 1, 3])
"""

print(archivo)

# Eliminar filas con valores nulos en cualquier columna
archivo = archivo.dropna()

# Eliminar filas con valores nulos solo en columnas específicas
archivo = archivo.dropna(subset=["sex", "island"])

# crear columnas nuevas
archivo["body_mass_en_kg"] = archivo["body_mass_g"] / 1000
archivo["gordito"] = np.where(archivo["body_mass_g"] > 4000, "1", "0")


dummies = pd.get_dummies(archivo["island"])

archivo = pd.concat([archivo.drop("island", axis=1), dummies], axis=1)
print(archivo.head())


print(archivo)
