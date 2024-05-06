import math

# Funcion para calcular la cinematica inversa de un robot de 2-DOF
def calcular_cinematica_inversa(x, y):
    # Longitudes de los brazos del robot
    L1 = 5  # Longitud del primer brazo
    L2 = 4  # Longitud del segundo brazo

    # Calcular el angulo del primer eslabon (theta1)
    theta1 = math.atan2(y, x)

    # Calcular la distancia entre el punto (x, y) y el origen del sistema de coordenadas
    r = math.sqrt(x**2 + y**2)

    # Calcular el angulo del segundo eslabon (theta2) utilizando el teorema del coseno
    cos_theta2 = (r**2 - L1**2 - L2**2) / (2 * L1 * L2)
    sin_theta2 = math.sqrt(1 - cos_theta2**2)
    theta2 = math.atan2(sin_theta2, cos_theta2)

    # Convertir los angulos de radianes a grados
    theta1_grados = math.degrees(theta1)
    theta2_grados = math.degrees(theta2)

    return theta1_grados, theta2_grados

# Funcion principal
def main():
    # Coordenadas del punto objetivo
    x_objetivo = 6
    y_objetivo = 3

    # Calcular la cinematica inversa para el punto objetivo
    theta1, theta2 = calcular_cinematica_inversa(x_objetivo, y_objetivo)

    # Mostrar los angulos resultantes
    print("Angulo del primer eslabon (theta1):", theta1, "grados")
    print("Angulo del segundo eslabon (theta2):", theta2, "grados")

# Llamar a la funcion principal para ejecutar el programa
if __name__ == "__main__":
    main()

