# Importar las bibliotecas necesarias
import numpy as np
from hmmlearn import hmm

# Crear un conjunto de datos de ejemplo (secuencia de observaciones)
observaciones = np.array([[0, 1, 0, 1, 0],  # Ejemplo de secuencia binaria
                          [1, 0, 1, 0, 1]])

# Definir el modelo HMM con emisiones gaussianas
n_estados_ocultos = 2
modelo_hmm = hmm.GaussianHMM(n_components=n_estados_ocultos, n_iter=100)

# Entrenar el modelo utilizando el algoritmo hacia adelante-atras
modelo_hmm.fit(observaciones)

# Obtener las probabilidades de transicion y las medias de las emisiones gaussianas
prob_transiciones = modelo_hmm.transmat_
prob_emisiones = modelo_hmm.means_

# Imprimir los resultados
print("Probabilidades de transicion:")
print(prob_transiciones)
print("\nMedias de las emisiones gaussianas:")
print(prob_emisiones)

