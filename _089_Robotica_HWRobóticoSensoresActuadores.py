# _*_ coding: utf-8 _*_

# Importar la biblioteca necesaria para el simulacro
import time  # Importa la biblioteca time para manejar el tiempo

# Simulacion del sensor de proximidad (simplemente como ejemplo)
def leer_sensor_proximidad():
    # Aqui podriamos leer datos reales del sensor
    return True  # Simulamos que hay un obstáculo cercano

# Simulacion del actuador electrico (simplemente como ejemplo)
def mover_robot_adelante():
    print("Moviendo el robot hacia adelante...")
    # Aqui podriamos enviar señales eléctricas para mover el robot

# Programa principal
def main():
    while True:
        if leer_sensor_proximidad():
            mover_robot_adelante()
        else:
            print("No hay obstáculos cercanos. Esperando...")
            time.sleep(1)  # Esperar 1 segundo antes de verificar nuevamente

if __name__ == "__main__":
    main()


