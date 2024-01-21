import logging

from aiogram.types import CallbackQuery

from app.services.telegram import TelegramService
from app.telegram.keyboards.types.confirm_user import ConfirmUser


async def confirm(callback: CallbackQuery) -> None:
    text = callback.message.text
    text = text.replace("🟥", "✅")
    await callback.message.edit_text(
        text=text,
        reply_markup=None
    )


async def confirm_user(callback: CallbackQuery, callback_data: ConfirmUser) -> None:
    text = callback.message.text
    text = text.replace("🟥", "✅")
    try:
        await TelegramService.get_instance().send_confirmation(callback_data.user_id, callback_data.type)
        await callback.message.edit_text(
            text=text,
            reply_markup=None
        )
    except Exception as e:
        logging.error(e)
