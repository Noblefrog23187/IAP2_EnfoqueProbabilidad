import numpy as np

# Datos de entrada y salida (ejemplo simple)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Inicializacion de pesos y bias
input_size = 2
hidden_size = 4
output_size = 1

# Pesos de la capa oculta y la capa de salida
W_hidden = np.random.randn(input_size, hidden_size)  # Pesos aleatorios para la capa oculta
b_hidden = np.zeros((1, hidden_size))  # Bias inicializados en cero para la capa oculta
W_output = np.random.randn(hidden_size, output_size)  # Pesos aleatorios para la capa de salida
b_output = np.zeros((1, output_size))  # Bias inicializados en cero para la capa de salida

# Funcion de activacion (sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la funcion de activacion (para retropropagacion)
def sigmoid_derivative(x):
    return x * (1 - x)

# Hiperparametros
learning_rate = 0.1  # Tasa de aprendizaje
epochs = 10000  # Numero de epocas de entrenamiento

# Entrenamiento de la red neuronal
for epoch in range(epochs):
    # Forward pass
    hidden_layer_input = np.dot(X, W_hidden) + b_hidden  # Entrada a la capa oculta
    hidden_layer_output = sigmoid(hidden_layer_input)  # Salida de la capa oculta despues de aplicar la funcion de activacion
    output_layer_input = np.dot(hidden_layer_output, W_output) + b_output  # Entrada a la capa de salida
    output_layer_output = sigmoid(output_layer_input)  # Salida de la capa de salida despues de aplicar la funcion de activacion

    # Calculo del error
    error = y - output_layer_output

    # Retropropagacion
    d_output = error * sigmoid_derivative(output_layer_output)  # Gradiente de la funcion de error respecto a la salida de la capa de salida
    error_hidden = d_output.dot(W_output.T)  # Error en la capa oculta
    d_hidden = error_hidden * sigmoid_derivative(hidden_layer_output)  # Gradiente de la funcion de error respecto a la salida de la capa oculta

    # Actualizacion de pesos y bias
    W_output += hidden_layer_output.T.dot(d_output) * learning_rate  # Actualizacion de los pesos de la capa de salida
    b_output += np.sum(d_output, axis=0, keepdims=True) * learning_rate  # Actualizacion del bias de la capa de salida
    W_hidden += X.T.dot(d_hidden) * learning_rate  # Actualizacion de los pesos de la capa oculta
    b_hidden += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate  # Actualizacion del bias de la capa oculta

# Predicciones
predicted_output = np.round(output_layer_output)  # Redondear las salidas de la capa de salida para obtener las predicciones finales
print("Predicciones:")
print(predicted_output)  # Imprimir las predicciones


