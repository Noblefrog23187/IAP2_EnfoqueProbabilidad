def probabilidad_condicionada(evento_A, evento_B, datos):
    # Contamos cuantas veces ocurre el evento A y el evento B juntos
    frecuencia_AB = sum(1 for d in datos if d == (evento_A, evento_B))
    
    # Contamos cuantas veces ocurre el evento B
    frecuencia_B = datos.count((evento_A, evento_B)) + datos.count((evento_A, not evento_B))
    
    # Calculamos la probabilidad condicionada dividiendo la frecuencia conjunta entre la frecuencia de B
    prob_condicionada = frecuencia_AB / frecuencia_B
    
    return prob_condicionada

def normalizar_probabilidades(probabilidades):
    # Calculamos la suma de todas las probabilidades
    suma_probabilidades = sum(probabilidades.values())
    
    # Normalizamos las probabilidades dividiendo cada una por la suma total
    probabilidades_normalizadas = {evento: prob / suma_probabilidades for evento, prob in probabilidades.items()}
    
    return probabilidades_normalizadas

# Datos de ejemplo: lista de observaciones
datos = [(True, True), (False, True), (True, True), (True, False), (False, False)]

# Eventos para los cuales queremos calcular la probabilidad condicionada
evento_A = True
evento_B = True

# Calculamos y mostramos la probabilidad condicionada
print(f"Datos: {datos}")
print(f"Evento A: {evento_A}")
print(f"Evento B: {evento_B}")
print(f"Probabilidad condicionada P(B|A): {probabilidad_condicionada(evento_A, evento_B, datos)}")

# Ejemplo de normalizacion de probabilidades
probabilidades = {'A': 0.3, 'B': 0.5, 'C': 0.2}
print(f"Probabilidades antes de la normalizacion: {probabilidades}")
print(f"Probabilidades normalizadas: {normalizar_probabilidades(probabilidades)}")

