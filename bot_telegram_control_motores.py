import serial
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token del bot
TOKEN = "7900027175:AAGbnNQTsM5YKGv8krenhVz4XCwxki-bcMU"  # Cambia esto por tu token real

# Configuración de comunicación serial
SERIAL_PORT = "COM1"  # Cambia esto al puerto correspondiente
BAUD_RATE = 9600


# Lista de movimientos del robot
async def move_robot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Obtener argumentos del comando
    datos = context.args

    if not datos or len(datos) < 3:
        await update.message.reply_text(
            "Por favor, especifica la parte del cuerpo, posición y acción que el robot debe realizar.\n"
            "Ejemplo: /Move brazo izquierdo rotar"
        )
        return

    # Extraer los argumentos
    parte = datos[0]
    posicion = datos[1]
    accion = datos[2]

    # Enviar respuesta al usuario
    await update.message.reply_text(
        f"Has indicado los siguientes parámetros:\n"
        f"  - Parte del robot: {parte}\n"
        f"  - Posición: {posicion}\n"
        f"  - Acción: {accion}\n\n"
        f"Procesando solicitud..."
    )
    print(f"Datos recibidos: {datos}")

    try:
        # Conexión serial con Arduino
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2) as serialArduino:
            # Crear la cadena de comando
            comando = f"{parte},{posicion},{accion}\n"
            serialArduino.write(comando.encode())  # Convertir a byte string
            print(f"Comando enviado: {comando}")
    except serial.SerialException as e:
        await update.message.reply_text(
            "Error al comunicarse con el Arduino. Verifica la conexión serial."
        )
        print(f"Error serial: {e}")

# Información general del robot
async def info_robot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Información del robot y cómo usar este bot:\n\n"
        "Comandos disponibles:\n"
        "  /Info - Información general sobre el robot.\n"
        "  /InfoMove - Lista de las partes del robot y acciones posibles.\n"
        "  /Move - Ejecuta un movimiento en una parte específica del robot.\n\n"
        "Detalles del robot:\n"
        "  - Motores de los brazos: 2 motores (25 kg de capacidad cada uno).\n"
        "  - Motores de las manos: 2 motores (2.5 kg de capacidad cada uno).\n"
        "  - Motores de la cabeza:\n"
        "      * Cuello y boca: 2 motores (25 kg cada uno).\n"
        "      * Ojos: 2 motores (2.5 kg cada uno).\n"
        "      * Detalles adicionales: 2 motores (9 g cada uno)."
    )


# Información de las partes y acciones del robot
async def infomove_robot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Partes y acciones disponibles para el robot:\n\n"
        "Partes del robot:\n"
        "  - cabeza: rotar, mover\n"
        "  - mano: abrir, cerrar, girar\n"
        "  - codo: adelante, atrás, rotar\n"
        "  - hombro: adelante, atrás, lateral\n"
        "  - ojos: abrir, cerrar, izquierda, derecha\n"
        "  - boca: abrir, cerrar\n"
        "  - cuello: rotar\n"
        "  - cadera: rotar\n\n"
    )

# Configuración principal del bot
def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Manejadores de comandos
    application.add_handler(CommandHandler("Move", move_robot))
    application.add_handler(CommandHandler("Info", info_robot))
    application.add_handler(CommandHandler("InfoMove", infomove_robot))

    # Iniciar el bot
    application.run_polling()


if __name__ == "__main__":
    main()
