from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram_dialog import setup_dialogs

from app.telegram.handlers import router as main_router
from app.telegram.middlewares.throttling import ThrottlingMiddleware
from app.settings import settings


async def on_startup(bot: Bot, dispatcher: Dispatcher) -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(
        settings.WEBHOOK_URL,
        drop_pending_updates=True,
        secret_token=settings.TELEGRAM_SECRET.get_secret_value(),
        allowed_updates=dispatcher.resolve_used_update_types()
    )


async def on_shutdown(bot: Bot) -> None:
    await bot.delete_webhook(drop_pending_updates=True)


def create_dispatcher() -> Dispatcher:
    dispatcher = Dispatcher()
    setup_dialogs(dispatcher)

    dispatcher.include_router(main_router)
    dispatcher.startup.register(on_startup)
    dispatcher.shutdown.register(on_shutdown)

    dispatcher.update.middleware(ThrottlingMiddleware())

    return dispatcher


def create_telegram_bot(token: str) -> Bot:
    return Bot(token=token, parse_mode=ParseMode.HTML)
