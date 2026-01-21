# fake-useragent-min

A minimal Python project demonstrating user-agent utilities with ruff-based tooling.

## Requirements

- Python 3.10 or later
- Windows 10 or later (also compatible with other platforms)

## Installation

1. Clone or navigate to the project directory:
   ```powershell
   cd c:\Users\v-shuliu1\test\0121-2\Claude-sonnet-4.5
   ```

2. Install the package with development dependencies:
   ```powershell
   pip install -e ".[dev]"
   ```

   This will install:
   - The `fake-useragent-min` package
   - `pytest` for running tests
   - `ruff` for linting and formatting

## Usage

```python
from fake_useragent_min import get_random_user_agent

# Get a random user-agent string
user_agent = get_random_user_agent()
print(user_agent)
```

## Running Tests

Run the full test suite using pytest:

```powershell
pytest
```

Or use the provided Windows batch script:

```powershell
.\run_tests.bat
```

For verbose output:

```powershell
pytest -v
```

## Code Quality Tools

This project uses `ruff` for both linting and formatting.

### Linting

Check for linting issues:

```powershell
ruff check .
```

Automatically fix issues where possible:

```powershell
ruff check --fix .
```

### Formatting

Check formatting:

```powershell
ruff format --check .
```

Apply formatting:

```powershell
ruff format .
```

## Project Structure

```
.
├── pyproject.toml              # Project metadata and ruff configuration
├── README.md                   # This file
├── run_tests.bat              # Windows test runner script
├── src/
│   └── fake_useragent_min/
│       ├── __init__.py        # Package initialization
│       └── fake.py            # Core functionality
└── tests/
    ├── test_fake_min.py       # Basic functionality tests
    └── test_config_validation.py  # Configuration validation tests
```

## Configuration

The project uses a comprehensive ruff configuration in `pyproject.toml`:

- **Target version**: Python 3.10+
- **Line length**: 100 characters
- **Enabled rule sets**: pycodestyle, pyflakes, isort, pep8-naming, pyupgrade, flake8-bugbear, flake8-comprehensions, flake8-simplify, and ruff-specific rules
- **Formatting**: Double quotes, 4-space indentation, automatic line ending detection

## Development

When contributing to this project:

1. Ensure all tests pass: `pytest`
2. Verify code quality: `ruff check .`
3. Format code: `ruff format .`
4. Add tests for new functionality

## License

This is a demonstration project for tooling configuration.
