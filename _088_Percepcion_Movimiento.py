# Importar la libreria necesaria para graficos
import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib y renombrala como plt

# Datos de ejemplo para el movimiento de percepcion
x = [1, 2, 3, 4, 5]  # Lista de valores para el eje x (tiempo)
y = [2, 3, 4, 5, 6]  # Lista de valores para el eje y (posicion)

# Crear un grafico de dispersion para visualizar el movimiento de percepcion
plt.scatter(x, y)  # Crea un grafico de dispersion con los datos proporcionados
plt.xlabel('Tiempo')  # Etiqueta del eje x
plt.ylabel('Posicion')  # Etiqueta del eje y
plt.title('Movimiento de Percepcion')  # Titulo del grafico
plt.show()  # Muestra el grafico


