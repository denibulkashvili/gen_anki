from enum import Enum
from typing import Any, Dict, List


class DeckCategory(Enum):
    INTERVIEW_UNIVERSITY = "INTERVIEW UNIVERSITY"
    TECH_STACK = "TECH STACK"


class InterviewUniversityDeck(Enum):
    ADVANCED_CONCEPTS = "Advanced Concepts"
    ALGORITHMS = "Algorithms"
    BASIC_CONCEPTS = "Basic Concepts"
    DATA_STRUCTURES = "Data Structures"
    DESIGN_PATTERNS = "Design Patterns"
    INTERVIEW_PROCESS = "Interview Process"
    NETWORKING = "Networking"
    PROGRAMMING_PRINCIPLES = "Programming Principles"
    SYSTEM_DESIGN = "System Design"


class TechStackDeck(Enum):
    CLOUD = "Cloud"
    DATABASES = "Databases"
    JAVASCRIPT = "Javascript"
    MESSAGE_BROKERS = "Message Brokers"


deck_id_map = {
    InterviewUniversityDeck.ADVANCED_CONCEPTS: 1607392319,
    InterviewUniversityDeck.ALGORITHMS: 1607392320,
    InterviewUniversityDeck.BASIC_CONCEPTS: 1607392321,
    InterviewUniversityDeck.DATA_STRUCTURES: 1607392322,
    InterviewUniversityDeck.DESIGN_PATTERNS: 1607392323,
    InterviewUniversityDeck.INTERVIEW_PROCESS: 1607392324,
    InterviewUniversityDeck.NETWORKING: 1607392325,
    InterviewUniversityDeck.PROGRAMMING_PRINCIPLES: 1607392326,
    InterviewUniversityDeck.SYSTEM_DESIGN: 1607392327,
    TechStackDeck.CLOUD: 1607392328,
    TechStackDeck.DATABASES: 1607392329,
    TechStackDeck.JAVASCRIPT: 1607392330,
    TechStackDeck.MESSAGE_BROKERS: 1607392331,
}


class DeckRegistry:
    def __init__(self) -> None:
        self.decks: List[Dict[str, Any]] = []
        self.create_decks()

    def create_decks(self) -> None:
        for interview_deck in InterviewUniversityDeck:
            deck_category = DeckCategory.INTERVIEW_UNIVERSITY.value
            deck_name = interview_deck.value
            name = f"{deck_category}::{deck_name}"
            path = f"{deck_category}/{deck_name}"
            deck_props = {"name": name, "path": path, "id": deck_id_map[interview_deck]}
            self.decks.append(deck_props)

        for tech_stack_deck in TechStackDeck:
            deck_category = DeckCategory.TECH_STACK.value
            deck_name = tech_stack_deck.value
            name = f"{deck_category}::{deck_name}"
            path = f"{deck_category}/{deck_name}"
            deck_props = {
                "name": name,
                "path": path,
                "id": deck_id_map[tech_stack_deck],
            }
            self.decks.append(deck_props)
