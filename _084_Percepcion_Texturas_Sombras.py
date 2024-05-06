# Importar librerias necesarias
import matplotlib.pyplot as plt  # Importamos la biblioteca matplotlib para visualizacion
import numpy as np  # Importamos la biblioteca numpy para trabajar con matrices y arrays

# Crear una matriz de valores aleatorios para simular una textura
textura = np.random.rand(10, 10)  # Creamos una matriz de tamano 10x10 con valores aleatorios entre 0 y 1

# Mostrar la textura en forma de imagen
plt.imshow(textura, cmap='gray')  # Mostramos la matriz como una imagen en escala de grises
plt.title('Textura Aleatoria')  # Establecemos el titulo de la figura
plt.axis('off')  # Desactivamos los ejes
plt.show()  # Mostramos la figura con la textura aleatoria


