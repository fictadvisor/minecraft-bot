from aiogram.filters.callback_data import CallbackData

from app.enums.service_type import ServiceType


class ConfirmUser(CallbackData, prefix="confirm"):
    type: ServiceType
    user_id: int
