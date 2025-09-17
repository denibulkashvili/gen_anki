#!/usr/bin/env python3
"""
Anki Model Manager
This module contains all the note models used in the Anki deck generation
"""

from enum import Enum
from typing import List

import genanki


class ModelType(Enum):
    BASIC = "BASIC"


class Model:
    def __init__(self, model_type: ModelType) -> None:
        self.model_type = model_type.value
        self.fields: List = []
        self.model = self.create_model()

    def create_model(self) -> "genanki.Model":
        if self.model_type == ModelType.BASIC.value:
            return self.create_basic_model()
        else:
            raise ValueError(f"Model type {self.model_type} not supported")

    def create_basic_model(self) -> "genanki.Model":
        fields = [{"name": "Question"}, {"name": "Answer"}]
        self.fields = fields

        return genanki.Model(
            1607392398,
            "anki_gen Basic",
            fields=fields,
            templates=[
                {
                    "name": "Basic Card",
                    "qfmt": "{{Question}}",
                    "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}',
                },
            ],
            css="""
            .card {
                font-family: arial;
                font-size: 20px;
                text-align: center;
                color: black;
                background-color: white;
            }
            """,
        )
