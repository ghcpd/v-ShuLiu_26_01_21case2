@echo off
REM Run the full pytest test suite for fake-useragent-min
REM Requires the virtual environment to be set up with dev dependencies installed

echo Running pytest test suite...
echo.

if exist ".venv\Scripts\python.exe" (
    .venv\Scripts\python.exe -m pytest tests -v
) else (
    echo Error: Virtual environment not found at .venv
    echo Please create it first with: python -m venv .venv
    echo Then install dependencies with: .venv\Scripts\pip.exe install -e ".[dev]"
    exit /b 1
)
