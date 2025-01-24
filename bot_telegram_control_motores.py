from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7900027175:AAGbnNQTsM5YKGv8krenhVz4XCwxki-bcMU"
#Lista de movimiento de robor
async def muve_robot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass
#Informacion del robot y como usar el bot
async  def info_robot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass
#Informacion de las partes del robot y como usar
async  def infomuve_robot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass
application = ApplicationBuilder().token(TOKEN).build()
application.add_handler( CommandHandler("Muve", ))
application.add_handler( CommandHandler("Info", ))
application.add_handler( CommandHandler("InfoMuve", ))
#Reaciona lo que envia el usuario
application.run_polling(allowed_updates=Update.ALL_TYPES)
