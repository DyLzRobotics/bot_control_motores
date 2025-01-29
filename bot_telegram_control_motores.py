import serial
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token del bot (cámbialo por el real)
TOKEN = "7900027175:AAGbnNQTsM5YKGv8krenhVz4XCwxki-bcMU"

# Configuración del puerto serial
SERIAL_PORT = "COM3"  # Cambia esto al puerto correcto en Windows, "/dev/ttyUSB0" en Linux
BAUD_RATE = 9600


class ArduinoController:
    """Clase para manejar la conexión con Arduino"""

    def __init__(self, port, baud_rate):
        self.port = port
        self.baud_rate = baud_rate
        self.serial_connection = None
        self.connect_to_arduino()

    def connect_to_arduino(self):
        """Intenta conectarse al puerto serial con reintentos"""
        try:
            self.serial_connection = serial.Serial(self.port, self.baud_rate, timeout=2)
            time.sleep(2)  # Esperar a que Arduino se estabilice
            print("✅ Conexión con Arduino establecida correctamente.")
        except serial.SerialException as e:
            print(f"⚠️ Error al conectar con Arduino: {e}")
            self.serial_connection = None

    def send_command(self, command):
        """Envía un comando a Arduino y recibe respuesta"""
        if self.serial_connection and self.serial_connection.is_open:
            try:
                self.serial_connection.write(command.encode() + b'\n')  # Enviar comando
                print(f"📤 Comando enviado: {command}")

                # Esperar una respuesta de Arduino (opcional)
                response = self.serial_connection.readline().decode().strip()
                if response:
                    print(f"📥 Respuesta de Arduino: {response}")
                return response

            except serial.SerialException as e:
                print(f"⚠️ Error al escribir en el puerto serial: {e}")
        else:
            print("⚠️ No hay conexión con Arduino. Intentando reconectar...")
            self.connect_to_arduino()

        return None


# Crear instancia de la conexión con Arduino
arduino = ArduinoController(SERIAL_PORT, BAUD_RATE)


# 📌 Función para recibir comandos y enviarlos al Arduino
async def move_robot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    datos = context.args

    if not datos or len(datos) < 3:
        await update.message.reply_text(
            "⚠️ Formato incorrecto. Usa:\n"
            "🔹 /Move <parte> <posición> <acción>\n"
            "Ejemplo: /Move brazo izquierdo rotar"
        )
        return

    # Extraer argumentos
    parte, posicion, accion = datos[:3]

    # Construcción del comando
    comando = f"{parte},{posicion},{accion}"
    print(f"📨 Enviando a Arduino: {comando}")

    # Enviar comando a Arduino
    respuesta = arduino.send_command(comando)

    # Responder al usuario
    msg = f"✅ Orden enviada:\n- Parte: {parte}\n- Posición: {posicion}\n- Acción: {accion}"
    if respuesta:
        msg += f"\n📩 Respuesta de Arduino: {respuesta}"

    await update.message.reply_text(msg)


# 📌 Información general del robot
async def info_robot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Información del robot:\n\n"
        "🔹 /Info - Información general\n"
        "🔹 /InfoMove - Partes y movimientos disponibles\n"
        "🔹 /Move <parte> <posición> <acción> - Mover robot\n"
        "🦾 Motores: 2x brazos (25kg), 2x manos (2.5kg), 2x ojos (9g)..."
    )


# 📌 Lista de partes y acciones del robot
async def infomove_robot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Partes y acciones disponibles:\n"
        "🦾 brazo: adelante, atrás, rotar\n"
        "🖐️ mano: abrir, cerrar, girar\n"
        "💪 codo: adelante, atrás\n"
        "👀 ojos: izquierda, derecha\n"
        "🗣️ boca: abrir, cerrar\n"
        "🦿 cadera: rotar\n"
    )


# 📌 Configuración del bot de Telegram
def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("Move", move_robot))
    application.add_handler(CommandHandler("Info", info_robot))
    application.add_handler(CommandHandler("InfoMove", infomove_robot))

    print("🤖 Bot de Telegram ejecutándose...")
    application.run_polling()


# 📌 Ejecutar bot
if __name__ == "__main__":
    main()
