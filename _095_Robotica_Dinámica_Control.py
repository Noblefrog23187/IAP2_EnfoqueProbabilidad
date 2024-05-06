import numpy as np

class Robot:
    def __init__(self, x=0, y=0, theta=0):
        self.x = x  # Posicion en el eje x
        self.y = y  # Posicion en el eje y
        self.theta = theta  # Orientacion del robot en radianes

    def move(self, v, omega, dt):
        # Actualiza la posicion y orientacion del robot en base a las velocidades lineal (v) y angular (omega)
        self.x += v * np.cos(self.theta) * dt
        self.y += v * np.sin(self.theta) * dt
        self.theta += omega * dt

# Funcion principal
def main():
    # Crear un objeto Robot con posicion inicial (0, 0) y orientacion inicial 0 radianes
    robot = Robot()

    # Simular el movimiento del robot durante 5 segundos con velocidad lineal constante y velocidad angular variable
    for t in np.arange(0, 5, 0.1):
        v = 0.5  # Velocidad lineal constante
        omega = np.sin(t)  # Velocidad angular variable sinusoidal
        robot.move(v, omega, 0.1)  # Actualizar la posicion y orientacion del robot
        print(f"Tiempo: {t:.1f}s, Posicion: ({robot.x:.2f}, {robot.y:.2f}), Orientacion: {robot.theta:.2f} rad")

if __name__ == "__main__":
    main()

