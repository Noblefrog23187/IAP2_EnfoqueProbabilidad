import random

# Definir la clase Robot para representar el robot
class Robot:
    def __init__(self, mundo):
        self.mundo = mundo  # El mundo en el que se encuentra el robot
        self.posicion_actual = random.choice(self.mundo)  # Posicion inicial aleatoria

    def mover(self):
        # Simula el movimiento del robot
        self.posicion_actual = random.choice(self.mundo)

    def get_posicion_actual(self):
        # Retorna la posicion actual del robot
        return self.posicion_actual

# Definir el mundo (lista de posibles posiciones)
mundo = [(0, 0), (1, 0), (0, 1), (1, 1)]

# Crear un objeto Robot
robot = Robot(mundo)

# Realizar la localizacion Monte Carlo durante 10 iteraciones
for i in range(10):
    print("Iteracion", i+1)
    
    # Simular el movimiento del robot
    robot.mover()
    
    # Imprimir la posicion actual del robot
    print("Posicion actual del robot:", robot.get_posicion_actual())