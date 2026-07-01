@echo off

isort src tests
if errorlevel 1 exit /b %errorlevel%

echo.
echo isort checks passed

black src tests
if errorlevel 1 exit /b %errorlevel%

echo.
echo black checks passed

flake8 src tests
if errorlevel 1 exit /b %errorlevel%

echo.
echo flake8 checks passed

mypy src tests
if errorlevel 1 exit /b %errorlevel%

echo.
echo mypy checks passed

echo.
echo ============ QUICK CHECKS PASSED ============
