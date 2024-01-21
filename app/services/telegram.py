from typing import Optional

import discord
from discord import Client

from app.enums.service_type import ServiceType
from app.settings import settings
from aiogram import Bot

from app.messages.form import REGISTER_FORM, CONFIRM
from app.telegram.keyboards.verification import verification_keyboard
from app.types.form import Form


class TelegramService:
    _instance: Optional["TelegramService"] = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, telegram_bot: Bot, discord_bot: Client):
        self.telegram_bot = telegram_bot
        self.discord_bot = discord_bot

    @classmethod
    def get_instance(cls) -> "TelegramService":
        if cls._instance is None:
            raise Exception()
        return cls._instance

    async def send_registration(self, data: Form, service_type: ServiceType, user_id: int) -> None:
        await self.telegram_bot.send_message(
            chat_id=settings.CHAT_ID,
            text=await REGISTER_FORM.render_async(**data),
            reply_markup=verification_keyboard(service_type, user_id)
        )

    async def send_confirmation(self, user_id: int, service_type: ServiceType) -> None:
        if service_type == ServiceType.TELEGRAM:
            await self.telegram_bot.send_message(
                user_id,
                CONFIRM
            )
        else:
            user = await self.discord_bot.fetch_user(user_id)
            embed = discord.Embed(
                title="✌️ Вітаємо! Вас додали у white list серверу. Бажаємо приємної гри!",
                description="IP, модпак та решту ігрової інформації ви зможете знайти на нашому [discord сервері](https://discord.gg/tS6t2wdV). "
            )
            await user.send(embed=embed)
