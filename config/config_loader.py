import json
import os
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Config:
    vault_path: str
    global_deck_name_prefix: str
    decks: List


class ConfigLoader:
    def __init__(self, config_path: str = "config/config.json") -> None:
        self.config_path = config_path
        self.config: Optional[Config] = None

    def load_config(self) -> Config:
        if self.config:
            return self.config

        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")

        try:
            with open(self.config_path, "r") as f:
                config_data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in config file: {e}")

        self.config = self._parse_config(config_data)
        return self.config

    def _parse_config(self, config_data: dict) -> Config:
        try:
            return Config(
                vault_path=config_data["settings"]["vault_path"],
                global_deck_name_prefix=config_data["settings"][
                    "global_deck_name_prefix"
                ],
                decks=config_data["decks"],
            )
        except KeyError as e:
            raise ValueError(f"Missing required key in config: {e}")


config_loader = ConfigLoader()
