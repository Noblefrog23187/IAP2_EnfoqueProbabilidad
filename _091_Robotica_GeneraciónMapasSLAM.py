import numpy as np

# Funcion para simular la lectura de datos del sensor
def leer_datos_sensor():
    # Simula la lectura de datos de un sensor, devolviendo una distancia y un angulo
    distancia = np.random.uniform(0.5, 5.0)  # Distancia medida por el sensor (en metros)
    angulo = np.random.uniform(-np.pi/4, np.pi/4)  # Angulo de la lectura del sensor (en radianes)
    return distancia, angulo

# Funcion para actualizar la posicion del robot utilizando los datos del sensor
def actualizar_posicion(x, y, theta, distancia, angulo):
    # Actualiza la posicion del robot segun los datos del sensor
    x += distancia * np.cos(theta + angulo)  # Actualiza la posicion en el eje x
    y += distancia * np.sin(theta + angulo)  # Actualiza la posicion en el eje y
    return x, y

# Funcion principal que simula el proceso SLAM
def main():
    # Posicion inicial del robot
    x_robot = 0.0  # Posicion inicial en el eje x
    y_robot = 0.0  # Posicion inicial en el eje y
    theta_robot = 0.0  # Orientacion inicial del robot (en radianes)

    # Bucle para simular el movimiento del robot y la actualizacion del mapa
    for _ in range(10):  # Realiza 10 iteraciones
        # Simula la lectura de datos del sensor
        distancia, angulo = leer_datos_sensor()

        # Actualiza la posicion del robot utilizando los datos del sensor
        x_robot, y_robot = actualizar_posicion(x_robot, y_robot, theta_robot, distancia, angulo)

        # Imprime la posicion actual del robot
        print("Posicion del robot: ({:.2f}, {:.2f})".format(x_robot, y_robot))

if __name__ == "__main__":
    main()

