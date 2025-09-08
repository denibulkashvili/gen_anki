.PHONY: install format lint type-check test clean all

# Install dependencies
install:
	pip install -r requirements.txt

# Install development dependencies
install-dev:
	pip install -r requirements.txt
	pre-commit install

# Format code with black and isort
format:
	black .
	isort .

# Run linting
lint:
	flake8 .

# Run type checking
type-check:
	mypy .

# Run all checks
check: format lint type-check

# Clean cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

# Run pre-commit on all files
pre-commit-all:
	pre-commit run --all-files

# Help
help:
	@echo "Available commands:"
	@echo "  install        - Install production dependencies"
	@echo "  install-dev    - Install all dependencies and setup pre-commit"
	@echo "  format         - Format code with black and isort"
	@echo "  lint          - Run flake8 linting"
	@echo "  type-check    - Run mypy type checking"
	@echo "  check         - Run all checks (format, lint, type-check)"
	@echo "  clean         - Remove cache files"
	@echo "  pre-commit-all - Run pre-commit on all files"
