def regla_de_bayes(probabilidad_A, probabilidad_B_dado_A, probabilidad_B):
    """
    Calcula la probabilidad condicional utilizando la Regla de Bayes.

    Args:
        probabilidad_A (float): Probabilidad de A.
        probabilidad_B_dado_A (float): Probabilidad de B dado A.
        probabilidad_B (float): Probabilidad de B.

    Returns:
        float: La probabilidad condicional de A dado B.
    """
    # Calcula la probabilidad de A dado B utilizando la Regla de Bayes
    probabilidad_A_dado_B = (probabilidad_B_dado_A * probabilidad_A) / probabilidad_B

    return probabilidad_A_dado_B

# Definir las probabilidades
probabilidad_A = 0.3  # P(A)
probabilidad_B_dado_A = 0.7  # P(B|A)
probabilidad_B = 0.5  # P(B)

# Calcular la probabilidad condicional de A dado B utilizando la Regla de Bayes
probabilidad_A_dado_B = regla_de_bayes(probabilidad_A, probabilidad_B_dado_A, probabilidad_B)

# Mostrar el resultado
print("La probabilidad condicional de A dado B es:", probabilidad_A_dado_B)

