@echo off
REM Windows batch script to run the full pytest suite
REM This script runs all tests and displays the results

echo Running pytest test suite...
echo.

pytest -v

echo.
echo Test run complete.
