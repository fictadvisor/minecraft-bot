from app.messages.environment import environment

REGISTER_FORM = environment.from_string("""
🟥 Нова реєстрація

ПІБ: <code>{{ name }}</code>
Нікнейм у Minecraft: <code>{{ nickname }}</code>
Нікнейм у Discord: <code>{{ discord_nickname }}</code>
""")
