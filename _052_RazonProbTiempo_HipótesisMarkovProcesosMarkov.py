import numpy as np

# Definicion de una cadena de Markov de tiempo discreto
# Matriz de transicion (probabilidades de transicion entre estados)
transition_matrix = np.array([[0.8, 0.2],  # Probabilidad de transicion de A a A y A a B
                              [0.4, 0.6]]) # Probabilidad de transicion de B a A y B a B

# Estado inicial (probabilidad inicial de estar en A o B)
initial_state = np.array([0.5, 0.5])  # Inicialmente igual probabilidad de estar en A o B

# Simulacion de la cadena de Markov
num_steps = 1000  # Numero de pasos de simulacion
current_state = initial_state.copy()  # Copia del estado inicial

for _ in range(num_steps):
    current_state = np.dot(current_state, transition_matrix)  # Actualizar el estado segun la matriz de transicion

# Resultado final (probabilidad de estar en A o B despues de las iteraciones)
print("Probabilidad final de estar en A:", current_state[0])  # Imprimir la probabilidad de estar en A
print("Probabilidad final de estar en B:", current_state[1])  # Imprimir la probabilidad de estar en B

