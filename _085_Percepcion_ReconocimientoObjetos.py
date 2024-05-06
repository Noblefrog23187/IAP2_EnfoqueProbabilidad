import cv2

# Cargar el clasificador pre-entrenado para deteccion de rostros
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Inicializar la camara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar rostros en la imagen
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Dibujar un rectangulo alrededor de cada rostro detectado
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Mostrar la imagen con los rostros detectados
    cv2.imshow('Deteccion de Rostros', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


