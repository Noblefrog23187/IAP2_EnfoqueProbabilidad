import numpy as np

# 1. Red de Hamming
def hamming_correction(pattern):
    # Calcula los pesos como el producto externo del patron consigo mismo
    weights = np.outer(pattern, pattern)
    # Simula un patron ruidoso cambiando un bit del patron original
    noisy_pattern = pattern.copy()
    noisy_pattern[2] = 0
    # Calcula el patron corregido aplicando los pesos al patron ruidoso
    corrected_pattern = np.sign(np.dot(weights, noisy_pattern))
    return corrected_pattern

# Ejemplo de uso
pattern_hamming = np.array([1, 0, 1, 0, 1])
corrected_hamming = hamming_correction(pattern_hamming)
print("Red de Hamming - Patron corregido:", corrected_hamming)

# 2. Red de Hopfield
def hopfield_update(weights, noisy_pattern, iterations=10):
    # Actualiza el patron ruidoso iterativamente utilizando la regla de actualizacion de Hopfield
    for _ in range(iterations):
        noisy_pattern = np.sign(np.dot(weights, noisy_pattern))
    return noisy_pattern

# Ejemplo de uso
pattern_hopfield1 = np.array([1, 0, 1, 0, 1])
pattern_hopfield2 = np.array([1, 1, 0, 1, 0])
# Calcula los pesos como la suma de los productos externos de los patrones
weights_hopfield = np.outer(pattern_hopfield1, pattern_hopfield1) + np.outer(pattern_hopfield2, pattern_hopfield2)
noisy_hopfield = np.array([1, 0, 0, 1, 1])
corrected_hopfield = hopfield_update(weights_hopfield, noisy_hopfield)
print("Red de Hopfield - Patron corregido:", corrected_hopfield)

# 3. Regla de Hebb
def hebb_weights(pattern1, pattern2):
    # Calcula los pesos segun la regla de Hebb
    return np.outer(pattern1, pattern1) + np.outer(pattern2, pattern2)

# Ejemplo de uso
pattern_hebb1 = np.array([1, 0, 1])
pattern_hebb2 = np.array([1, 1, 0])
weights_hebb = hebb_weights(pattern_hebb1, pattern_hebb2)
print("Regla de Hebb - Matriz de pesos:", weights_hebb)

# 4. Maquina de Boltzmann (capa oculta)
def boltzmann_hidden_layer(input_pattern, weights):
    # Calcula la salida de la capa oculta como la signo de la multiplicacion punto entre el patron de entrada y los pesos
    return np.sign(np.dot(input_pattern, weights))

# Ejemplo de uso
pattern_boltzmann = np.array([1, 0, 1])
weights_boltzmann = np.random.randn(3, 4)  # Matriz de pesos aleatoria
output_boltzmann = boltzmann_hidden_layer(pattern_boltzmann, weights_boltzmann)
print("Maquina de Boltzmann - Salida de la capa oculta:", output_boltzmann)


