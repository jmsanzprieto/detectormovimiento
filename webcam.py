import cv2
from playsound import playsound
import threading
import time
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Datos del correo
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_BCC = os.getenv("EMAIL_BCC") 
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")

def reproducir_alarma():
    """Reproduce el sonido de la alarma durante 4 segundos."""
    inicio = time.time()
    while time.time() - inicio < 4:
        playsound('alarm.mp3')

def enviar_correo(nombre_foto):
    """Envía un correo con la foto adjunta."""
    try:
        # Crear el mensaje
        msg = EmailMessage()
        msg["Subject"] = "Movimiento detectado - Foto capturada"
        msg["From"] = EMAIL_FROM
        msg["To"] = EMAIL_TO
        msg["Bcc"] = EMAIL_BCC 
        msg.set_content("Se detectó movimiento. Adjuntamos una foto tomada en el momento del evento.")

        # Adjuntar la foto
        with open(nombre_foto, "rb") as file:
            msg.add_attachment(file.read(), maintype="image", subtype="jpeg", filename=nombre_foto)

        # Conectar al servidor SMTP y enviar el correo
        with smtplib.SMTP_SSL(SMTP_SERVER, int(SMTP_PORT)) as server:
            server.login(EMAIL_FROM, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"Correo enviado a {EMAIL_TO} con la foto {nombre_foto}")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

def guardar_foto(frame):
    """Guarda una foto en caso de múltiples detecciones y envía un correo."""
    nombre_foto = f"foto_movimiento_{int(time.time())}.jpg"
    cv2.imwrite(nombre_foto, frame)
    print(f"Foto guardada: {nombre_foto}")
    enviar_correo(nombre_foto)

def detectar_movimiento():
    # Inicializa la cámara
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: No se pudo acceder a la cámara.")
        return

    print("Detectando movimiento... Presiona 'Ctrl + C' para salir.")

    # Variables para comparar frames y contador de movimientos
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()
    contador_movimientos = 0
    foto_guardada = False

    while True:
        try:
            # Calcula la diferencia entre frames consecutivos
            diff = cv2.absdiff(frame1, frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)

            # Umbral para detectar movimiento
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations=3)

            # Encuentra contornos en la imagen
            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            movimiento_detectado = False
            for contour in contours:
                if cv2.contourArea(contour) < 30000:  # Mayor número --> menos sensible
                    continue

                # Incrementa el contador y muestra el mensaje
                movimiento_detectado = True
                contador_movimientos += 1
                print(f"Movimiento detectado. Total: {contador_movimientos}")
                threading.Thread(target=reproducir_alarma).start()
                break

            if movimiento_detectado and contador_movimientos > 4 and not foto_guardada:
                guardar_foto(frame1)
                foto_guardada = True

            if not movimiento_detectado:
                # Reinicia el contador y el estado de la foto si no hay movimientos
                contador_movimientos = 0
                foto_guardada = False

            # Actualiza los frames para la comparación
            frame1 = frame2
            ret, frame2 = cap.read()

        except KeyboardInterrupt:
            print("Finalizando el programa...")
            break

    # Libera recursos
    cap.release()

if __name__ == "__main__":
    detectar_movimiento()
