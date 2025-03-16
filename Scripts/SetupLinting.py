#!/usr/bin/env python
# File: SetupLinting.py
# Standard: AIDEV-PascalCase-1.2
# Created: 2025-03-15
# Last Modified: 2025-03-15
# Description: Setup script for AIDEV-PascalCase linting in VSCode

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path

def EnsureDirectory(DirectoryPath):
    """Ensure a directory exists, creating it if necessary."""
    Path(DirectoryPath).mkdir(parents=True, exist_ok=True)
    
def WriteTextFile(FilePath, Content):
    """Write content to a text file."""
    with open(FilePath, 'w') as File:
        File.write(Content)
    print(f"Created: {FilePath}")

def RunCommand(Command):
    """Run a shell command and print the output."""
    print(f"Running: {Command}")
    try:
        Result = subprocess.run(Command, shell=True, check=True, 
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             universal_newlines=True)
        print(Result.stdout)
        return True
    except subprocess.CalledProcessError as Error:
        print(f"Error: {Error}")
        print(Error.stderr)
        return False

def SetupVSCodeSettings(ProjectRoot):
    """Set up VSCode settings for the project."""
    VSCodeDir = os.path.join(ProjectRoot, '.vscode')
    EnsureDirectory(VSCodeDir)
    
    # Create settings.json
    SettingsPath = os.path.join(VSCodeDir, 'settings.json')
    SettingsContent = {
        "python.linting.enabled": True,
        "python.linting.pylintEnabled": True,
        "python.linting.pylintArgs": [
            "--rcfile=.pylintrc"
        ],
        "python.linting.flake8Enabled": True,
        "python.linting.flake8Args": [
            "--config=.flake8"
        ],
        "editor.formatOnSave": True,
        "editor.codeActionsOnSave": {
            "source.organizeImports": True
        },
        "python.formatting.provider": "black",
        "python.formatting.blackArgs": [
            "--line-length=100"
        ]
    }
    
    with open(SettingsPath, 'w') as SettingsFile:
        json.dump(SettingsContent, SettingsFile, indent=4)
    
    print(f"Created VSCode settings: {SettingsPath}")

