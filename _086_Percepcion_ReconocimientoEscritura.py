
# Importar librerias necesarias
import numpy as np #Se importan las bibliotecas necesarias: NumPy para manipulacion de datos numericos y Matplotlib para la visualizacion de datos
import matplotlib.pyplot as plt

# Generar datos de ejemplo (simulacion de escritura)
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Visualizar los datos de escritura
plt.figure()
plt.plot(x, y)
plt.title('Ejemplo de Escritura')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.show()
