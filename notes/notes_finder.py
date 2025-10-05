#!/usr/bin/env python3
"""
Simple markdown file reader - Step 1
"""

import glob
import os
from typing import Any, Dict, List

from .content_parser import ContentParser


class DeckNotesFinder:
    def __init__(self, path: str) -> None:
        self.path = path
        self.all_md_files: List[str] = []
        self.flashcards: List[Dict[str, Any]] = []

    def extract_flashcards(self) -> List[Dict[str, Any]]:
        self._find_markdown_files_in_deck()
        for file_path in self.all_md_files:
            flashcards_from_file = ContentParser(file_path).extract_flashcards()
            self.flashcards.extend(flashcards_from_file)

        if not self._are_flashcards_valid():
            return []

        return self.flashcards

    def _find_markdown_files_in_deck(self) -> List[str]:
        if not os.path.exists(self.path):
            print(f"❌ Folder does not exist: {self.path}")
            return self.all_md_files

        pattern = os.path.join(self.path, "**", "*.md")
        md_files = glob.glob(pattern, recursive=True)
        self.all_md_files.extend(md_files)
        return self.all_md_files

    def _are_flashcards_valid(self) -> bool:
        is_valid = True

        if not self.flashcards or len(self.flashcards) == 0:
            return is_valid

        unique_ids = set()

        for flashcard in self.flashcards:
            if not flashcard["id"] or not flashcard["model"] or not flashcard["fields"]:
                print(f"❌ Invalid flashcard properties: {flashcard}")
                is_valid = False

            if flashcard["id"] in unique_ids:
                print(f"❌ Duplicate ID found: {flashcard['id']}")
                is_valid = False

            unique_ids.add(flashcard["id"])

        return is_valid
