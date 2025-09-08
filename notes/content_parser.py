#!/usr/bin/env python3
"""
This module is used to parse the content of a markdown file
and extract the flashcards content
"""

import re
from typing import Any, Dict, List, Optional


class ContentParser:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.flashcards: List[Dict[str, Any]] = []

    def extract_flashcards(self) -> List[Dict[str, Any]]:
        content = self._read_file()
        return self._extract_flashcards_from_content(content)

    def _extract_flashcards_from_content(
        self, content: Optional[str]
    ) -> List[Dict[str, Any]]:
        if not content:
            return self.flashcards

        # Find the single GEN_ANKI marker and parse everything after it
        marker = re.search(r"<!--\s*GEN_ANKI\s*-->", content)
        if not marker:
            return self.flashcards

        section = content[marker.end() :].strip()
        if not section:
            return self.flashcards

        # Split section into individual card blocks by "# ID:" headers
        id_iter = list(
            re.finditer(r"^\s*#\s*ID\s*:\s*(\d+)\s*$", section, re.MULTILINE)
        )
        if not id_iter:
            return self.flashcards

        for i, m in enumerate(id_iter):
            card_start = m.start()
            card_end = id_iter[i + 1].start() if i + 1 < len(id_iter) else len(section)
            card_block = section[card_start:card_end]

            # ID for this card
            card_id = int(m.group(1))

            # Model for this card
            model_match = re.search(
                r"^\s*##\s*Model\s*:\s*([^\n]+)\s*$", card_block, re.MULTILINE
            )
            if not model_match:
                # Skip if no model specified
                continue
            model = model_match.group(1).strip()

            # Fields for this card: ### <FieldName> followed by content
            # until next ### or end of card block
            fields = {}
            field_headers = list(
                re.finditer(r"^\s*###\s*(.+?)\s*$", card_block, re.MULTILINE)
            )
            for f_idx, fh in enumerate(field_headers):
                field_name = fh.group(1).strip()
                f_start = fh.end()
                f_end = (
                    field_headers[f_idx + 1].start()
                    if f_idx + 1 < len(field_headers)
                    else len(card_block)
                )
                field_value = card_block[f_start:f_end].strip()
                fields[field_name] = field_value

            self.flashcards.append({"id": card_id, "model": model, "fields": fields})

        return self.flashcards

    def _read_file(self) -> Optional[str]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                content = file.read()
                return content
        except Exception as e:
            print(f"❌ Error reading {self.file_path}: {e}")
            return None
