from typing import Optional

import discord
from discord import ui

from app.services.telegram import TelegramService


class Form(ui.Modal, title='Реєстрація'):
    full_name: str = ui.TextInput(label="Введіть ПІБ", placeholder="Шевченко Тарас Григорович", required=True)
    place_of_study: Optional[str] = ui.TextInput(label="Введіть місце навчання", required=False)
    nickname: Optional[str] = ui.TextInput(label="Нікнейм у Minecraft", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        await TelegramService.send_registration({
            "first_name": str(self.full_name),
            "place_of_study": str(self.place_of_study),
            "nickname": str(self.nickname)
        }, bot=interaction.client.telegram_bot)
        await interaction.response.edit_message(content="Дякуємо за реєтрацію", view=None)
