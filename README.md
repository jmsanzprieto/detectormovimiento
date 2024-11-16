# Detección de Movimiento con Alarma y Notificación por Correo Electrónico

Este proyecto utiliza la cámara del pc y el procesamiento de imágenes en tiempo real para detectar movimiento a través de la cámara web. Cuando se detecta movimiento, se reproduce una alarma sonora y se envía un correo electrónico con una foto tomada en el momento del evento. El correo electrónico contiene la foto como archivo adjunto y se envía a una lista de destinatarios definida en el archivo `.env`.

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instalados los siguientes requisitos:

- Python 3.x
- `opencv-python` para la captura de vídeo y procesamiento de imágenes.
- `playsound` para reproducir el sonido de la alarma.
- `python-dotenv` para manejar las variables de entorno.
- `smtplib` para enviar correos electrónicos.
- `email.message` para crear y enviar el correo con el archivo adjunto.

Puedes instalar las dependencias necesarias utilizando `pip`:

```bash
pip install opencv-python playsound python-dotenv
