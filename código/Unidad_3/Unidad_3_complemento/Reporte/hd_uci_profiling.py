import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
file_path = "heart_disease_uci.csv"
df = pd.read_csv(file_path)

# Visualizar las primeras filas del dataset
print("Primeras filas del dataset:")
print(df.head())

# Información general del dataset
print("\nInformación del dataset:")
df.info()

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe())

# Detección de valores faltantes
print("\nValores faltantes por columna:")
print(df.isnull().sum())

# Visualización de valores faltantes
msno.bar(df)
plt.show()

# Detección de duplicados
duplicados = df.duplicated().sum()
print(f"\nNúmero de registros duplicados: {duplicados}")

print(df.columns)

# Distribución de las variables numéricas
df.hist(figsize=(12, 10), bins=30)
plt.show()



# Boxplots para detectar valores atípicos
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['age', 'sex', 'dataset', 'cp', 'trestbps', 'chol', 'fbs',
       'restecg', 'thalch', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']])
#plt.xticks(rotation=90)
plt.show()



