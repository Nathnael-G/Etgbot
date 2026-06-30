from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# ============================================================
# 🔑 Read tokens from environment variables
# ============================================================
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables!")

WEB_APP_URL = os.environ.get("WEB_APP_URL", "https://glittery-sprite-3de50c.netlify.app/")

# Get the Render URL from environment (Render sets this automatically)
RENDER_URL = os.environ.get("RENDER_EXTERNAL_URL", "https://etgbot.onrender.com")
# ============================================================

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send welcome message when /start is issued."""
    web_app_button = InlineKeyboardButton(
        "🚀 Open Web App", 
        web_app=WebAppInfo(url=WEB_APP_URL)
    )
    reply_markup = InlineKeyboardMarkup([[web_app_button]])
    
    welcome_text = (
        "👋 Welcome to Our Bot!\n\n"
        "We're excited to have you here. "
        "Click the button below to explore our powerful web app.\n\n"
        "✨ Features include:\n"
        "• Interactive dashboard\n"
        "• Real-time updates\n"
        "• And much more!"
    )
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a help message when /help is issued."""
    help_text = (
        "🤖 Available Commands:\n"
        "/start - Welcome message with Web App link\n"
        "/help - Show this help message\n"
        "/about - Learn more about us"
    )
    await update.message.reply_text(help_text)

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send an about message when /about is issued."""
    about_text = (
        "ℹ️ About This Bot\n\n"
        "This bot connects you to our innovative Web App. "
        "Built with ❤️ using Telegram's Mini App platform.\n\n"
        "📱 Open the Web App to access all features!"
    )
    await update.message.reply_text(about_text)

def main():
    """Start the bot using webhook."""
    print("🤖 Starting bot with webhook...")
    
    # Create the Application
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Register command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    
    # Set up webhook
    webhook_url = f"{RENDER_URL}/webhook"
    print(f"🔗 Setting webhook to: {webhook_url}")
    
    # Start the webhook
    app.run_webhook(
        listen="0.0.0.0",  # Listen on all interfaces
        port=int(os.environ.get("PORT", 10000)),  # Use Render's port
        url_path=BOT_TOKEN,  # Use token as path for security
        webhook_url=webhook_url
    )

if __name__ == '__main__':
    main()