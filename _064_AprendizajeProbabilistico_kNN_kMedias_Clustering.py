# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

# Generar datos sinteticos (puedes reemplazar esto con tus propios datos)
X, y = make_blobs(n_samples=300, centers=3, random_state=42)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo k-NN con 3 vecinos
knn = KNeighborsClassifier(n_neighbors=3)

# Entrenar el modelo con los datos de entrenamiento
knn.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = knn.predict(X_test)

# Calcular la precision del modelo k-NN
accuracy = accuracy_score(y_test, y_pred)
print(f"Precision del modelo k-NN: {accuracy:.2f}")

# Crear el modelo K-Means con 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)

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

print(f"Numero de clusters: 3")
print(f"Coordenadas de los centroides:\n{centroids}")

