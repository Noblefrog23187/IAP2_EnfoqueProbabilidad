import numpy as np
from scipy.linalg import inv

# Definir las matrices iniciales
A = np.array([[1, 1], [0, 1]])  # Matriz de transicion de estado
H = np.array([[1, 0]])          # Matriz de observacion
Q = np.array([[0.0001, 0], [0, 0.0001]])  # Covarianza del proceso (ruido del sistema)
R = np.array([[1]])             # Covarianza de la medicion (ruido de la observacion)

# Inicializar el estado y la covarianza
x = np.array([[0], [0]])       # Estado inicial (posicion y velocidad)
P = np.array([[1, 0], [0, 1]]) # Covarianza inicial

# Datos observados (simulacion de una posicion)
observaciones = np.array([1.1, 2.0, 2.9, 4.0])

# Filtro de Kalman
for z in observaciones:
    # Prediccin
    x = np.dot(A, x)
    P = np.dot(np.dot(A, P), A.T) + Q

    # Actualizacion
    y = z - np.dot(H, x)
    S = np.dot(np.dot(H, P), H.T) + R
    K = np.dot(np.dot(P, H.T), inv(S))
    x = x + np.dot(K, y)
    P = np.dot((np.eye(2) - np.dot(K, H)), P)

    print(f"Posicion estimada: {x[0][0]:.2f}, Velocidad estimada: {x[1][0]:.2f}")

print("Matriz de covarianza final:")
print(P)

