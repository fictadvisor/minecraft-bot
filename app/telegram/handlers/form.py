from typing import Dict, Any

from aiogram import Bot
from aiogram.enums import ContentType
from aiogram.types import Message, User
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Const

from app.services.telegram import TelegramService
from app.telegram.states.form import Form


async def full_name(message: Message, message_input: MessageInput, manager: DialogManager) -> None:
    manager.dialog_data["full_name"] = message.text
    await manager.next()


async def place_of_study(message: Message, message_input: MessageInput, manager: DialogManager):
    manager.dialog_data["place_of_study"] = message.text
    await manager.next()


async def nickname(message: Message, message_input: MessageInput, manager: DialogManager):
    manager.dialog_data["nickname"] = message.text
    data = manager.dialog_data
    await manager.done(data)


async def result(data: Dict[str, Any], manager: DialogManager) -> None:
    user: User = manager.middleware_data["event_from_user"]
    bot: Bot = manager.middleware_data["bot"]
    await TelegramService.send_registration(data, bot)
    await bot.send_message(user.id, "Дякуємо за реєстрацію!")


form = Dialog(
    Window(
        Const("Введіть ПІБ"),
        MessageInput(full_name, content_types=[ContentType.TEXT]),
        state=Form.full_name
    ),
    Window(
        Const("Введіть місце навчання"),
        MessageInput(place_of_study, content_types=[ContentType.TEXT]),
        state=Form.place_of_study
    ),
    Window(
        Const("Введіть нікнейм в Minecraft"),
        MessageInput(nickname, content_types=[ContentType.TEXT]),
        state=Form.nickname
    ),
    on_close=result
)
