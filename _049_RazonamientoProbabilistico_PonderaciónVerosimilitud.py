import numpy as np
from scipy.special import factorial

# Datos observados (numero de multimillonarios en diferentes paises)
multimillonarios = [10, 15, 8, 12, 20]

def log_verosimilitud(mu, datos):
    # Calcula el logaritmo de la funcion de verosimilitud
    # Suma los logaritmos de la funcion de probabilidad de Poisson para cada dato en los datos observados
    log_likelihood = sum(np.log(mu**y * np.exp(-mu) / factorial(y)) for y in datos)
    return log_likelihood

def estimacion_maxima_verosimilitud(datos):
    # Encuentra el valor de mu que maximiza la verosimilitud
    # Define un rango de valores para mu y calcula el logaritmo de la verosimilitud para cada valor en el rango
    mejores_mu = np.linspace(0.1, 30, 1000)  # Rango de valores para mu
    mejores_likelihoods = [log_verosimilitud(mu, datos) for mu in mejores_mu]
    # Encuentra el valor de mu que maximiza la verosimilitud
    mejor_mu = mejores_mu[np.argmax(mejores_likelihoods)]

    return mejor_mu

# Calcula la estimacion de maxima verosimilitud
mu_optimo = estimacion_maxima_verosimilitud(multimillonarios)

print(f"Estimacion de mu (numero promedio de multimillonarios): {mu_optimo:.2f}")

