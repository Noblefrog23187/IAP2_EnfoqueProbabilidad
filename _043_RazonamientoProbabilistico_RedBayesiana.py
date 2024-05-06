class RedBayesiana:
    def __init__(self):
        self.nodos = {}  # Diccionario para almacenar los nodos de la red

    def agregar_nodo(self, nombre, padres, probabilidad):
        """
        Agrega un nodo a la red bayesiana.

        Args:
            nombre (str): Nombre del nodo.
            padres (list): Lista de nombres de los nodos padres.
            probabilidad (dict): Probabilidad condicional del nodo dado sus padres.
        """
        self.nodos[nombre] = {'padres': padres, 'probabilidad': probabilidad}

    def calcular_probabilidad(self, nombre_nodo, valores_nodos):
        """
        Calcula la probabilidad del nodo dado sus padres.

        Args:
            nombre_nodo (str): Nombre del nodo.
            valores_nodos (dict): Valores de los nodos padres del nodo.

        Returns:
            float: La probabilidad del nodo.
        """
        probabilidad = self.nodos[nombre_nodo]['probabilidad']  # Obtener la probabilidad condicional
        prob = probabilidad[tuple(valores_nodos[padre] for padre in self.nodos[nombre_nodo]['padres'])]
        return prob

# Crear una instancia de la red bayesiana
red_bayesiana = RedBayesiana()

# Definir los nodos y sus relaciones
red_bayesiana.agregar_nodo('A', [], {(): 0.3})  # Nodo A sin padres
red_bayesiana.agregar_nodo('B', ['A'], {(True,): 0.8, (False,): 0.2})  # Nodo B con A como padre

# Calcular la probabilidad del nodo B dado el valor verdadero de A
probabilidad_B_dado_A_true = red_bayesiana.calcular_probabilidad('B', {'A': True})
print("La probabilidad del nodo B dado A=True es:", probabilidad_B_dado_A_true)