def CreatePylintPlugin(ProjectRoot):
    """Create the Pylint plugin for AIDEV-PascalCase standards."""
    PluginDir = os.path.join(ProjectRoot, 'PylintPlugins')
    EnsureDirectory(PluginDir)
    
    # Create __init__.py
    InitPath = os.path.join(PluginDir, '__init__.py')
    WriteTextFile(InitPath, "")
    
    # Create AIdevChecker.py
    CheckerPath = os.path.join(PluginDir, 'AIdevChecker.py')
    CheckerContent = """
\"\"\"Pylint plugin for AIDEV-PascalCase standards.\"\"\"

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker
from astroid import nodes
import re

class AIDevPascalCaseChecker(BaseChecker):
    \"\"\"Checker enforcing AIDEV-PascalCase naming conventions.\"\"\"
    
    __implements__ = IAstroidChecker
    
    name = 'aidev-pascal-case'
    priority = -1
    msgs = {
        'C9001': (
            'Variable name "%s" should use PascalCase',
            'pascal-case-variable',
            'Variables should use PascalCase according to AIDEV standard'
        ),
        'C9002': (
            'Function name "%s" should use PascalCase',
            'pascal-case-function',
            'Functions should use PascalCase according to AIDEV standard'
        ),
        'C9003': (
            'Method name "%s" should use PascalCase (except special methods)',
            'pascal-case-method',
            'Methods should use PascalCase according to AIDEV standard'
        ),
        'C9004': (
            'Special term "%s" is not capitalized correctly',
            'special-term-capitalization',
            'Special terms like API, DB, GUI should be capitalized correctly'
        )
    }
    options = ()
    
    def __init__(self, linter=None):
        super().__init__(linter)
        self.special_terms = {
            'api': 'API',
            'db': 'DB',
            'gui': 'GUI',
            'url': 'URL',
            'html': 'HTML',
            'json': 'JSON',
            'xml': 'XML',
            'css': 'CSS',
            'sql': 'SQL',
            'ui': 'UI'
        }
    
    def is_pascal_case(self, name):
        \"\"\"Check if a name follows PascalCase convention.\"\"\"
        # Skip special cases like __init__
        if name.startswith('__') and name.endswith('__'):
            return True
            
        # Allow single underscores for private attributes
        if name.startswith('_') and not name.startswith('__'):
            name = name[1:]
            
        # Skip if all uppercase (constants)
        if name.isupper() and '_' in name:
            return True
            
        # Check for appropriate capitalization
        parts = name.split('_')
        return all(part and part[0].isupper() for part in parts)
        
    def check_special_terms(self, name):
        \"\"\"Check if special terms are capitalized correctly.\"\"\"
        for term, correct in self.special_terms.items():
            pattern = re.compile(r'\\b' + term + r'\\b', re.IGNORECASE)
            if pattern.search(name) and correct not in name:
                return False
        return True
    
    def visit_assignname(self, node):
        \"\"\"Check variable names.\"\"\"
        # Skip if part of a function parameter or inside comprehension
        if isinstance(node.parent, (nodes.Arguments, nodes.Comprehension)):
            return
            
        # Skip constants (all uppercase)
        if node.name.isupper() and '_' in node.name:
            return
            
        if not self.is_pascal_case(node.name):
            self.add_message('pascal-case-variable', node=node, args=(node.name,))
        
        if not self.check_special_terms(node.name):
            self.add_message('special-term-capitalization', node=node, args=(node.name,))
    
    def visit_functiondef(self, node):
        \"\"\"Check function and method names.\"\"\"
        # Skip if this is a special method
        if node.name.startswith('__') and node.name.endswith('__'):
            return
            
        # Check if it's a method or a function
        if isinstance(node.parent, nodes.ClassDef):
            if not self.is_pascal_case(node.name):
                self.add_message('pascal-case-method', node=node, args=(node.name,))
        else:
            if not self.is_pascal_case(node.name):
                self.add_message('pascal-case-function', node=node, args=(node.name,))
        
        if not self.check_special_terms(node.name):
            self.add_message('special-term-capitalization', node=node, args=(node.name,))

def register(linter):
    \"\"\"Register the checker.\"\"\"
    linter.register_checker(AIDevPascalCaseChecker(linter))
"""
    WriteTextFile(CheckerPath, CheckerContent)
    
    # Create a README for the plugin
    ReadmePath = os.path.join(PluginDir, 'README.md')
    ReadmeContent = """# AIDEV-PascalCase Pylint Plugin

This plugin enforces the AIDEV-PascalCase naming conventions in Python code:

1. Variable names should use PascalCase
2. Function names should use PascalCase
3. Method names should use PascalCase (except special methods like __init__)
4. Special terms like API, DB, GUI should be capitalized correctly
"""
    WriteTextFile(ReadmePath, ReadmeContent)
    
    print(f"Created Pylint plugin in: {PluginDir}")
    
    return PluginDir

def CreatePylintConfig(ProjectRoot, PluginPath):
    """Create Pylint configuration file."""
    PylintrcPath = os.path.join(ProjectRoot, '.pylintrc')
    
    # Get the relative path to the plugin directory
    RelativePath = os.path.relpath(PluginPath, ProjectRoot)
    
    PylintContent = f"""[MASTER]
# Path to the custom plugin
init-hook='import sys; sys.path.append("{RelativePath}")'
load-plugins=PylintPlugins.AIdevChecker

[MESSAGES CONTROL]
# Enable the custom checks
enable=pascal-case-variable,pascal-case-function,pascal-case-method,special-term-capitalization

# Disable some default checks that conflict with our standards
disable=invalid-name,C0103

[FORMAT]
# Maximum line length
max-line-length=100

[REPORTS]
# Set the output format
output-format=colorized

# Activate the evaluation score
evaluation=10.0 - ((float(5 * error + warning + refactor + convention) / statement) * 10)

# Set the output to show column numbers
msg-template={{path}}:{{line}}:{{column}}: {{msg_id}}: {{msg}} ({{symbol}})
"""
    WriteTextFile(PylintrcPath, PylintContent)

