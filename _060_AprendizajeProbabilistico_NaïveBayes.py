# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Generar datos sinteticos (puedes reemplazar esto con tus propios datos)
np.random.seed(42)
n_samples = 1000
X = np.random.rand(n_samples, 2)  # Caracteristicas (atributos)
y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Etiquetas (clases)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el clasificador Naive-Bayes
clf = GaussianNB()
clf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precision del clasificador
accuracy = accuracy_score(y_test, y_pred)
print(f"Precision del clasificador: {accuracy:.2f}")

