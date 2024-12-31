import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar el bot de Telegram
TOKEN = "7721418131:AAGRzdKFFHRfHjdtfAdZCc7l4N8HH1jKzjE"
application = ApplicationBuilder().token(TOKEN).build()

# Función para manejar el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responde con un saludo cuando el usuario envía el comando /start."""
    await update.message.reply_text("Hola Mundo! 👋")

# Añadir manejadores al bot
application.add_handler(CommandHandler("start", start))

@app.route('/webhook', methods=['POST'])
def webhook():
    """Procesa las actualizaciones enviadas por Telegram."""
    # Decodificar la solicitud entrante
    json_str = request.get_data().decode('utf-8')
    update = Update.de_json(json_str, application.bot)

    # Procesar la actualización con el bot
    application.process_update(update)
    return 'OK'

if __name__ == "__main__":
    # Configurar el webhook
    webhook_url = f"https://prueba2-zqoh.onrender.com"
    application.bot.set_webhook(webhook_url)

    # Ejecutar la aplicación Flask
    port = int(os.environ.get("PORT", 5000))  # Render asigna automáticamente el puerto
    app.run(host="0.0.0.0", port=port)

