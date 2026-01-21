@echo off
REM Run the full pytest test suite for fake-useragent-min
REM Usage: run_tests.bat

echo Running pytest test suite...
echo.

pytest -v

echo.
if %ERRORLEVEL% EQU 0 (
    echo All tests passed!
) else (
    echo Some tests failed. See output above for details.
)

exit /b %ERRORLEVEL%
