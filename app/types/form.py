from typing import TypedDict, Optional


class Form(TypedDict):
    full_name: str
    place_of_study: Optional[str]
    nickname: str
