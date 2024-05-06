import numpy as np
from hmmlearn import hmm

# Generar datos sinteticos (puedes reemplazar esto con tus propios datos)
np.random.seed(42)
n_samples = 1000
X = np.random.rand(n_samples, 2)  # Caracteristicas (atributos)

# Crear un modelo HMM con 3 estados ocultos
n_estados_ocultos = 3
modelo_hmm = hmm.GaussianHMM(n_components=n_estados_ocultos, n_iter=100)

# Entrenar el modelo con los datos
modelo_hmm.fit(X)

# Obtener las etiquetas de los estados ocultos
etiquetas_estados = modelo_hmm.predict(X)

# Visualizar los resultados
print(f"Etiquetas de los estados ocultos: {etiquetas_estados}")

