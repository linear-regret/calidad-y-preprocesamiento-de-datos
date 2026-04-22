import pandas as pd
from ydata_profiling import ProfileReport

# Cargar el dataset
file_path = "heart_disease_uci.csv"
df = pd.read_csv(file_path)

# Generación de un reporte automático de perfilado de datos
profile = ProfileReport(df, title="Reporte de Perfilado de Datos - Heart Disease UCI")
profile.to_file("heart_disease_profiling_report.html")

print("\nReporte de perfilado generado: heart_disease_profiling_report.html")