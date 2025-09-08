#!/usr/bin/env python3
"""
Anki Deck Generator using genanki
This script creates a deck with different types of cards
"""
import os

from decks import Deck, DeckRegistry
from models import ModelType
from notes import DeckNotesFinder, Note

PACKAGES_DIR = "./generated_decks"
OBSIDIAN_VAULT_PATH = "/mnt/c/Users/legion/Documents/Obsidian Vaults/programming"
GLOBAL_DECK_NAME_PREFIX = "SOFTWARE ENGINEERING"


def build_decks() -> None:
    deck_registry = DeckRegistry()

    for deck in deck_registry.decks:
        deck_name = f"{GLOBAL_DECK_NAME_PREFIX}::{deck['name']}"
        deck_path = deck["path"]
        deck_id = deck["id"]

        absolute_deck_path = os.path.join(
            OBSIDIAN_VAULT_PATH, GLOBAL_DECK_NAME_PREFIX, deck_path
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