def CreateFlake8Config(ProjectRoot):
    """Create Flake8 configuration file."""
    Flake8Path = os.path.join(ProjectRoot, '.flake8')
    Flake8Content = """[flake8]
max-line-length = 100
exclude = .git,__pycache__,build,dist,venv
# We're using our custom naming convention, so ignore name-related errors
ignore = E501, W503, N802, N803, N806
"""
    WriteTextFile(Flake8Path, Flake8Content)

def CreatePreCommitConfig(ProjectRoot, PluginPath):
    """Create pre-commit configuration file."""
    PreCommitPath = os.path.join(ProjectRoot, '.pre-commit-config.yaml')
    
    PreCommitContent = """repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files

-   repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
    -   id: flake8
        additional_dependencies: [flake8-docstrings]

-   repo: local
    hooks:
    -   id: pylint
        name: pylint
        entry: pylint
        language: system
        types: [python]
        args: [
            "--rcfile=.pylintrc",  # use the project's pylintrc
        ]
"""
    WriteTextFile(PreCommitPath, PreCommitContent)

def CreateSampleCode(ProjectRoot):
    """Create sample Python files to test the linting rules."""
    SamplesDir = os.path.join(ProjectRoot, 'Samples')
    EnsureDirectory(SamplesDir)
    
    # Sample with violations
    BadSamplePath = os.path.join(SamplesDir, 'BadSample.py')
    BadSampleContent = """# File: BadSample.py
# Standard: AIDEV-PascalCase-1.2 (intentionally violating for testing)
# Created: 2025-03-15
# Last Modified: 2025-03-15
# Description: Sample with PascalCase violations for testing linting

def process_data(input_data):
    # Process the input data and return results.
    result = []
    for item in input_data:
        processed_item = item * 2
        result.append(processed_item)
    return result

class DataProcessor:
    # Class for processing data.
    
    def __init__(self):
        self.data = []
        self.api_endpoint = "https://example.com/api"  # Special term violation
        
    def add_item(self, item):
        # Add an item to the data list.
        self.data.append(item)
        
    def get_results(self):
        # Get the processed results.
        return process_data(self.data)

# Variable name violations
user_input = [1, 2, 3, 4, 5]
processed_results = process_data(user_input)
print(f"Results: {processed_results}")
"""
    WriteTextFile(BadSamplePath, BadSampleContent)
    
    # Sample with correct styling
    GoodSamplePath = os.path.join(SamplesDir, 'GoodSample.py')
    GoodSampleContent = """# File: GoodSample.py
# Standard: AIDEV-PascalCase-1.2
# Created: 2025-03-15
# Last Modified: 2025-03-15
# Description: Sample with correct PascalCase for testing linting

def ProcessData(InputData):
    # Process the input data and return results.
    Result = []
    for Item in InputData:
        ProcessedItem = Item * 2
        Result.append(ProcessedItem)
    return Result

class DataProcessor:
    # Class for processing data.
    
    def __init__(self):
        self.Data = []
        self.APIEndpoint = "https://example.com/api"  # Correct special term
        
    def AddItem(self, Item):
        # Add an item to the data list.
        self.Data.append(Item)
        
    def GetResults(self):
        # Get the processed results.
        return ProcessData(self.Data)

# Correctly named variables
UserInput = [1, 2, 3, 4, 5]
ProcessedResults = ProcessData(UserInput)
print(f"Results: {ProcessedResults}")
"""
    WriteTextFile(GoodSamplePath, GoodSampleContent)
    
    print(f"Created sample files in: {SamplesDir}")

