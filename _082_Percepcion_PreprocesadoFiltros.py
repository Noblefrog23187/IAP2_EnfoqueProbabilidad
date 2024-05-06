import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
imagen = cv2.imread('imagen.jpg')

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro de suavizado Gaussiano
imagen_suavizada = cv2.GaussianBlur(imagen_gris, (5, 5), 0)

# Aplicar un filtro de deteccion de bordes (diferencia de sobel)
sobelx = cv2.Sobel(imagen_suavizada, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(imagen_suavizada, cv2.CV_64F, 0, 1, ksize=5)
bordes = np.sqrt(sobelx**2 + sobely**2)

# Mostrar las imzgenes originales y procesadas
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(imagen_suavizada, cmap='gray')
plt.title('Imagen Suavizada')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(bordes, cmap='gray')
plt.title('Deteccion de Bordes')
plt.axis('off')

plt.show()


