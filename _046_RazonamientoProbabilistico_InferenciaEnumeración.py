def inferencia_por_enumeracion(evidencia):
    # Definimos las probabilidades iniciales
    p_h1 = 0.3
    p_h2 = 0.7
    p_e1_given_h1 = 0.8
    p_e1_given_h2 = 0.2

    # Calculamos la probabilidad posterior
    p_h1_given_evidencia = (p_e1_given_h1 * p_h1) / ((p_e1_given_h1 * p_h1) + (p_e1_given_h2 * p_h2))
    p_h2_given_evidencia = 1 - p_h1_given_evidencia

    # Imprimimos los resultados
    print(f"Probabilidad de que haya trafico dado que esta lloviendo: {p_h1_given_evidencia:.2f}")
    print(f"Probabilidad de que no haya trafico dado que esta lloviendo: {p_h2_given_evidencia:.2f}")

# Ejemplo de uso
evidencia_lluvia = True  # Esta lloviendo
inferencia_por_enumeracion(evidencia_lluvia)