def CreateInstallScript(ProjectRoot):
    """Create installation script for the linting setup."""
    InstallScriptPath = os.path.join(ProjectRoot, 'InstallLinting.sh')
    InstallScriptContent = """#!/bin/bash
# File: InstallLinting.sh
# Standard: AIDEV-PascalCase-1.2
# Created: 2025-03-15
# Last Modified: 2025-03-15
# Description: Script to install AIDEV-PascalCase linting in any project

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${1:-$(pwd)}"

echo "Installing AIDEV-PascalCase linting to: $TARGET_DIR"

# Create .vscode directory if it doesn't exist
mkdir -p "$TARGET_DIR/.vscode"

# Copy plugin directory
echo "Copying Pylint plugin..."
cp -r "$SCRIPT_DIR/PylintPlugins" "$TARGET_DIR/"

# Copy configuration files
echo "Copying configuration files..."
cp "$SCRIPT_DIR/.pylintrc" "$TARGET_DIR/"
cp "$SCRIPT_DIR/.flake8" "$TARGET_DIR/"
cp "$SCRIPT_DIR/.pre-commit-config.yaml" "$TARGET_DIR/"

# Copy VSCode settings
echo "Setting up VSCode configuration..."
cp "$SCRIPT_DIR/.vscode/settings.json" "$TARGET_DIR/.vscode/"

echo "Installation complete!"
echo "Make sure to install required packages:"
echo "pip install pylint flake8 pre-commit"
echo ""
echo "Then initialize pre-commit:"
echo "cd $TARGET_DIR && pre-commit install"
"""
    WriteTextFile(InstallScriptPath, InstallScriptContent)
    os.chmod(InstallScriptPath, 0o755)  # Make executable
    
    # Windows version - using raw string to avoid escape sequence warnings
    InstallBatPath = os.path.join(ProjectRoot, 'InstallLinting.bat')
    InstallBatContent = r"""@echo off
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
"""
    WriteTextFile(InstallBatPath, InstallBatContent)

def CreateReadme(ProjectRoot):
    """Create README file for the project."""
    ReadmePath = os.path.join(ProjectRoot, 'README.md')
    ReadmeContent = """# AIDEV-PascalCase Linting Setup

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
   InstallLinting.bat C:\\path\\to\\your\\project
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
"""
    WriteTextFile(ReadmePath, ReadmeContent)

def SetupGitRepo(ProjectRoot):
    """Initialize a git repository if it doesn't exist."""
    GitDir = os.path.join(ProjectRoot, '.git')
    if not os.path.exists(GitDir):
        print("Initializing git repository...")
        try:
            subprocess.run(['git', 'init'], cwd=ProjectRoot, check=True, 
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # Create a .gitignore file
            GitignorePath = os.path.join(ProjectRoot, '.gitignore')
            GitignoreContent = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Virtual environment
venv/
ENV/
.env/

# VS Code
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
"""
            WriteTextFile(GitignorePath, GitignoreContent)
            print("Git repository initialized")
            return True
        except subprocess.SubprocessError as Error:
            print(f"Error initializing git repository: {Error}")
            return False
    else:
        print("Git repository already exists")
        return True
    
def main():
    """Main function to set up AIDEV-PascalCase linting."""
    print("Setting up AIDEV-PascalCase linting...")
    
    # Get the current directory
    ProjectRoot = os.getcwd()
    print(f"Project root: {ProjectRoot}")
    
    # Create Pylint plugin
    PluginDir = CreatePylintPlugin(ProjectRoot)
    
    # Create configuration files
    CreatePylintConfig(ProjectRoot, PluginDir)
    CreateFlake8Config(ProjectRoot)
    CreatePreCommitConfig(ProjectRoot, PluginDir)
    
    # Set up VSCode settings
    SetupVSCodeSettings(ProjectRoot)
    
    # Create sample code
    CreateSampleCode(ProjectRoot)
    
    # Create installation scripts
    CreateInstallScript(ProjectRoot)
    
    # Create README
    CreateReadme(ProjectRoot)
    
    # Initialize git repository (required for pre-commit)
    GitInitialized = SetupGitRepo(ProjectRoot)
    
    # Initialize pre-commit if git was initialized
    if GitInitialized:
        RunCommand("pre-commit install")
    
    print("\nSetup complete!")
    print("To test the linting, open the Samples directory in VSCode.")
    print("The BadSample.py file should show linting errors for naming convention violations.")
    print("\nTo install this configuration in another project:")
    print("  ./InstallLinting.sh /path/to/your/project")
    print("or on Windows:")
    print("  InstallLinting.bat C:\\path\\to\\your\\project")

if __name__ == "__main__":
    main()
