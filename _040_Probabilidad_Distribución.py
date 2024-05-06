def distribucion_probabilidad(datos):
    # Inicializamos un diccionario para almacenar las frecuencias de cada dato
    frecuencias = {}
    
    # Contamos las ocurrencias de cada dato en los datos de entrada
    for dato in datos:
        if dato in frecuencias:
            frecuencias[dato] += 1
        else:
            frecuencias[dato] = 1
    
    # Calculamos la suma total de las frecuencias
    total_frecuencias = sum(frecuencias.values())
    
    # Calculamos la distribucion de probabilidad dividiendo cada frecuencia por el total
    distribucion = {dato: frecuencia / total_frecuencias for dato, frecuencia in frecuencias.items()}
    
    return distribucion

# Datos de ejemplo: lista de observaciones
datos = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Calculamos y mostramos la distribucion de probabilidad de los datos
print("Datos de ejemplo:", datos)
print("Distribucion de probabilidad:")
for dato, probabilidad in distribucion_probabilidad(datos).items():
    print(f"{dato}: {probabilidad}")

