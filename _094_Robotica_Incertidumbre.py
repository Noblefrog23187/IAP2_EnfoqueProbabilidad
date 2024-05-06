import random

# Funcion para simular mediciones con incertidumbre
def medir_distancia_real():
    # Simulacion de la distancia real medida por el robot
    distancia_real = random.uniform(0.0, 10.0)  # Genera una distancia aleatoria entre 0 y 10 metros
    return distancia_real

# Funcion para simular mediciones con ruido o error de medicion
def medir_con_incertidumbre(distancia_real, incertidumbre):
    # Simulacion de la medicion con incertidumbre
    medicion = distancia_real + random.uniform(-incertidumbre, incertidumbre)
    return medicion

# Funcion principal
def main():
    distancia_real = medir_distancia_real()  # Obtener la distancia real medida por el robot
    incertidumbre = 0.5  # Definir la incertidumbre en las mediciones (en metros)

    # Realizar una medicion con incertidumbre
    medicion_con_incertidumbre = medir_con_incertidumbre(distancia_real, incertidumbre)

    # Mostrar resultados
    print("Distancia Real:", distancia_real, "metros")
    print("Medicion con Incertidumbre:", medicion_con_incertidumbre, "metros")

if __name__ == "__main__":
    main()

