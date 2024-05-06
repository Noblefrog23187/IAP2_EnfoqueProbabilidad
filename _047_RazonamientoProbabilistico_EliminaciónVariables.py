class EliminacionVariables:
    def __init__(self, tablas_probabilidad):
        """
        Inicializa un objeto de eliminacion de variables con las tablas de probabilidad proporcionadas.

        Args:
            tablas_probabilidad (dict): Un diccionario que mapea cada variable a su tabla de probabilidad.
        """
        self.tablas_probabilidad = tablas_probabilidad

    def eliminar_variables(self, variables_eliminar, evidencia):
        """
        Realiza la eliminacion de variables dadas y calcula la probabilidad de la variable objetivo.

        Args:
            variables_eliminar (list): Lista de variables que se van a eliminar.
            evidencia (dict): Un diccionario que contiene la evidencia en forma de variable-valor.

        Returns:
            dict: Un diccionario que contiene las probabilidades de cada valor de la variable objetivo dada la evidencia.
        """
        # Crear una copia de las tablas de probabilidad para trabajar sin modificar las originales
        tablas_probabilidad_temp = self.tablas_probabilidad.copy()

        # Aplicar la evidencia a las tablas de probabilidad
        for variable, valor in evidencia.items():
            # Filtrar las tablas de probabilidad segun la evidencia
            tablas_probabilidad_temp = {var: {val: prob for val, prob in tabla.items() if val == valor}
                                        for var, tabla in tablas_probabilidad_temp.items() if var == variable}

        # Eliminar las variables dadas de las tablas de probabilidad
        for variable_eliminar in variables_eliminar:
            tablas_probabilidad_temp.pop(variable_eliminar, None)

        # Realizar la suma de eliminacion de variables
        resultado = self.suma_eliminacion_variables(tablas_probabilidad_temp)

        # Normalizar las probabilidades y devolver el resultado
        return self.normalizar_probabilidades(resultado)

    def suma_eliminacion_variables(self, tablas_probabilidad_temp):
        """
        Realiza la suma de eliminacion de variables para calcular la probabilidad de la variable objetivo.

        Args:
            tablas_probabilidad_temp (dict): Un diccionario que contiene las tablas de probabilidad filtradas y modificadas.

        Returns:
            dict: Un diccionario que contiene las probabilidades de cada valor de la variable objetivo.
        """
        # Realizar la suma de eliminacion de variables iterativamente
        while len(tablas_probabilidad_temp) > 1:
            # Obtener las variables a combinar
            variables_combinar = list(tablas_probabilidad_temp.keys())[:2]
            # Realizar la combinacion de las tablas de probabilidad de las dos variables
            tabla_combinada = self.combinar_tablas_probabilidad(tablas_probabilidad_temp[variables_combinar[0]],
                                                                tablas_probabilidad_temp[variables_combinar[1]])
            # Actualizar las tablas de probabilidad con la tabla combinada
            tablas_probabilidad_temp.pop(variables_combinar[0])
            tablas_probabilidad_temp.pop(variables_combinar[1])
            tablas_probabilidad_temp[variables_combinar[0] + '_' + variables_combinar[1]] = tabla_combinada
        # El resultado final estara en la unica tabla de probabilidad restante
        return list(tablas_probabilidad_temp.values())[0]

    def combinar_tablas_probabilidad(self, tabla1, tabla2):
        """
        Combina dos tablas de probabilidad sumando las probabilidades de cada valor comun.

        Args:
            tabla1 (dict): La primera tabla de probabilidad.
            tabla2 (dict): La segunda tabla de probabilidad.

        Returns:
            dict: Un diccionario que contiene las probabilidades combinadas.
        """
        resultado = {}
        for clave1, prob1 in tabla1.items():
            for clave2, prob2 in tabla2.items():
                # Si las claves son iguales, sumar las probabilidades
                if clave1 == clave2:
                    resultado[clave1] = prob1 + prob2
        return resultado

    def normalizar_probabilidades(self, probabilidades):
        """
        Normaliza las probabilidades para que sumen 1.

        Args:
            probabilidades (dict): Un diccionario que contiene las probabilidades de cada valor de una variable.

        Returns:
            dict: Un diccionario que contiene las probabilidades normalizadas.
        """
        suma = sum(probabilidades.values())
        return {clave: valor / suma for clave, valor in probabilidades.items()}


# Ejemplo de uso
tablas_probabilidad = {
    'A': {('a1', 'b', '1'): 0.2, ('a2', 'b', '1'): 0.8},
    'B': {('b',): 0.5},
    'C': {('1',): 0.7, ('2',): 0.3}
}

red_bayesiana = EliminacionVariables(tablas_probabilidad)

# Realizar eliminacion de variables
variables_eliminar = ['B']
evidencia = {'C': '1'}
probabilidades_A = red_bayesiana.eliminar_variables(variables_eliminar, evidencia)
print("Probabilidades de A dado C=1 (con B eliminada):", probabilidades_A)
