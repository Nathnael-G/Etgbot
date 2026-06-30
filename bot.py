import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables!")

WEB_APP_URL = os.environ.get("WEB_APP_URL", "https://glittery-sprite-3de50c.netlify.app/")
# ============================================================

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    This function runs when a user sends the /start command.
    It sends a welcome message with a button to open the Web App.
    """
    
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
    
    await update.message.reply_text(
        welcome_text, 
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a helpful message when the user sends /help."""
    help_text = (
        "🤖 Available Commands:\n"
        "/start - Welcome message with Web App link\n"
        "/help - Show this help message\n"
        "/about - Learn more about us"
    )
    await update.message.reply_text(help_text)

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send an about message when the user sends /about."""
    about_text = (
        "ℹ️ About This Bot\n\n"
        "This bot connects you to our innovative Web App. "
        "Built with ❤️ using Telegram's Mini App platform.\n\n"
        "📱 Open the Web App to access all features!"
    )
    await update.message.reply_text(about_text)

def main():
    """
    The main function that sets up and runs the bot.
    """
    print("🤖 Starting bot...")
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    
    print("✅ Bot is running! Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == '__main__':
    main()