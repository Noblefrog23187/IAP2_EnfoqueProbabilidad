import random  # Importamos el modulo random para generar numeros aleatorios

# Definimos una funcion para simular el lanzamiento de una moneda
def lanzar_moneda():
    return random.choice(['cara', 'cruz'])  # La funcion elige aleatoriamente entre 'cara' y 'cruz'

# Funcion principal que simula varios lanzamientos de la moneda y calcula la probabilidad de cada resultado
def simular_lanzamientos(num_lanzamientos):
    resultados = {'cara': 0, 'cruz': 0}  # Inicializamos un diccionario para contar los resultados
    for _ in range(num_lanzamientos):  # Realizamos el numero especificado de lanzamientos
        resultado = lanzar_moneda()  # Lanzamos la moneda
        resultados[resultado] += 1  # Actualizamos el contador del resultado obtenido
    return resultados  # Devolvemos el diccionario con los resultados

# Simulamos 100 lanzamientos de la moneda
num_lanzamientos = 100
resultados = simular_lanzamientos(num_lanzamientos)

# Calculamos la probabilidad de obtener cara y cruz
probabilidad_cara = resultados['cara'] / num_lanzamientos
probabilidad_cruz = resultados['cruz'] / num_lanzamientos

# Imprimimos los resultados
print(f"Despues de {num_lanzamientos} lanzamientos:")
print(f"La probabilidad de obtener cara es: {probabilidad_cara}")
print(f"La probabilidad de obtener cruz es: {probabilidad_cruz}")

