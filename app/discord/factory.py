import discord
from aiogram import Bot
from discord.ext import commands

from app.discord.views.register import RegisterView


def create_discord_bot() -> commands.Bot:
    intents = discord.Intents.default()
    intents.message_content = True

    client = commands.Bot(command_prefix="/", intents=intents)

    @client.tree.command(name="register", description="Реєстрація на сервері")
    async def register(interaction: discord.Interaction):
        await interaction.response.send_message("Для реєстрації потрібно заповнити форму", view=RegisterView(), ephemeral=True)

    @client.event
    async def on_ready():
        await client.tree.sync()

    return client
