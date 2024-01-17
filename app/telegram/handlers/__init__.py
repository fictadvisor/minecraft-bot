from aiogram import Router, F
from aiogram.filters import CommandStart

from app.telegram.handlers.form import form
from app.telegram.handlers.start import start, register

router = Router(name=__name__)

router.message.register(start, CommandStart())
router.callback_query.register(register, F.data == "register")
router.include_router(form)
