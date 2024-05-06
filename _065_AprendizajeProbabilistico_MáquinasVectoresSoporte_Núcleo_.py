# Importar las bibliotecas necesarias
from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generar datos de ejemplo
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, random_state=1)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Crear el clasificador SVM con nucleo probabilistico
clf = svm.SVC(kernel='rbf', probability=True)
clf.fit(X_train, y_train)

# Calcular la precision del modelo
accuracy = clf.score(X_test, y_test)
print(f'Precision del modelo: {accuracy}')
