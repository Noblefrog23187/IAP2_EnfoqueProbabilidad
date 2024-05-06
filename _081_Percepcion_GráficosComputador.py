import matplotlib.pyplot as plt  # Importamos la biblioteca pyplot de matplotlib
import numpy as np

# Datos de ejemplo
x = np.random.rand(50)  # Coordenadas x aleatorias
y = np.random.rand(50)  # Coordenadas y aleatorias

# Crear un grafico de dispersion
plt.scatter(x, y, color='b', marker='o', label='Puntos aleatorios')
# Dibujamos el grafico de dispersion con los datos x e y, utilizando puntos azules ('b') como marcadores circulares ('o')

# Personalizar el grafico
plt.title('Grafico de Dispersian')  # Establecemos el titulo del grafico
plt.xlabel('Eje X')  # Etiquetamos el eje X
plt.ylabel('Eje Y')  # Etiquetamos el eje Y
plt.grid(True)  # Mostramos una cuadricula en el grafico
plt.legend()  # Mostramos la leyenda en el grafico

# Mostrar el grafico
plt.show()  # Mostramos el grafico completo


