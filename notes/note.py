import genanki

from models import Model, ModelType


class Note:
    def __init__(self, note_id: int) -> None:
        self.note_id = note_id

    def create_note(self, model_type: ModelType, parsed_fields: dict) -> genanki.Note:
        if model_type == ModelType.BASIC:
            return self.create_basic_note(parsed_fields)
        else:
            raise ValueError(f"Model type {model_type} not supported")

    def create_basic_note(self, parsed_fields: dict) -> genanki.Note:
        model = Model(ModelType.BASIC)

        question = parsed_fields["Question"]
        answer = parsed_fields["Answer"]

        note = genanki.Note(
            guid=self.note_id, model=model.model, fields=[question, answer]
        )
        return note
