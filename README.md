# Fake UserAgent (Minimal)

Minimal example package demonstrating a small fake-useragent-style helper plus Ruff-based tooling.

## Requirements
- Python 3.10+
- Optional dev tools: `ruff`, `pytest`, `tomli` (auto-selected for Python <3.11)

## Setup
```bash
pip install -e .[dev]
```

## Running Tests
```bash
pytest
```

## Ruff
Ruff is configured via `pyproject.toml` to handle both linting and formatting across `src/`,
`tests/`, and the project metadata itself.
