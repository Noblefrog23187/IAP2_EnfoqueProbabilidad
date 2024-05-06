from sklearn.feature_extraction.text import TfidfVectorizer

# Datos de ejemplo (documentos)
documents = [
    "El gato come pescado.",
    "El perro juega en el parque.",
    "Los pajaros vuelan en el cielo.",
    "El gato y el perro son amigos."
]

# Inicializar el vectorizador TF-IDF
vectorizer = TfidfVectorizer()

# Ajustar el vectorizador a los datos y transformar los documentos en vectores TF-IDF
tfidf_matrix = vectorizer.fit_transform(documents)

# Palabras del vocabulario
vocab = vectorizer.get_feature_names_out()

# Consulta de ejemplo
query = "gato come pescado"

# Transformar la consulta en un vector TF-IDF
query_vector = vectorizer.transform([query])

# Calcular la similitud de coseno entre la consulta y los documentos
from sklearn.metrics.pairwise import cosine_similarity
similarities = cosine_similarity(query_vector, tfidf_matrix)

# Obtener los indices de los documentos mas similares
top_similar_indices = similarities.argsort()[0][::-1]

# Imprimir los documentos mas similares a la consulta
print("Documentos mas similares a la consulta:")
for idx in top_similar_indices:
    print(documents[idx])

