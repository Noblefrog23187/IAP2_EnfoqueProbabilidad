# Definimos una funcion para calcular la probabilidad a priori de un evento
def probabilidad_a_priori(evento, datos):
    # Contamos cuantas veces ocurre el evento en los datos
    frecuencia_evento = datos.count(evento)
    
    # Calculamos la probabilidad a priori dividiendo la frecuencia del evento entre el total de observaciones
    probabilidad = frecuencia_evento / len(datos)
    
    return probabilidad

# Datos de ejemplo: lista de observaciones
datos = ['A', 'B', 'A', 'C', 'A', 'A', 'B', 'C', 'D', 'A']

# Evento para el cual queremos calcular la probabilidad a priori
evento = 'A'

# Calculamos y mostramos la probabilidad a priori del evento
print(f"Datos: {datos}")
print(f"Evento: {evento}")
print(f"Probabilidad a priori de '{evento}': {probabilidad_a_priori(evento, datos)}")

