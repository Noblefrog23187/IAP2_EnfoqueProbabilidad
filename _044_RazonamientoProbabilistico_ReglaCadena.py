class RedBayesiana:
    def __init__(self):
        self.nodos = {}  # Diccionario para almacenar informacion sobre los nodos de la red

    def agregar_nodo(self, nombre, padres, distribucion):
        """
        Agrega un nuevo nodo a la red bayesiana.

        Args:
            nombre (str): Nombre del nodo.
            padres (list): Lista de nombres de los nodos padres.
            distribucion (dict): Distribucion de probabilidad condicional del nodo.
        """
        self.nodos[nombre] = {'padres': padres, 'distribucion': distribucion}

    def calcular_probabilidad(self, nodo, configuracion):
        """
        Calcula la probabilidad de un nodo dado su configuracion y la evidencia disponible.

        Args:
            nodo (str): Nombre del nodo cuya probabilidad se calculara.
            configuracion (dict): Configuracion de valores de los nodos.

        Returns:
            float: Probabilidad del nodo dado su configuracion y la evidencia disponible.
        """
        if not self.nodos[nodo]['padres']:  # Si el nodo no tiene padres
            return self.nodos[nodo]['distribucion'][()]  # Devolver la probabilidad del nodo sin padres
        padres = tuple(configuracion[p] for p in self.nodos[nodo]['padres'])  # Obtener valores de los padres
        return self.nodos[nodo]['distribucion'][padres]  # Devolver la probabilidad condicional del nodo


class ReglaDeLaCadena:
    def __init__(self, red_bayesiana):
        """
        Inicializa la regla de la cadena con una red bayesiana dada.

        Args:
            red_bayesiana (RedBayesiana): Objeto de la clase RedBayesiana.
        """
        self.red_bayesiana = red_bayesiana  # Asignar la red bayesiana

    def calcular_probabilidad(self, evidencia, variable):
        """
        Calcula la probabilidad condicional de una variable dada una evidencia utilizando la regla de la cadena.

        Args:
            evidencia (dict): Evidencia disponible en forma de un diccionario de nodos y sus valores.
            variable (str): Nombre de la variable cuya probabilidad condicional se calculara.

        Returns:
            float: Probabilidad condicional de la variable dada la evidencia.
        """
        probabilidad = 1.0
        for nodo in evidencia:  # Para cada nodo en la evidencia
            probabilidad *= self.red_bayesiana.calcular_probabilidad(nodo, evidencia)  # Multiplicar las probabilidades
        probabilidad *= self.red_bayesiana.calcular_probabilidad(variable, evidencia)  # Multiplicar la probabilidad de la variable
        return probabilidad


# Ejemplo de uso
red_bayesiana = RedBayesiana()  # Crear una instancia de la red bayesiana
# Agregar nodos a la red bayesiana
red_bayesiana.agregar_nodo('A', [], {(): 0.3})
red_bayesiana.agregar_nodo('B', ['A'], {(True,): 0.8, (False,): 0.2})

# Crear una instancia de la regla de la cadena con la red bayesiana dada
regla_de_la_cadena = ReglaDeLaCadena(red_bayesiana)
# Calcular la probabilidad de B dado A=True utilizando la regla de la cadena
probabilidad = regla_de_la_cadena.calcular_probabilidad({'A': True}, 'B')
print("Probabilidad de B dado A=True:", probabilidad)

