def independencia_condicional(evento_A, evento_B_dado_A, evento_B):
    """
    Calcula si los eventos B y A son condicionalmente independientes dada la ocurrencia del evento A.

    Args:
        evento_A (float): Probabilidad del evento A.
        evento_B_dado_A (float): Probabilidad del evento B dado A.
        evento_B (float): Probabilidad del evento B.

    Returns:
        bool: True si los eventos B y A son condicionalmente independientes dado A, False en caso contrario.
    """
    # Calcula la probabilidad conjunta P(A ? B) usando la regla del producto
    probabilidad_conjunta = evento_A * evento_B_dado_A

    # Comprueba si la probabilidad conjunta es igual al producto de las probabilidades P(A) * P(B)
    return abs(probabilidad_conjunta - (evento_A * evento_B)) < 1e-10

# Definir las probabilidades de los eventos
probabilidad_A = 0.3  # P(A)
probabilidad_B_dado_A = 0.5  # P(B|A)
probabilidad_B = 0.4  # P(B)

# Comprobar si los eventos B y A son condicionalmente independientes dado A
es_independiente = independencia_condicional(probabilidad_A, probabilidad_B_dado_A, probabilidad_B)

# Mostrar el resultado
if es_independiente:
    print("Los eventos B y A son condicionalmente independientes dado A.")
else:
    print("Los eventos B y A no son condicionalmente independientes dado A.")

