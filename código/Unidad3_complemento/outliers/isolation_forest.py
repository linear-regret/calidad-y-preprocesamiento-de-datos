import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Generamos datos normales en forma de nube de puntos
rng = np.random.RandomState(42)
X_inliers = 0.5 * rng.randn(200, 2)

# Generamos datos anómalos alejados del centro
X_outliers = rng.uniform(low=-3, high=3, size=(20, 2))

# Unimos los datos
X = np.vstack((X_inliers, X_outliers))

# Entrenamos Isolation Forest con dos características
clf = IsolationForest(contamination=0.1, random_state=42)
clf.fit(X)

# Predicción de anomalías (-1 es anómalo, 1 es normal)
y_pred = clf.predict(X)

# Visualización de los datos y las anomalías detectadas
plt.figure(figsize=(8, 6))
plt.scatter(X[y_pred == 1, 0], X[y_pred == 1, 1], c="blue", label="Normal")
plt.scatter(X[y_pred == -1, 0], X[y_pred == -1, 1], c="red", marker="x", label="Anomalía")

plt.title("Detección de anomalías con Isolation Forest (2D)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True)
plt.show()
