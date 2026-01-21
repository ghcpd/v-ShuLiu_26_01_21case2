# fake-useragent-min

A minimal Python project demonstrating user-agent utilities and ruff-based tooling.

## Requirements

- **Python 3.10+** (the project targets Python 3.10 and later)
- **pip** (for installing dependencies)

## Installation

1. Clone or download this repository.

2. (Recommended) Create and activate a virtual environment:

   ```bash
   # On Windows
   python -m venv .venv
   .venv\Scripts\activate

   # On Unix/macOS
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install the package in editable mode with development dependencies:

   ```bash
   pip install -e ".[dev]"
   ```

   This installs:
   - The `fake_useragent_min` package
   - `pytest` for running tests
   - `ruff` for linting and formatting

## Running Tests

Run the full test suite using pytest:

```bash
pytest
```

Or with verbose output:

```bash
pytest -v
```

On Windows, you can also use the provided batch script:

```bash
run_tests.bat
```

## Linting and Formatting

This project uses **Ruff** as the primary tool for both linting and formatting.

### Check for linting issues

```bash
ruff check .
```

### Auto-fix linting issues

```bash
ruff check --fix .
```

### Check formatting

```bash
ruff format --check .
```

### Apply formatting

```bash
ruff format .
```

## Project Structure

```
.
├── pyproject.toml              # Project metadata and Ruff configuration
├── README.md                   # This file
├── run_tests.bat               # Windows batch script to run tests
├── src/
│   └── fake_useragent_min/
│       ├── __init__.py         # Package exports
│       └── fake.py             # Core implementation
└── tests/
    ├── test_fake_min.py        # Tests for the user-agent functionality
    └── test_ruff_config.py     # Tests validating Ruff configuration
```

## Usage

```python
from fake_useragent_min import get_random_user_agent

# Get a random User-Agent string
ua = get_random_user_agent()
print(ua)  # e.g., "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
```

## Configuration

The Ruff configuration in `pyproject.toml` includes:

- **target-version**: Python 3.10+
- **line-length**: 88 characters (consistent with Black)
- **indent-width**: 4 spaces
- **Selected rules**: pycodestyle, Pyflakes, isort, pep8-naming, pydocstyle, pyupgrade, flake8-bugbear, flake8-comprehensions, flake8-simplify, and Ruff-specific rules
- **Docstring convention**: Google style

See `pyproject.toml` for the complete configuration.
