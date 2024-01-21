import logging

from app.api.factory import create_app
from app.discord.factory import create_discord_bot
from app.services.telegram import TelegramService
from app.telegram.factory import create_telegram_bot, create_dispatcher
from app.settings import settings

telegram_bot = create_telegram_bot(token=settings.TELEGRAM_TOKEN.get_secret_value())
dispatcher = create_dispatcher()
discord_bot = create_discord_bot()
TelegramService(telegram_bot, discord_bot)
app = create_app(
    telegram_bot=telegram_bot,
    discord_bot=discord_bot,
    dispatcher=dispatcher,
    webhook_secret=settings.TELEGRAM_SECRET.get_secret_value(),
)

logging.basicConfig(level="DEBUG")
