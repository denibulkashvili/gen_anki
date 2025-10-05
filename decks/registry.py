from enum import Enum
from typing import Any, Dict, List


class DeckNameEnum(Enum):
    INTERVIEW_UNIVERSITY = "INTERVIEW UNIVERSITY"
    TECH_STACK = "TECH STACK"


deck_id_map = {
    DeckNameEnum.INTERVIEW_UNIVERSITY: 1607392319,
    DeckNameEnum.TECH_STACK: 1607392320,
}


class DeckRegistry:
    def __init__(self) -> None:
        self.decks: List[Dict[str, Any]] = []
        self.create_decks()

    def create_decks(self) -> None:
        for deck_name_enum in DeckNameEnum:
            deck_name = deck_name_enum.value
            deck_props = {"name": deck_name, "id": deck_id_map[deck_name_enum]}
            self.decks.append(deck_props)
