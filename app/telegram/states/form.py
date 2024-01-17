from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    full_name = State()
    place_of_study = State()
    nickname = State()
