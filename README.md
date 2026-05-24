# Anki Deck Generator

A Python tool that automatically generates Anki flashcard decks from markdown files in your Obsidian vault (or any markdown-based note system). This tool parses specially formatted markdown files and converts them into `.apkg` files that can be directly imported into Anki.

## Features

- 📝 **Markdown-based flashcard creation** - Write flashcards in familiar markdown syntax
- 🎯 **Multiple card models** - Support for different Anki card types
- 🔄 **Batch processing** - Generate multiple decks at once
- 🏗️ **Structured organization** - Hierarchical deck structure with prefixes
- ✅ **Validation** - Built-in validation for duplicate IDs and malformed cards
- 🎨 **Code quality tools** - Pre-configured with black, isort, flake8, and mypy

## Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Setup

1. Clone or download this repository:
```bash
cd /path/to/anki_gen
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv      # create venv once
source venv/bin/activate  # activate it whenever you work
```

3. Install production dependencies:
```bash
make install
```

Or for development (includes linting and formatting tools):
```bash
make install-dev
```

## Configuration

1. Copy the example configuration file:
```bash
cp config/config-example.json config/config.json
```

2. Edit `config/config.json` with your settings:
```json
{
    "settings": {
        "OBSIDIAN_VAULT_PATH": "/path/to/your/vault",
        "GLOBAL_DECK_NAME_PREFIX": "YOUR DECK PREFIX"
    },
    "decks": [
        {
            "name": "DECK NAME",
            "id": 1607392319
        }
    ]
}
```

### Configuration Options

- `OBSIDIAN_VAULT_PATH`: Absolute path to your Obsidian vault (or markdown notes directory)
- `GLOBAL_DECK_NAME_PREFIX`: Prefix for all generated deck names (e.g., "SOFTWARE ENGINEERING")
- `decks`: Array of deck configurations
  - `name`: Name of the deck (should correspond to a folder in your vault under the prefix)
  - `id`: Unique numeric ID for the deck (must be unique across all your Anki decks)

## Usage

### Creating Flashcards

In your markdown files, use the following format to define flashcards:

```markdown
<!-- GEN_ANKI -->

# ID: 1607392319001
## Model: BASIC
### Front
What is Python?

### Back
Python is a high-level, interpreted programming language.

# ID: 1607392319002
## Model: BASIC
### Front
What is Anki?

### Back
Anki is a spaced repetition flashcard program.
```

#### Flashcard Format

- `<!-- GEN_ANKI -->`: Marker indicating the start of flashcard content
- `# ID: <number>`: Unique identifier for each card (must be unique across all your cards)
- `## Model: <MODEL_TYPE>`: The card model/type to use
- `### <Field Name>`: Field names followed by their content

### Generating Decks

Run the main script to generate all configured decks:

```bash
python main.py
```

Or:

```bash
python3 main.py
```

Generated `.apkg` files will be saved in the `generated_decks/` directory.

### Importing into Anki

1. Open Anki
2. Go to File → Import
3. Select the generated `.apkg` file from `generated_decks/`
4. Follow the import wizard

## Project Structure

```
anki_gen/
├── config/              # Configuration files
│   ├── config.json      # Your configuration (not tracked)
│   └── config-example.json
├── decks/               # Deck management
│   ├── deck.py          # Deck class
│   └── registry.py      # Deck registry
├── models/              # Anki card models
│   └── model.py         # Model definitions
├── notes/               # Note processing
│   ├── content_parser.py    # Markdown parser
│   ├── note.py             # Note creation
│   └── notes_finder.py     # File discovery
├── generated_decks/     # Output directory for .apkg files
├── main.py             # Entry point
├── requirements.txt     # Dependencies
├── pyproject.toml      # Tool configurations
└── Makefile            # Development commands
```

## Development

### Available Make Commands

```bash
make install        # Install production dependencies
make install-dev    # Install all dependencies and setup pre-commit
make format         # Format code with black and isort
make lint          # Run flake8 linting
make type-check    # Run mypy type checking
make check         # Run all checks (format, lint, type-check)
make clean         # Remove cache files
make pre-commit-all # Run pre-commit on all files
make help          # Show available commands
```

### Code Quality

This project uses:
- **black**: Code formatting (line length: 88)
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Static type checking
- **pre-commit**: Git hooks for automatic checks

## Dependencies

### Production
- `genanki==0.13.1` - Anki deck generation library
- `PyYAML==6.0.2` - YAML parsing
- `chevron==0.14.0` - Mustache templating
- `frozendict==2.4.6` - Immutable dictionaries
- `cached-property==2.0.1` - Caching utilities

### Development
- `black==23.12.1` - Code formatter
- `flake8==7.0.0` - Linter
- `isort==5.13.2` - Import sorter
- `mypy==1.8.0` - Type checker
- `pre-commit==3.6.0` - Git hooks

## Tips

1. **Unique IDs**: Ensure each flashcard has a unique ID. The script will detect duplicates and report errors.

2. **Deck Organization**: Organize your markdown files in folders that match your deck names in the configuration.

3. **Model Types**: Make sure the model type specified in your flashcards matches the available models in `models/model.py`.

4. **Validation**: The script validates flashcards before generation and will skip decks with invalid cards.

5. **Incremental Updates**: When updating flashcards, keep the same ID to update existing cards in Anki rather than creating duplicates.

## Troubleshooting

### No cards generated
- Check that your markdown files contain the `<!-- GEN_ANKI -->` marker
- Verify that the folder path in your configuration matches your vault structure
- Ensure flashcard IDs are unique

### Import errors in Anki
- Verify that the deck ID in configuration is unique
- Check that all required fields are present for the model type

### Path not found
- Use absolute paths in your configuration
- Verify the folder exists: `<VAULT_PATH>/<PREFIX>/<DECK_NAME>`

## License

This project is provided as-is for personal use.

## Contributing

This is a personal script, but feel free to fork and modify for your own needs!
