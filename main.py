#!/usr/bin/env python3
"""
Anki Deck Generator using genanki
This script creates a deck with different types of cards
"""
import os

from config import config_loader
from decks import Deck, DeckRegistry
from models import ModelType
from notes import DeckNotesFinder, Note

PACKAGES_DIR = "./generated_decks"


def build_decks() -> None:
    config = config_loader.load_config()
    deck_registry = DeckRegistry()

    for deck in deck_registry.decks:
        deck_name = f"{config.global_deck_name_prefix}::{deck['name']}"
        deck_path = deck["name"]
        deck_id = deck["id"]

        absolute_deck_path = os.path.join(
            config.vault_path, config.global_deck_name_prefix, deck_path
        )

        flashcards = DeckNotesFinder(absolute_deck_path).extract_flashcards()
        notes = []
        for flashcard in flashcards:
            # Convert parsed model string to ModelType enum
            model_enum = ModelType[flashcard["model"]]
            note = Note(flashcard["id"]).create_note(model_enum, flashcard["fields"])
            notes.append(note)

        notes_len = len(notes)
        if notes_len == 0:
            continue

        package_path = os.path.join(PACKAGES_DIR, f"{deck_path}.apkg")
        os.makedirs(os.path.dirname(package_path), exist_ok=True)
        anki_deck = Deck(deck_id, deck_name).add_notes(notes)
        anki_deck.write_to_file(package_path)

        print(f"🎯Generated {notes_len} notes for {deck_name}")


def main() -> None:
    print("Generating Decks...")

    build_decks()

    print("Done")


if __name__ == "__main__":
    main()
