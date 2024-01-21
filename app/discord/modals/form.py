
import discord
from discord import ui

from app.enums.service_type import ServiceType
from app.services.telegram import TelegramService


class Form(ui.Modal, title='Реєстрація'):
    name: ui.TextInput = ui.TextInput(label="Введіть ім'я", placeholder="Шевченко Тарас Григорович", required=True)
    nickname: ui.TextInput = ui.TextInput(label="Нікнейм у Minecraft", placeholder="Notch", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        await TelegramService.get_instance().send_registration({
            "name": str(self.name),
            "nickname": str(self.nickname),
            "discord_nickname": str(interaction.user.global_name)
        }, service_type=ServiceType.DISCORD, user_id=interaction.user.id)
        await interaction.response.edit_message(content="Дякуємо за реєтрацію", view=None)
