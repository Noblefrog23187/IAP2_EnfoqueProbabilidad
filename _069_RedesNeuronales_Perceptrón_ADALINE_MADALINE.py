# Importar las bibliotecas necesarias
import numpy as np  # Para manipulacion de datos numericos
from sklearn.datasets import load_iris  # Para cargar el conjunto de datos de iris
from sklearn.model_selection import train_test_split  # Para dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.linear_model import Perceptron, SGDClassifier  # Para crear modelos de Perceptron y ADALINE
from sklearn.preprocessing import StandardScaler  # Para normalizar (escalar) los datos
from sklearn.metrics import accuracy_score  # Para calcular la precision del modelo

# Cargar el conjunto de datos de iris (ejemplo de clasificacion)
iris = load_iris()
X, y = iris.data, iris.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Normalizar los datos (escalar)
scaler = StandardScaler()  # Inicializar el objeto para escalar los datos
X_train = scaler.fit_transform(X_train)  # Escalar los datos de entrenamiento y aprender los parametros de escala
X_test = scaler.transform(X_test)  # Escalar los datos de prueba utilizando los parametros de escala aprendidos

# Crear el modelo Perceptron
perceptron_model = Perceptron(max_iter=1000, random_state=42)  # Inicializar el modelo Perceptron
perceptron_model.fit(X_train, y_train)  # Entrenar el modelo Perceptron

# Crear el modelo ADALINE (SGDClassifier con funcion de perdida hinge)
adaline_model = SGDClassifier(loss='hinge', max_iter=1000, random_state=42)  # Inicializar el modelo ADALINE
adaline_model.fit(X_train, y_train)  # Entrenar el modelo ADALINE

# Crear el modelo MADALINE (Multiple ADALINE)
madaline_model = SGDClassifier(loss='hinge', max_iter=1000, random_state=42, n_jobs=-1)  # Inicializar el modelo MADALINE
madaline_model.fit(X_train, y_train)  # Entrenar el modelo MADALINE

# Realizar predicciones en el conjunto de prueba
y_pred_perceptron = perceptron_model.predict(X_test)  # Predicciones del modelo Perceptron
y_pred_adaline = adaline_model.predict(X_test)  # Predicciones del modelo ADALINE
y_pred_madaline = madaline_model.predict(X_test)  # Predicciones del modelo MADALINE

# Calcular la precision de los modelos
accuracy_perceptron = accuracy_score(y_test, y_pred_perceptron)  # Precision del modelo Perceptron
accuracy_adaline = accuracy_score(y_test, y_pred_adaline)  # Precision del modelo ADALINE
accuracy_madaline = accuracy_score(y_test, y_pred_madaline)  # Precision del modelo MADALINE

# Imprimir la precision de los modelos
print(f"Precision del Perceptron: {accuracy_perceptron:.4f}")
print(f"Precision de ADALINE: {accuracy_adaline:.4f}")
print(f"Precision de MADALINE: {accuracy_madaline:.4f}")

