from enum import Enum


class ServiceType(str, Enum):
    TELEGRAM = "telegram"
    DISCORD = "discord"
