import numpy as np

class MantoMarkov:
    def __init__(self, estados, matriz_transicion):
        """
        Inicializa un modelo de manto de Markov con los estados y la matriz de transicion dada.

        Args:
            estados (list): Lista de estados posibles en el modelo.
            matriz_transicion (np.ndarray): Matriz de transicion entre los estados.
        """
        self.estados = estados
        self.matriz_transicion = matriz_transicion

    def simular(self, estado_inicial, pasos):
        """
        Simula el proceso de manto de Markov durante el numero especificado de pasos.

        Args:
            estado_inicial (str): Estado inicial del proceso.
            pasos (int): Numero de pasos a simular.

        Returns:
            list: Lista de estados visitados durante la simulacion.
        """
        estado_actual = estado_inicial
        estados_simulados = [estado_actual]

        for _ in range(pasos):
            # Determinar el proximo estado segun la matriz de transicion
            estado_siguiente = np.random.choice(self.estados, p=self.matriz_transicion[self.estados.index(estado_actual)])
            estados_simulados.append(estado_siguiente)
            estado_actual = estado_siguiente

        return estados_simulados


# Ejemplo de uso
estados = ['Soleado', 'Nublado', 'Lluvioso']
# Definir la matriz de transicion
matriz_transicion = np.array([
    [0.7, 0.2, 0.1],
    [0.3, 0.6, 0.1],
    [0.1, 0.4, 0.5]
])

# Crear una instancia del modelo de manto de Markov
mm = MantoMarkov(estados, matriz_transicion)

# Simular el proceso de manto de Markov durante 10 pasos comenzando desde el estado 'Soleado'
simulacion = mm.simular('Soleado', 10)
print("Simulacion del proceso de Manto de Markov:", simulacion)

