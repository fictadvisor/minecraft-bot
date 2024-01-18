from aiogram.types import CallbackQuery


async def confirm(callback: CallbackQuery) -> None:
    text = callback.message.text
    text = text.replace("🟥", "✅")
    await callback.message.edit_text(
        text=text,
        reply_markup=None
    )
