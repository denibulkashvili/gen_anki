import genanki


class Deck:
    def __init__(self, deck_id: int, deck_name: str) -> None:
        self.deck_id = deck_id
        self.deck_name = deck_name
        self.deck = genanki.Deck(deck_id, deck_name)

    def add_notes(self, notes: list) -> "Deck":
        for note in notes:
            self.deck.add_note(note)
        return self

    def write_to_file(self, file_name: str) -> "Deck":
        genanki.Package(self.deck).write_to_file(file_name)
        return self
