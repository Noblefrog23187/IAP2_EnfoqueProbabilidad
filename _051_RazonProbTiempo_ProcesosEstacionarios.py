import numpy as np
import matplotlib.pyplot as plt

# Crear una serie de tiempo sintetica (proceso estacionario)
np.random.seed(42)  # Fijamos la semilla para reproducibilidad
n_samples = 100
t = np.arange(n_samples)
noise = np.random.normal(loc=0, scale=1, size=n_samples)  # Ruido aleatorio
time_series = 0.5 * t + noise  # Serie de tiempo con tendencia lineal

# Visualizacion de la serie de tiempo
plt.figure(figsize=(8, 4))  # Crear una figura con un tamano especifico
plt.plot(t, time_series, label="Serie de tiempo")  # Graficar la serie de tiempo
plt.xlabel("Tiempo")  # Etiqueta del eje x
plt.ylabel("Valor")  # Etiqueta del eje y
plt.title("Serie de tiempo sintetica")  # Titulo de la grafica
plt.grid(True)  # Habilitar la cuadricula en la grafica
plt.legend()  # Mostrar la leyenda
plt.show()  # Mostrar la grafica

# Prueba de estacionariedad (Dickey-Fuller)
from statsmodels.tsa.stattools import adfuller

result = adfuller(time_series)  # Realizar la prueba de Dickey-Fuller
print("Estadistico de prueba:", result[0])  # Imprimir el estadistico de la prueba
print("Valor p:", result[1])  # Imprimir el valor p
print("Valores criticos:", result[4])  # Imprimir los valores criticos
print("Es estacionaria", result[1] < 0.05)  # Verificar si la serie de tiempo es estacionaria

