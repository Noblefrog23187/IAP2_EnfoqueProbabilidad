import re

# Texto de ejemplo
texto = """
El gato come pescado.
El perro juega en el parque.
Los pajaros vuelan en el cielo.
El gato y el perro son amigos.
"""

# Definicion de patrones de expresiones regulares para extraer informacion
patron_animal = re.compile(r"(gato|perro|pajaros)")
patron_accion = re.compile(r"(come|juega|vuelan)")
patron_lugar = re.compile(r"(parque|cielo)")

# Busqueda de coincidencias en el texto
animales = patron_animal.findall(texto)
acciones = patron_accion.findall(texto)
lugares = patron_lugar.findall(texto)

# Impresion de la informacion extraida
print("Animales:", animales)
print("Acciones:", acciones)
print("Lugares:", lugares)


