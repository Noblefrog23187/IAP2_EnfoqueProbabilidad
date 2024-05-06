# Programa de control para un brazo robotico

# Definir una clase para el brazo robotico
class BrazoRobotico:
    def __init__(self):
        self.posicion = 0  # Inicializar la posicion del brazo

    # Metodo para mover el brazo hacia arriba
    def mover_arriba(self):
        self.posicion += 1  # Incrementar la posicion
        print("Brazo movido hacia arriba. Posicion:", self.posicion)

    # Metodo para mover el brazo hacia abajo
    def mover_abajo(self):
        if self.posicion > 0:
            self.posicion -= 1  # Decrementar la posicion si no esta en la posicion mas baja
        print("Brazo movido hacia abajo. Posicion:", self.posicion)

# Funcion principal
def main():
    brazo = BrazoRobotico()  # Crear una instancia del brazo robotico

    # Menu de opciones
    while True:
        print("\n*** Control del Brazo Robotico ***")
        print("1. Mover hacia arriba")
        print("2. Mover hacia abajo")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            brazo.mover_arriba()  # Llamar al metodo para mover el brazo hacia arriba
        elif opcion == '2':
            brazo.mover_abajo()  # Llamar al metodo para mover el brazo hacia abajo
        elif opcion == '3':
            print("Saliendo del programa...")
            break  # Salir del bucle y finalizar el programa
        else:
            print("Opcion no valida. Intentelo de nuevo.")

if __name__ == "__main__":
    main()

