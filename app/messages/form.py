from app.messages.environment import environment

REGISTER_FORM = environment.from_string("""
🟥 Нова реєстрація

ПІБ: <code>{{ full_name }}</code>
Місце навчання: <code>{{ place_of_study }}</code>
Нікнейм: <code>{{ nickname }}</code>
""")
