import numpy as np

# Definir la funcion de transicion de estado (modelo dinamico)
def transicion_estado(x_t_1):
    # Ejemplo: Modelo de movimiento lineal
    return x_t_1 + np.random.normal(loc=0, scale=1)

# Definir la funcion de observacion (modelo de medicion)
def observacion(x_t):
    # Ejemplo: Observacion con ruido gaussiano
    return x_t + np.random.normal(loc=0, scale=0.1)

# Inicializar el filtro de particulas
n_particulas = 100
particulas = np.random.normal(loc=0, scale=1, size=n_particulas)

# Simulacion de filtrado de particulas
observaciones = [1.1, 2.0, 2.9, 4.0]
for z in observaciones:
    # Prediccion: Mover las particulas segun el modelo de transicion
    particulas = transicion_estado(particulas)

    # Actualizacion: Ponderar las particulas segun la observacion
    pesos = np.exp(-0.5 * (z - particulas)**2 / 0.1**2)
    pesos /= np.sum(pesos)

    # Resampling: Muestrear nuevas particulas segun los pesos
    particulas = np.random.choice(particulas, size=n_particulas, p=pesos)

    # Estimacion: Calcular la media de las particulas como la estimacion del estado
    estimacion_estado = np.mean(particulas)

    print(f"Estimacion del estado: {estimacion_estado:.2f}")

print("Particulas finales:")
print(particulas)

