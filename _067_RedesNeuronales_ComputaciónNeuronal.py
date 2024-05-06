# Importar las bibliotecas necesarias
import numpy as np  # Para manipulacion de datos numericos
from sklearn.datasets import load_iris  # Para cargar el conjunto de datos de iris
from sklearn.model_selection import train_test_split  # Para dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.neural_network import MLPClassifier  # Para construir el modelo de red neuronal
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

# Crear el modelo de red neuronal
model = MLPClassifier(hidden_layer_sizes=(8,), activation='relu', max_iter=1000, random_state=42)
# Parametros:
# - hidden_layer_sizes: tupla que especifica el numero de neuronas en cada capa oculta
# - activation: funcion de activacion de las capas ocultas (ReLU en este caso)
# - max_iter: numero maximo de iteraciones (epocas) durante el entrenamiento
# - random_state: semilla para la reproducibilidad de los resultados

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular la precision del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Precision del modelo: {accuracy:.4f}")  # Imprimir la precision del modelo con cuatro decimales

