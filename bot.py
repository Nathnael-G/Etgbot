from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# ============================================================
# 🔑 IMPORTANT: Replace these with your actual values!
# ============================================================
BOT_TOKEN = ""  # Paste your token from Step 1
WEB_APP_URL = "https://glittery-sprite-3de50c.netlify.app/"  # Your Web App link from Step 2
# ============================================================

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    This function runs when a user sends the /start command.
    It sends a welcome message with a button to open the Web App.
    """
    
    # 1. Create a button that opens your Web App
    web_app_button = InlineKeyboardButton(
        "🚀 Open Web App", 
        web_app=WebAppInfo(url=WEB_APP_URL)
    )
    
    # 2. Wrap the button in a keyboard markup
    reply_markup = InlineKeyboardMarkup([[web_app_button]])
    
    # 3. Create the welcome message
    welcome_text = (
        "👋 Welcome to Our Bot!\n\n"
        "We're excited to have you here. "
        "Click the button below to explore our powerful web app.\n\n"
        "✨ Features include:\n"
        "• Interactive dashboard\n"
        "• Real-time updates\n"
        "• And much more!"
    )
    
    # 4. Send the message with the button
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
    # 1. Create the Application using your bot token
    print("🤖 Starting bot...")
    app = Application.builder().token(BOT_TOKEN).build()
    
    # 2. Register command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    
    # 3. Start the bot
    print("✅ Bot is running! Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == '__main__':
    main()