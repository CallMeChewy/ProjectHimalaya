@echo off
REM File: InstallLinting.bat
REM Standard: AIDEV-PascalCase-1.2
REM Created: 2025-03-15
REM Last Modified: 2025-03-15
REM Description: Script to install AIDEV-PascalCase linting in any project

setlocal

set SCRIPT_DIR=%~dp0
set TARGET_DIR=%1

if "%TARGET_DIR%"=="" set TARGET_DIR=%CD%

echo Installing AIDEV-PascalCase linting to: %TARGET_DIR%

REM Create .vscode directory if it doesn't exist
if not exist "%TARGET_DIR%\.vscode" mkdir "%TARGET_DIR%\.vscode"

REM Copy plugin directory
echo Copying Pylint plugin...
xcopy /E /I /Y "%SCRIPT_DIR%\PylintPlugins" "%TARGET_DIR%\PylintPlugins"

REM Copy configuration files
echo Copying configuration files...
copy /Y "%SCRIPT_DIR%\.pylintrc" "%TARGET_DIR%\"
copy /Y "%SCRIPT_DIR%\.flake8" "%TARGET_DIR%\"
copy /Y "%SCRIPT_DIR%\.pre-commit-config.yaml" "%TARGET_DIR%\"

REM Copy VSCode settings
echo Setting up VSCode configuration...
copy /Y "%SCRIPT_DIR%\.vscode\settings.json" "%TARGET_DIR%\.vscode\"

echo Installation complete!
echo Make sure to install required packages:
echo pip install pylint flake8 pre-commit
echo.
echo Then initialize pre-commit:
echo cd %TARGET_DIR% ^&^& pre-commit install

endlocal
