import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib para graficar
import numpy as np  # Importa la biblioteca numpy para operaciones numericas

# Definir el rango de los angulos de las articulaciones del robot
theta1_range = np.linspace(0, np.pi, 100)  # Rango de angulos para la articulacion 1 (en radianes)
theta2_range = np.linspace(0, 2*np.pi, 100)  # Rango de angulos para la articulacion 2 (en radianes)

# Crear una cuadricula de valores para el espacio de configuracion
theta1, theta2 = np.meshgrid(theta1_range, theta2_range)

# Calcular las coordenadas (x, y) del extremo del efector final del robot en funcion de los angulos de las articulaciones
x = np.cos(theta1) + np.cos(theta1 + theta2)  # Calcula la coordenada x
y = np.sin(theta1) + np.sin(theta1 + theta2)  # Calcula la coordenada y

# Graficar el espacio de configuracion del robot
plt.figure(figsize=(8, 6))  # Crea una nueva figura con un tamano especifico
plt.contourf(theta1, theta2, np.sqrt(x**2 + y**2), cmap='viridis')  # Grafica un contorno relleno
plt.colorbar(label='Distancia al origen')  # Anade una barra de color con etiqueta
plt.xlabel('Angulo de articulacion 1 (rad)')  # Etiqueta del eje x
plt.ylabel('Angulo de articulacion 2 (rad)')  # Etiqueta del eje y
plt.title('Espacio de Configuracion del Robot')  # Titulo del grafico
plt.show()  # Muestra el grafico

