from sqlalchemy.orm import Mapped

from app.models import Base


class Registration(Base):
    __tablename__ = "registrations"

    name: Mapped[str]
    discord_nickname: Mapped[str]
    minecraft_nickname: Mapped[str]
