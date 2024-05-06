# Importar las bibliotecas necesarias
import numpy as np

# Definir la funcion de activacion sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Definir la clase de la Red Neuronal
class NeuralNetwork:
    def __init__(self):
        np.random.seed(1)  # Fijar la semilla aleatoria para reproducibilidad
        self.weights = 2 * np.random.random((3, 1)) - 1  # Inicializar los pesos aleatorios entre -1 y 1

    def train(self, inputs, outputs, iterations):
        for iteration in range(iterations):
            input_layer = inputs
            outputs = self.predict(input_layer)
            error = outputs - outputs  # Calcular el error de la red
            adjustments = np.dot(input_layer.T, error * (outputs * (1 - outputs)))  # Calcular los ajustes necesarios a los pesos
            self.weights += adjustments  # Actualizar los pesos de la red

    def predict(self, inputs):
        return sigmoid(np.dot(inputs, self.weights))  # Realizar la prediccion utilizando la funcion de activacion sigmoide

# Datos de entrada y salida para entrenar la red
training_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])  # Entradas
training_outputs = np.array([[0, 1, 1, 0]]).T  # Salidas esperadas (objetivos)

# Crear una instancia de la Red Neuronal
neural_network = NeuralNetwork()

# Entrenar la red con los datos de entrada y salida
neural_network.train(training_inputs, training_outputs, 10000)  # Entrenar durante 10000 iteraciones

# Realizar predicciones con la red entrenada
print("Predicciones despues del entrenamiento:")
print(neural_network.predict(np.array([1, 0, 0])))  # Realizar una prediccion con una nueva entrada


