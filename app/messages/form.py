from app.messages.environment import environment

REGISTER_FORM = environment.from_string("""
🟥 Нова реєстрація

ПІБ: <code>{{ name }}</code>
Нікнейм у Minecraft: <code>{{ nickname }}</code>
Нікнейм у Discord: <code>{{ discord_nickname }}</code>
""")

REGISTRATION = """
Дякуємо, ваша заявка відправлена. 
⏰ Очікуйте на підтвердження.

Детальніше ознайомтесь на сервері: https://discord.gg/tS6t2wdV
"""

CONFIRM = """
✌️ Вітаємо! Вас додали у white list серверу. Бажаємо приємної гри! 

IP, модпак та решту ігрової інформації ви зможете знайти на нашому <a href="https://discord.gg/tS6t2wdV">discord сервері</a>. 
"""

