import pandas as pd
data = {'ID': [1, 2, 2, 3, 5, 9], 'Nombre': ['Ana', 'Luis', 'Luis', 'Maria', 'Pablo', 'Pablo']}
df = pd.DataFrame(data)
# Detección de duplicados

print("Primeras filas del dataset:")
print(df.head(10))

#Detección exacta de duplicados
duplicados = df.duplicated().sum()
print(f"\nNúmero de duplicados exactos: {duplicados}")


#Detección parcial de duplicados
duplicados_parciales = df.duplicated(subset=['Nombre']).sum()
print(f"\nNúmero de duplicados parciales por el campo nombre: {duplicados_parciales}")

##df_sin_duplicados = df.drop_duplicates(subset=['Nombre'])
##print(df_sin_duplicados)


##df_sin_duplicados = df.drop_duplicates()
##print(df_sin_duplicados)