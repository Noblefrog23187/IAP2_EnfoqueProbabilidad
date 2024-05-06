import random

class MuestreoProbabilistico:
    def __init__(self, red_bayesiana):
        """
        Inicializa un objeto para realizar muestreo probabilistico en una red bayesiana dada.

        Args:
            red_bayesiana (dict): Un diccionario que representa la red bayesiana, donde las claves son las variables
                                  y los valores son listas de tuplas (valor, probabilidad) para cada variable.
        """
        self.red_bayesiana = red_bayesiana

    def muestreo_directo(self, variable_objetivo, evidencia):
        """
        Realiza muestreo directo para estimar la probabilidad de la variable objetivo dada la evidencia.

        Args:
            variable_objetivo (str): La variable cuya probabilidad se desea estimar.
            evidencia (dict): Un diccionario que contiene la evidencia en forma de variable-valor.

        Returns:
            float: La estimacion de la probabilidad de la variable objetivo dado la evidencia.
        """
        conteo = 0
        total_muestras = 10000  # Numero total de muestras para el muestreo
        for _ in range(total_muestras):
            muestra = self.generar_muestra(evidencia)
            if muestra[variable_objetivo] == evidencia.get(variable_objetivo):
                conteo += 1
        return conteo / total_muestras

    def muestreo_por_rechazo(self, variable_objetivo, evidencia):
        """
        Realiza muestreo por rechazo para estimar la probabilidad de la variable objetivo dada la evidencia.

        Args:
            variable_objetivo (str): La variable cuya probabilidad se desea estimar.
            evidencia (dict): Un diccionario que contiene la evidencia en forma de variable-valor.

        Returns:
            float: La estimacion de la probabilidad de la variable objetivo dado la evidencia.
        """
        conteo = 0
        total_muestras = 10000  # Numero total de muestras para el muestreo
        for _ in range(total_muestras):
            muestra = self.generar_muestra(self.red_bayesiana)
            if self.cumple_evidencia(muestra, evidencia):
                conteo += 1
        return conteo / total_muestras

    def generar_muestra(self, evidencia):
        """
        Genera una muestra aleatoria de la red bayesiana dada la evidencia.

        Args:
            evidencia (dict): Un diccionario que contiene la evidencia en forma de variable-valor.

        Returns:
            dict: Un diccionario que contiene una muestra aleatoria de la red bayesiana.
        """
        muestra = {}
        for variable, valores in self.red_bayesiana.items():
            if variable in evidencia:
                # Si la variable esta en la evidencia, se selecciona su valor directamente
                muestra[variable] = evidencia[variable]
            else:
                # Si la variable no esta en la evidencia, se selecciona un valor aleatorio basado en las probabilidades
                muestra[variable] = self.seleccionar_valor(valores)
        return muestra

    def seleccionar_valor(self, valores):
        """
        Selecciona un valor aleatorio basado en las probabilidades proporcionadas.

        Args:
            valores (list): Una lista de tuplas (valor, probabilidad) para una variable.

        Returns:
            str: El valor seleccionado aleatoriamente.
        """
        probabilidad_acumulada = 0
        aleatorio = random.random()
        for valor, probabilidad in valores:
            probabilidad_acumulada += probabilidad
            if aleatorio <= probabilidad_acumulada:
                return valor

    def cumple_evidencia(self, muestra, evidencia):
        """
        Verifica si la muestra cumple con la evidencia dada.

        Args:
            muestra (dict): La muestra aleatoria generada.
            evidencia (dict): Un diccionario que contiene la evidencia en forma de variable-valor.

        Returns:
            bool: True si la muestra cumple con la evidencia, False en caso contrario.
        """
        for variable, valor in evidencia.items():
            if muestra.get(variable) != valor:
                return False
        return True

# Ejemplo de uso
red_bayesiana = {
    'A': [('a1', 0.3), ('a2', 0.7)],
    'B': [('b', 0.5)],
    'C': [('c1', 0.4), ('c2', 0.6)]
}

muestreo = MuestreoProbabilistico(red_bayesiana)

# Ejemplo de muestreo directo
probabilidad_directa = muestreo.muestreo_directo('A', {'B': 'b'})
print("Probabilidad de A dado B='b' (muestreo directo):", probabilidad_directa)

# Ejemplo de muestreo por rechazo
probabilidad_rechazo = muestreo.muestreo_por_rechazo('A', {'B': 'b'})
print("Probabilidad de A dado B='b' (muestreo por rechazo):", probabilidad_rechazo)

