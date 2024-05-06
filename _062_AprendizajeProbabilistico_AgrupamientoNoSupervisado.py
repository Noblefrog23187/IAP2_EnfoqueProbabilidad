# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generar datos sinteticos (puedes reemplazar esto con tus propios datos)
np.random.seed(42)
n_samples = 1000
X = np.random.rand(n_samples, 2)  # Caracteristicas (atributos)

# Crear el modelo K-Means con 3 clusters
n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=42)

# Entrenar el modelo con los datos
kmeans.fit(X)

# Obtener las etiquetas de los clusters y los centroides
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Visualizar los resultados
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=100, label='Centroides')
plt.xlabel("Caracteristica 1")
plt.ylabel("Caracteristica 2")
plt.title("Agrupamiento con K-Means")
plt.legend()
plt.show()

print(f"Numero de clusters: {n_clusters}")
print(f"Coordenadas de los centroides:\n{centroids}")

