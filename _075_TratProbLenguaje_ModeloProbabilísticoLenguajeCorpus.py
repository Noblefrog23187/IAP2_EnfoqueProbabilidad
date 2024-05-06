import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import LidstoneProbDist
from nltk.corpus import brown

# Descargar los recursos necesarios de NLTK (solo se necesita hacer una vez)
nltk.download('punkt')
nltk.download('brown')

# Obtener el corpus Brown
corpus = brown.words()

# Preprocesamiento del corpus: tokenizacion y conversion a minusculas
corpus = [word.lower() for word in corpus if word.isalpha()]

# Crear un modelo de probabilidad usando Lidstone (para suavizado)
# Se usa LidstoneProbDist con un valor de gamma=0.1 para evitar la probabilidad de cero
model = LidstoneProbDist(nltk.FreqDist(corpus), gamma=0.1)

# Funcion para predecir la probabilidad de una palabra dada una historia
def predict_next_word(history):
    # Tokenizar la historia
    tokens = word_tokenize(history.lower())
    # Obtener la ultima palabra de la historia
    last_word = tokens[-1]
    # Calcular la probabilidad de la siguiente palabra dado el contexto anterior
    prob = model.prob(last_word)
    return prob

# Ejemplo de uso
history = "in the"
next_word_prob = predict_next_word(history)
print("Probabilidad de la siguiente palabra despues de 'in the':", next_word_prob)

