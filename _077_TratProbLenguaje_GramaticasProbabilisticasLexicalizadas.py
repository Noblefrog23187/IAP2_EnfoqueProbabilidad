import random

# Definicion de la GLCP
glcp = {
    'VP': [('V NP', 0.7), ('V NP NP', 0.3)],
    'NP': [('D N', 1.0)] # NP tiene una unica regla: 'D N'.
}

# Funcion para derivar una frase
def derivar_frase(glcp, simbolo_inicial='VP'):
    frase = []
    pila = [simbolo_inicial]

    while pila:
        simbolo = pila.pop()
        if simbolo in glcp:
            # Elegir una regla segun la probabilidad
            regla, probabilidad = random.choices(glcp[simbolo], weights=[p[1] for p in glcp[simbolo]])[0]
            pila.extend(regla.split())
        else:
            frase.append(simbolo)

    return ' '.join(frase)

# Generar algunas frases
for _ in range(5):
    frase_generada = derivar_frase(glcp)
    print(f"Frase generada: {frase_generada}")

# Comentarios:
# La GLCP tiene dos reglas para VP: 'V NP' con probabilidad 0.7 y 'V NP NP' con probabilidad 0.3.
# La funcion derivar_frase utiliza una pila para construir la frase siguiendo las reglas de la gramatica.
# Las frases generadas pueden variar debido a la aleatoriedad en la eleccion de las reglas.

