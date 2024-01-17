import discord.ui

from app.discord.modals.form import Form


class RegisterView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Зареєструватись")
    async def register(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(Form())
