from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.enums.service_type import ServiceType
from app.telegram.keyboards.types.confirm_user import ConfirmUser


def verification_keyboard(service_type: ServiceType, user_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text="Підтвердити", callback_data=ConfirmUser(type=service_type, user_id=user_id))

    return builder.as_markup()
