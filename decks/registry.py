from typing import Any, Dict, List

from config import config_loader


class DeckRegistry:
    def __init__(self) -> None:
        self.decks: List[Dict[str, Any]] = []
        self.create_decks()

    def create_decks(self) -> None:
        config = config_loader.load_config()
        for deck_props in config.decks:
            self.decks.append(deck_props)
