import speech_recognition as sr
import random

# Funcion para reconocimiento de voz
def recognize_speech():
    recognizer = sr.Recognizer()  # Creamos un objeto reconocedor
    with sr.Microphone() as source:  # Utilizamos el microfono como fuente de audio
        print("Di algo:")  # Pedimos al usuario que hable
        audio = recognizer.listen(source)  # Escuchamos el audio del microfono
    try:
        text = recognizer.recognize_google(audio, language='es-ES')  # Reconocemos el audio utilizando Google Speech Recognition
        return text
    except sr.UnknownValueError:  # Manejamos errores si no se pudo reconocer el habla
        print("No se pudo entender lo que dijiste")
        return ""
    except sr.RequestError as e:  # Manejamos errores de conexion
        print("Error en la solicitud; {0}".format(e))
        return ""

# Funcion para realizar un razonamiento probabilistico simple
def probabilistic_reasoning():
    probability = random.random()  # Generamos un numero aleatorio entre 0 y 1
    if probability < 0.5:
        return "Si"
    else:
        return "No"

# Funcion principal
def main():
    speech = recognize_speech()  # Llamamos a la funcion de reconocimiento de voz
    if speech:  # Si se reconocio algo
        print("Entendido: " + speech)
        print("Es correcto, Probabilidad de ser correcto:", probabilistic_reasoning())  # Llamamos a la funcion de razonamiento probabilistico

if __name__ == "__main__":
    main()  # Llamamos a la funcion principal si este script se ejecuta directamente
