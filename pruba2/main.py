from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

# Función para manejar el mensaje "Hello World!"
async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello World!")

# Configurar el token del bot
TOKEN = "7721418131:AAGRzdKFFHRfHjdtfAdZCc7l4N8HH1jKzjE"
"
application = ApplicationBuilder().token(TOKEN).build()

# Función para manejar el comando /help
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ayuda del bot: esto es un bot para desplegar ")

# Añadir manejadores
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, say_hello))
application.add_handler(CommandHandler("help", help))

# Iniciar el bot
print("Running")
application.run_polling(allowed_updates=Update.ALL_TYPES)



