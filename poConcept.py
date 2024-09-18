import smtplib
import schedule
import time
from datetime import datetime

# Configuración del servidor SMTP (Ejemplo con Gmail)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL = 'jesusramon0508@gmail.com'      #  correo
PASSWORD = 'xjxj hlxg orkr dqvl'        #  contraseña de aplicacionb

# Función para enviar una alerta por correo
def enviar_alerta(destinatario, asunto, mensaje):
    try:
        # Conexión al servidor SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Seguridad
            server.login(EMAIL, PASSWORD)

            # Formateo del correo
            mensaje_correo = f'Subject: {asunto}\n\n{mensaje}'
            server.sendmail(EMAIL, destinatario, mensaje_correo)
            print(f'Alerta enviada a {destinatario}')
    except Exception as e:
        print(f'Error al enviar la alerta: {e}')

# Función que define la tarea de enviar una alerta en una fecha específica
def programar_alerta(destinatario, asunto, mensaje, fecha_alerta):
    def tarea_alerta():
        if datetime.now() >= fecha_alerta:
            enviar_alerta(destinatario, asunto, mensaje)
            return schedule.CancelJob  # Cancelar tarea tras ejecución

    # Programación del chequeo cada minuto
    schedule.every(1).minutes.do(tarea_alerta)

# Ejemplo de uso
if __name__ == "__main__":
    # Configuración de la alerta
    destinatario = 'jesus.ruiz.soto@uabc.edu.mx'
    asunto = 'Alerta programada'
    mensaje = 'Esta es una alerta programada desde el sistema de prueba.'
    
    # Fecha y hora de la alerta (usar el formato YYYY, MM, DD, HH, MM)
    fecha_alerta = datetime(2024, 9, 18, 13, 31)  # Ajustar esta fecha

    # Programar la alerta
    programar_alerta(destinatario, asunto, mensaje, fecha_alerta)

    print('Alerta programada, esperando ejecución...')
    
    # Bucle principal que chequea las tareas programadas
    while True:
        schedule.run_pending()
        time.sleep(1)
