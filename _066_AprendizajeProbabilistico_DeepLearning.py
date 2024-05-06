# Importar las bibliotecas necesarias
import numpy as np  # Para manipulacion de datos numericos
from keras.models import Sequential  # Para construir modelos secuenciales
from keras.layers import Dense  # Capa densa (totalmente conectada)
from keras.optimizers import Adam  # Optimizador para el entrenamiento
from sklearn.datasets import make_classification  # Para generar datos sinteticos

# Generar datos sinteticos para clasificacion binaria
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Construir el modelo de red neuronal
model = Sequential()  # Crear un modelo secuencial
model.add(Dense(units=64, activation='relu', input_dim=20))  # Anadir una capa densa con activacion ReLU
model.add(Dense(units=1, activation='sigmoid'))  # Anadir una capa densa de salida con activacion sigmoide

# Compilar el modelo
model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2)

