import random  # Importamos el modulo random para utilizar mas adelante

# Vocabulario de ejemplo
vocabulario = {'hello': 'hola', 'world': 'mundo', 'python': 'python'}

def traduccion_estadistica(frase):
    palabras = frase.split()  # Dividimos la frase en palabras
    traduccion = [vocabulario[palabra] if palabra in vocabulario else palabra for palabra in palabras]
    # Si la palabra esta en el vocabulario, la traducimos; de lo contrario, la dejamos igual
    return ' '.join(traduccion)  # Unimos las palabras traducidas en una frase nuevamente

# Ejemplo de frase a traducir
frase_ejemplo = 'hello world, this is python'
traduccion = traduccion_estadistica(frase_ejemplo)  # Realizamos la traduccion de la frase de ejemplo

print(f'Traduccion: {traduccion}')  # Imprimimos la traduccion obtenida


