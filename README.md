# AIDEV-PascalCase Linting Setup

This project provides tools to set up automated linting for AIDEV-PascalCase standards in Python projects.

## Quick Start

1. Clone this repository
2. Run the setup script:
   ```bash
   python SetupLinting.py
   ```
3. Install the required packages:
   ```bash
   pip install pylint flake8 pre-commit
   ```
4. Initialize git repository (required for pre-commit):
   ```bash
   git init
   pre-commit install
   ```
5. Open the `Samples` directory to see examples

## Installing in Other Projects

To install this linting configuration in another project:

1. Use the install script:
   ```bash
   ./InstallLinting.sh /path/to/your/project
   ```
   Or on Windows:
   ```
   InstallLinting.bat C:\path\to\your\project
   ```

2. Install the required packages in that project:
   ```bash
   pip install pylint flake8 pre-commit
   ```

3. Initialize git and pre-commit in that project:
   ```bash
   cd /path/to/your/project
   git init
   pre-commit install
   ```

## Testing the Configuration

1. Open the `Samples/BadSample.py` file in VSCode
2. You should see linting errors highlighting the naming convention violations
3. Compare with `Samples/GoodSample.py` which follows the conventions

## Configuration Files

- `.pylintrc`: Pylint configuration with AIDEV-PascalCase rules
- `.flake8`: Flake8 configuration
- `.pre-commit-config.yaml`: Pre-commit hooks configuration
- `.vscode/settings.json`: VSCode settings for linting

## Custom Pylint Plugin

The custom plugin is in the `PylintPlugins` directory:

- `AIdevChecker.py`: Contains the rules for AIDEV-PascalCase checking
