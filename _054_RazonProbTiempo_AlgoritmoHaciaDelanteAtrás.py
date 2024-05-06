# Definir una funcion que implemente el Algoritmo Hacia Delante-Atras
def algoritmo_hacia_delante_atras(probabilidad_inicial, transiciones_adelante, transiciones_atras, pasos):
    probabilidad = probabilidad_inicial
    for _ in range(pasos):
        nueva_probabilidad = [0] * len(probabilidad)
        for i in range(len(probabilidad)):
            for j in range(len(transiciones_adelante[i])):
                nueva_probabilidad[j] += probabilidad[i] * transiciones_adelante[i][j]
            for k in range(len(transiciones_atras[i])):
                nueva_probabilidad[k] += probabilidad[i] * transiciones_atras[i][k]
        probabilidad = nueva_probabilidad
    return probabilidad

# Definir las probabilidades iniciales y las matrices de transicion
probabilidad_inicial = [0.5, 0.5]
transiciones_adelante = [[0.7, 0.3], [0.4, 0.6]]
transiciones_atras = [[0.2, 0.8], [0.1, 0.9]]
pasos = 3

# Ejecutar el algoritmo
resultado = algoritmo_hacia_delante_atras(probabilidad_inicial, transiciones_adelante, transiciones_atras, pasos)
print(resultado)

