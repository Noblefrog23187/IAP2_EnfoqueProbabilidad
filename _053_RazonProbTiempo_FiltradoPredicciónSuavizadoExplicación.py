import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generar una serie de tiempo sintetica con ruido
np.random.seed(42)  # Fijar la semilla aleatoria para reproducibilidad
n_samples = 100
t = np.arange(n_samples)
noise = np.random.normal(loc=0, scale=1, size=n_samples)
time_series = 0.5 * t + noise  # Serie de tiempo con tendencia lineal y ruido gaussiano

# Filtrado: Aplicamos un filtro de media movil para suavizar la serie de tiempo
window_size = 5
smoothed_series = np.convolve(time_series, np.ones(window_size) / window_size, mode='valid')

# Prediccion: Estimamos el proximo valor utilizando una distribucion normal
mean_last_value = time_series[-1]  # Media del ultimo valor de la serie de tiempo
std_last_value = np.std(time_series)  # Desviacion estandar de la serie de tiempo
predicted_next_value = np.random.normal(loc=mean_last_value, scale=std_last_value)  # Prediccion del proximo valor

# Suavizado: Visualizamos la serie de tiempo original y suavizada
plt.figure(figsize=(10, 6))
plt.plot(t, time_series, label="Serie de tiempo original")  # Serie de tiempo original
plt.plot(t[window_size - 1:], smoothed_series, label="Serie de tiempo suavizada")  # Serie de tiempo suavizada
plt.axvline(x=n_samples, color='red', linestyle='--', label="Prediccion")  # Linea vertical para la prediccion
plt.scatter(n_samples, predicted_next_value, color='red', marker='o')  # Punto para el proximo valor predicho
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.title("Filtrado, Prediccion y Suavizado de una Serie de Tiempo")
plt.legend()
plt.grid(True)
plt.show()

# Explicacion: Mostramos el valor predicho
print(f"Proximo valor predicho: {predicted_next_value:.2f}")

