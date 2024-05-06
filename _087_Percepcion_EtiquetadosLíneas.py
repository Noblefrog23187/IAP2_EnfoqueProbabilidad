import cv2  # Importa la biblioteca OpenCV
import numpy as np  # Importa la biblioteca NumPy

# Cargar la imagen
image = cv2.imread('imagen.jpg')  # Lee la imagen desde el archivo 'imagen.jpg'
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convierte la imagen a escala de grises

# Aplicar el detector de bordes Canny
edges = cv2.Canny(gray, 50, 150, apertureSize=3)  # Aplica el detector de bordes Canny

# Detectar lineas mediante la transformada de Hough
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)  # Detecta lineas usando la transformada de Hough

# Dibujar las lineas detectadas en la imagen original
if lines is not None:  # Verifica si se detectaron lineas
    for line in lines:  # Itera sobre todas las lineas detectadas
        rho, theta = line[0]  # Obtiene los parametros rho y theta de la linea
        a = np.cos(theta)  # Calcula el coseno de theta
        b = np.sin(theta)  # Calcula el seno de theta
        x0 = a * rho  # Calcula las coordenadas x del punto de interseccion
        y0 = b * rho  # Calcula las coordenadas y del punto de interseccion
        x1 = int(x0 + 1000 * (-b))  # Calcula la coordenada x del primer punto de la linea
        y1 = int(y0 + 1000 * (a))   # Calcula la coordenada y del primer punto de la linea
        x2 = int(x0 - 1000 * (-b))  # Calcula la coordenada x del segundo punto de la linea
        y2 = int(y0 - 1000 * (a))   # Calcula la coordenada y del segundo punto de la linea
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Dibuja la linea sobre la imagen original

# Mostrar la imagen resultante con las lineas detectadas
cv2.imshow('Lineas Detectadas', image)  # Muestra la imagen con las lineas detectadas
cv2.waitKey(0)  # Espera a que se presione una tecla
cv2.destroyAllWindows()  # Cierra todas las ventanas abiertas

