import numpy as np
from scipy.stats import norm

# Generar datos sinteticos (mezcla de dos distribuciones gaussianas)
np.random.seed(42)
n_samples = 1000
data = np.concatenate([np.random.normal(loc=5, scale=1, size=n_samples // 2),
                       np.random.normal(loc=10, scale=2, size=n_samples // 2)])

# Inicializar los parametros (media y desviacion estandar) de las dos distribuciones
mu1, sigma1 = 4, 1
mu2, sigma2 = 8, 1

# Algoritmo EM
n_iterations = 10
for _ in range(n_iterations):
    # Expectation step: Calcular las probabilidades posteriores (responsabilidades)
    p1 = norm.pdf(data, loc=mu1, scale=sigma1)
    p2 = norm.pdf(data, loc=mu2, scale=sigma2)
    responsibilities = p1 / (p1 + p2)

    # Maximization step: Actualizar los parametros
    mu1 = np.sum(responsibilities * data) / np.sum(responsibilities)
    mu2 = np.sum((1 - responsibilities) * data) / np.sum(1 - responsibilities)
    sigma1 = np.sqrt(np.sum(responsibilities * (data - mu1)**2) / np.sum(responsibilities))
    sigma2 = np.sqrt(np.sum((1 - responsibilities) * (data - mu2)**2) / np.sum(1 - responsibilities))

print(f"Parametros estimados para la primera distribucion: mu={mu1:.2f}, sigma={sigma1:.2f}")
print(f"Parametros estimados para la segunda distribucion: mu={mu2:.2f}, sigma={sigma2:.2f}")

