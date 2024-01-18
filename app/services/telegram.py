from app.settings import settings
from aiogram import Bot

from app.messages.form import REGISTER_FORM
from app.telegram.keyboards.verification import verification_keyboard
from app.types.form import Form


class TelegramService:
    @staticmethod
    async def send_registration(data: Form, bot: Bot) -> None:
        await bot.send_message(
            chat_id=settings.CHAT_ID,
            text=await REGISTER_FORM.render_async(**data),
            reply_markup=verification_keyboard()
        )
