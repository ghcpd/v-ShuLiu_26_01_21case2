# fake-useragent-min

A minimal project demonstrating user-agent utilities and Ruff-based tooling.

## Requirements

- Python 3.10 or higher

## Installation

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

2. Install development dependencies:

   ```powershell
   pip install -e ".[dev]"
   ```

## Running Tests

Run the full test suite with pytest:

```powershell
pytest
```

Or with verbose output:

```powershell
pytest -v
```

## Linting and Formatting

This project uses [Ruff](https://github.com/astral-sh/ruff) for linting and formatting.

### Check for linting issues:

```powershell
ruff check src tests
```

### Auto-fix linting issues:

```powershell
ruff check src tests --fix
```

### Check formatting:

```powershell
ruff format src tests --check
```

### Apply formatting:

```powershell
ruff format src tests
```

## Project Structure

```
├── pyproject.toml              # Project metadata and Ruff configuration
├── src/
│   └── fake_useragent_min/
│       ├── __init__.py         # Package exports
│       └── fake.py             # User-agent utilities
└── tests/
    ├── test_fake_min.py        # Original behavior tests
    └── test_config_requirements.py  # Configuration validation tests
```

## Usage

```python
from fake_useragent_min import get_random_user_agent

ua = get_random_user_agent()
print(ua)  # e.g., "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
```
