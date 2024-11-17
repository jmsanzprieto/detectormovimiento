# Detección de Movimiento con Alarma y Notificación por Correo Electrónico

Este proyecto utiliza la cámara del PC y el procesamiento de imágenes en tiempo real para detectar movimiento a través de la cámara web. Cuando se detecta movimiento, se reproduce una alarma sonora y se envía un correo electrónico con una foto tomada en el momento del evento. Además, se registra cada envío en un archivo JSON con la fecha, hora y nombre de la imagen adjunta.

## Características

- **Detección de movimiento**: Utiliza procesamiento de imágenes para identificar cambios significativos entre frames consecutivos de la cámara.
- **Alarma sonora**: Reproduce un sonido de alarma durante 4 segundos cuando se detecta movimiento.
- **Notificación por correo electrónico**: Envía un correo con la foto capturada como archivo adjunto a los destinatarios configurados.
- **Registro de eventos**: Guarda un registro en un archivo JSON (`registros_envios.json`) con la fecha, hora y nombre de la imagen enviada por correo.

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instalados los siguientes requisitos:

- **Python 3.x**
- **Dependencias de Python**:
  - `opencv-python`: Para la captura de vídeo y procesamiento de imágenes.
  - `playsound`: Para reproducir el sonido de la alarma.
  - `python-dotenv`: Para manejar las variables de entorno.
  - `smtplib`: Para enviar correos electrónicos.
  - `email.message`: Para crear y enviar el correo con el archivo adjunto.
- **Archivo de configuración `.env`**:
  Contiene las credenciales necesarias para el envío de correos electrónicos. 

## Instalación

Instala las dependencias necesarias ejecutando el siguiente comando:

```bash
pip install opencv-python playsound python-dotenv
