import numpy as np
import matplotlib.pyplot as plt

# Generar datos sinteticos (distribucion verdadera desconocida)
np.random.seed(42)
datos_verdaderos = np.random.normal(loc=5, scale=2, size=1000)

# Supongamos que tenemos algunas observaciones (datos observados)
observaciones = datos_verdaderos[:50]

# Asumimos una distribucion a priori para el parametro (media)
media_priori = np.random.normal(loc=0, scale=10)

# Calcular la distribucion a posteriori utilizando el Teorema de Bayes
media_posteriori = (np.sum(observaciones) + 1) / (len(observaciones) + 1)

# Visualizar los resultados
plt.hist(datos_verdaderos, bins=30, alpha=0.5, label="Distribucion verdadera")
plt.axvline(x=media_priori, color='r', linestyle='--', label="Media a priori")
plt.axvline(x=media_posteriori, color='g', linestyle='--', label="Media a posteriori")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.title("Aprendizaje Bayesiano")
plt.legend()
plt.show()

print(f"Media a priori: {media_priori:.2f}")
print(f"Media a posteriori: {media_posteriori:.2f}")

