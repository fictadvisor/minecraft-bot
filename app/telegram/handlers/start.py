from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager, ShowMode, StartMode

from app.telegram.keyboards.start import start_keyboard
from app.telegram.states.form import Form


async def start(message: Message) -> None:
    await message.answer("Для реєстрації потрібно заповнити форму", reply_markup=start_keyboard())


async def register(callback: CallbackQuery, dialog_manager: DialogManager) -> None:
    await callback.message.edit_reply_markup()
    await dialog_manager.start(Form.full_name, mode=StartMode.RESET_STACK, show_mode=ShowMode.SEND)
