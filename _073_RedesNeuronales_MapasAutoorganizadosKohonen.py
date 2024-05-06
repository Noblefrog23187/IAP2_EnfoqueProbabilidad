import numpy as np
import matplotlib.pyplot as plt

# Definicion de los datos (coleccion de vectores binarios)
n_i = 1000  # Numero de instancias
n_d = 10    # Dimension de los vectores (elementos en {0, 1})

# Generacion de datos iniciales aleatorios
elementos = [0, 1]  # Elementos posibles en los vectores binarios
proporcion = [5/6, 1/6]  # Proporcion de unos y ceros en los vectores generados
datosIniciales = np.random.choice(elementos, size=(n_i, n_d), replace=True, p=proporcion)
# Genera una matriz de tamano (n_i, n_d) con valores aleatorios (0 o 1) segun la proporcion definida

# Suma por filas para verificar la proporcion
suma_por_filas = datosIniciales.sum(axis=1)  # Suma los valores de cada fila (axis=1 indica que se suman por filas)
print(f"Suma por filas:\n{suma_por_filas}")  # Imprime la suma por filas para verificar la proporcion

# Media de la suma por filas
media_suma = suma_por_filas.mean()  # Calcula la media de las sumas por filas
print(f"Media de la suma por filas: {media_suma:.3f}")  # Imprime la media de las sumas por filas con tres decimales

# Histograma de todos los datos iniciales
plt.hist(datosIniciales.ravel(), bins=20)  # Crea un histograma con los valores de todos los datos iniciales (aplanados) usando 20 bins
plt.title("Histograma de todos los datos iniciales")  # Titulo del histograma
plt.show()  # Muestra el histograma

