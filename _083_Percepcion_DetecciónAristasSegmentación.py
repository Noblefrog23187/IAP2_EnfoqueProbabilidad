import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar una imagen en escala de grises (asegurate de tener una imagen disponible)
imagen_original = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar el operador Sobel para detectar bordes
gradiente_x = cv2.Sobel(imagen_original, cv2.CV_64F, 1, 0, ksize=3)
gradiente_y = cv2.Sobel(imagen_original, cv2.CV_64F, 0, 1, ksize=3)

# Calcular el gradiente total
gradiente_total = np.sqrt(gradiente_x**2 + gradiente_y**2)

# Mostrar las imagenes original y el gradiente total
plt.subplot(1, 2, 1)
plt.imshow(imagen_original, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gradiente_total, cmap='gray')
plt.title('Gradiente Total (Deteccion de Bordes)')
plt.axis('off')

plt.show()

def segmentar_con_grabcut(imagen, bounding_box):
    seg = np.zeros(imagen.shape[:2], np.uint8)
    x, y, width, height = bounding_box
    seg[y:y+height, x:x+width] = 1

    background_model = np.zeros((1, 65), np.float64)
    foreground_model = np.zeros((1, 65), np.float64)

    cv2.grabCut(imagen, seg, bounding_box, background_model, foreground_model, 5, cv2.GC_INIT_WITH_RECT)

    mask_nueva = np.where((seg == 2) | (seg == 0), 0, 1).astype("uint8")
    return mask_nueva

# Ejemplo de uso
bounding_box_ejemplo = (100, 100, 200, 200)  # Coordenadas x, y, ancho, alto
mascara_segmentada = segmentar_con_grabcut(imagen_original, bounding_box_ejemplo)

# Mostrar la mascara segmentada
plt.imshow(mascara_segmentada, cmap='gray')
plt.title('Mascara Segmentada')
plt.axis('off')
plt.show()

