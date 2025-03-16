# AIDEV-PascalCase Standards 1.3
**Created: March 15, 2025 3:30 PM**
**Last Modified: March 15, 2025  3:30 PM**

[Context: Development_Standards]
[Pattern_Type: Naming_Convention]
[Implementation_Level: Project_Wide]
[Version: 1.3]

## Change Log from v1.2
- Added clarification on import statement formatting
- Enhanced guidelines for parameters and function arguments
- Added GUI-specific naming conventions
- Expanded docstring formatting requirements
- Included real-world examples from implementations
- Clarified constant naming and usage
- Added module organization guidelines
- Updated timestamp format requirements

## Design Philosophy and Justification

[Context: Standards_Rationale] 
[Priority: Highest]

### Developer Fingerprint

The AIDEV-PascalCase standard serves as a distinct fingerprint of its creator's work—a visual signature that marks code with a sense of craftsmanship and individual style. Just as master typographers and printers developed recognizable styles, this coding standard carries forward that tradition into software development. This fingerprint:

1. **Establishes Provenance**: Makes code immediately recognizable to collaborators
2. **Reflects Craftsmanship**: Demonstrates attention to both function and form
3. **Honors Tradition**: Connects modern software development to traditional design arts
4. **Ensures Consistency**: Creates a unified visual language across projects

### Visual Clarity in Code

The AIDEV-PascalCase standard is founded on principles of typography and visual design. Code is not merely functional—it is a visual medium that developers interact with for extended periods. The choices made in this standard prioritize:

1. **Axis of Symmetry**: Code should exhibit balance and visual harmony, facilitating easier scanning and comprehension
2. **Character Distinction**: Each identifier should be visually distinct without relying on hard-to-discern characters
3. **Readability at Scale**: Standards must remain effective when viewing large codebases or printed materials
4. **Visual Hierarchy**: Different elements (classes, functions, variables) should have visual patterns that aid in rapid identification

### Practical Benefits

This standard offers several tangible benefits over conventional Python style guides:

1. **Rapid Visual Parsing**: PascalCase creates clear word boundaries without sacrificing visual flow, unlike snake_case where underscores can be difficult to see, especially in printed code or certain fonts
2. **Consistency Across Languages**: Maintains visual consistency when working in multi-language environments (JavaScript, C#, Java, etc.)
3. **Reduced Eye Strain**: Eliminates the need to focus on low-visibility characters like underscores
4. **Clear Scope Identification**: Variable scopes and types can be more easily distinguished
5. **Enhanced Refactoring**: Makes variable names more visually distinct during search-and-replace operations

## Core Principles

[Context: Fundamental_Rules]
[Priority: Highest]

### 1. Capitalization Immutability

[Pattern: Name_Preservation]

```python
# Once capitalized, a name's format becomes immutable
ExistingName = "Value"    # Will always remain "ExistingName"
```

### 2. Special Terms Recognition

[Pattern: Reserved_Terms]
[Priority: High]

```
Preserved Terms:
- AI  (Artificial Intelligence)
- DB  (Database)
- GUI (Graphical User Interface)
- API (Application Programming Interface)
- UI  (User Interface)
- UX  (User Experience)
- ID  (Identifier)
- IO  (Input/Output)
- OS  (Operating System)
- IP  (Internet Protocol)
- URL (Uniform Resource Locator)
- HTTP (Hypertext Transfer Protocol)
```

### 3. System Element Preservation

[Pattern: System_Preservation]

```python
# Python keywords and system elements remain lowercase
def FunctionName():    # System-level element
    pass               # Python keyword
```

### 4. Timestamp Documentation

[Pattern: Time_Tracking]

```python
# File: Example.py
# Path: Project/Component/Example.py
# Standard: AIDEV-PascalCase-1.3
# Created: 2025-03-15
# Last Modified: 2025-03-15  11:20AM
# Description: Brief description of the file's purpose
```

Note the two spaces between the date and time in the Last Modified timestamp.

## Character Usage Guidelines

[Context: Visual_Design]
[Priority: High]

### Dash (-) Character Usage

[Pattern: Dash_Constraints]

The dash character impairs visual balance and should be used only in specific circumstances:

1. **Joining Acronyms with Words**:

   ```
   AIDEV-PascalCase    # Correct - connects acronym to words
   Model-Manager       # Incorrect - use ModelManager instead
   ```
2. **Sequential or Enumerated Elements**:

   ```
   Page-2-Section-3    # Correct - represents a sequence
   PG2-SEC3            # Correct - abbreviated sequence
   ```
3. **Standard Date Formats**:

   ```
   2025-03-15          # Correct - standard date format
   ```
4. **Avoid in All Other Cases**:

   ```
   Process-Data        # Incorrect - use ProcessData instead
   User-Input          # Incorrect - use UserInput instead
   ```

### Underscore (_) Character Usage

[Pattern: Underscore_Constraints]

The underscore character has poor visibility and should be limited to:

1. **Constants (ALL_CAPS)**:

   ```python
   MAX_RETRY_COUNT = 5    # Correct - constant with underscore separation
   DEFAULT_TIMEOUT = 30   # Correct - constant with underscore separation
   ```
2. **Pattern Markers in Comments/Documentation**:

   ```python
   # [Pattern: Name_Preservation]  # Correct - used in metadata/documentation
   ```
3. **Global Variable Prefixing (Optional)**:

   ```python
   g_ActiveUsers = []     # Correct - 'g' prefix for global variable
   _GlobalConfig = {}     # Alternative - underscore prefix
   ```
4. **Avoid in All Other Cases**:

   ```python
   process_data()         # Incorrect - use ProcessData() instead
   user_input             # Incorrect - use UserInput instead
   ```

## Implementation Rules

[Context: Practical_Application]

### Module Declaration

[Pattern: Standard_Header]

```python
# File: ModuleName.py
# Path: Project/Component/ModuleName.py
# Standard: AIDEV-PascalCase-1.3
# Created: 2025-03-15
# Last Modified: 2025-03-15  11:20AM
# Description: Brief description of module functionality
```

### Import Statement Formatting

[Pattern: Import_Declaration]

Import statements follow Python conventions but should be organized in a specific order:

```python
# Standard library imports
import os
import sys
from datetime import datetime

# Third-party library imports
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow

# Application-specific imports
from Core.ConfigManager import ConfigManager
from Utils.ValidationUtils import ValidateInput
```

Group imports by type with a single blank line between groups. Within each group, order alphabetically. For multi-line imports, align the imported elements for visual clarity.

### Variable Naming

[Pattern: Variable_Declaration]

All variables, including function parameters, should use PascalCase:

```python
class ExampleClass:
    def ProcessData(self, InputText: str, MaxLength: int = 100) -> None:
        self.CurrentValue = InputText[:MaxLength]
        self.LastModified = self.GetTimestamp()
        
        # Local variables use PascalCase as well
        ResultString = f"Processed: {self.CurrentValue}"
        return ResultString
```

### Function Naming

[Pattern: Function_Declaration]

```python
def ProcessInput(Data: dict, DefaultMode: str = "Standard") -> str:
    """Process the input data and return a formatted string."""
    Result = FormatData(Data, Mode=DefaultMode)
    return Result
```

### Class Naming

[Pattern: Class_Declaration]

```python
class DataProcessor:
    """A class that processes various types of data."""
  
    def __init__(self):
        self.ProcessedItems = 0
```

### Constants

[Pattern: Constant_Declaration]

Constants should be defined using ALL_CAPS with underscore separation:

```python
MAX_ITEMS = 100               # Module-level constant
DEFAULT_TIMEOUT = 30          # Module-level constant
COLOR_DARK_BACKGROUND = QColor(53, 53, 53)  # GUI color constants

class Config:
    API_KEY = "abc123"        # Class-level constant
    DEFAULT_RETRY_COUNT = 3   # Class-level constant
```

### Global Variables

[Pattern: Global_Variable]

```python
g_ActiveSessions = {}   # Global with 'g' prefix
_GlobalRegistry = []    # Alternative style with underscore
```

### GUI-Specific Naming

[Pattern: GUI_Element_Naming]

GUI elements should follow PascalCase with their element type included in the name:

```python
# Widgets
MainWindow = QMainWindow()
SettingsButton = QPushButton("Settings")
UserNameLabel = QLabel("Username:")
PasswordInput = QLineEdit()

# Layouts
MainLayout = QVBoxLayout()
ButtonsLayout = QHBoxLayout()

# Actions and connections
SaveAction = QAction("Save", self)
SaveAction.triggered.connect(self.SaveDocument)

# Colors
BackgroundColor = QColor(240, 240, 240)
HighlightColor = QColor(42, 130, 218)
```

## Docstring Formatting

[Pattern: Documentation_Format]

Docstrings should be comprehensive and follow a consistent format:

### Module Docstrings

```python
"""
Module for handling configuration data.

This module provides functionality to load, save, and validate
configuration settings for the application.
"""
```

### Class Docstrings

```python
class ConfigManager:
    """A class that manages application configuration.
    
    This class provides methods for loading configuration from files,
    saving configuration to files, and validating configuration values.
    
    Attributes:
        DefaultConfig: The default configuration dictionary
        ConfigPath: Path to the configuration file
        IsModified: Flag indicating if config has been modified
    """
```

### Method Docstrings

```python
def ProcessData(self, InputData: dict, ValidateOnly: bool = False) -> bool:
    """Process the input data and update internal state.
    
    Args:
        InputData: Dictionary containing data to process
        ValidateOnly: If True, only validate but don't process
    
    Returns:
        bool: True if processing was successful, False otherwise
    
    Raises:
        ValueError: If InputData is not properly formatted
    """
```

## Module Organization

[Pattern: Code_Organization]

Modules should be organized in a consistent structure:

```python
# File header with timestamp information
# Module docstring

# Imports (organized as described above)

# Constants

# Global variables

# Classes
class MainClass:
    """Class docstring."""
    # Class constants
    
    # Initialization methods
    def __init__(self):
        pass
    
    # Public methods
    
    # Private helper methods

# Functions outside classes

# Main entry point (if applicable)
def main():
    pass

if __name__ == "__main__":
    main()
```

## Special Cases

[Pattern: Edge_Case_Handling]

### 1. Compound Special Terms

```python
AIConfig      # Correct
DbConnection  # Incorrect - should be DBConnection
GuiWindow     # Incorrect - should be GUIWindow
```

### 2. System Integration

```python
__init__.py   # System file - preserved
requirements.txt  # Configuration file - preserved
```

### 3. Multi-Word Variables

```python
UserInputValue  # Correct - each word capitalized
UserinputValue  # Incorrect - inconsistent capitalization
```

### 4. Parameters and Arguments

Function parameters follow the same PascalCase convention as all other variables:

```python
def CalculateTotal(PriceList: list, TaxRate: float = 0.08) -> float:
    """Calculate the total price including tax."""
    Subtotal = sum(PriceList)
    Total = Subtotal * (1 + TaxRate)
    return Total
```

When calling functions, maintain variable naming consistency:

```python
# Variables used as arguments should follow PascalCase
ItemPrices = [10.99, 24.50, 5.75]
LocalTaxRate = 0.095
FinalTotal = CalculateTotal(PriceList=ItemPrices, TaxRate=LocalTaxRate)
```

## Real-World Examples

### 1. Class Implementation Example

This example from a TextFileGenerator application shows proper implementation of AIDEV-PascalCase standards:

```python
class TextFileGenerator(QMainWindow):
    """A GUI application for generating customized text files on the desktop."""
    
    def __init__(self):
        """Initialize the TextFileGenerator application."""
        super().__init__()
        
        # Initialize member variables
        self.CurrentTheme = "Light"
        self.OutputDirectory = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
        self.TemplateOptions = {
            "Blank": "",
            "Lorem Ipsum": self.GetLoremIpsum(),
            "Code Sample": self.GetCodeSample(),
        }
        
        # Setup UI
        self.SetupUI()
        self.ApplyTheme(self.CurrentTheme)
```

### 2. Method Implementation Example

```python
def SaveFile(self):
    """Save the content to a text file on the desktop."""
    try:
        # Generate filename
        Timestamp = ""
        if self.AddTimestampCheckBox.isChecked():
            Timestamp = f"_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
        TemplateName = self.TemplateComboBox.currentText().replace(" ", "")
        Filename = f"{TemplateName}{Timestamp}.txt"
        FilePath = os.path.join(self.OutputDirectory, Filename)
        
        # Write content to file
        with open(FilePath, 'w', encoding='utf-8') as f:
            f.write(self.PreviewTextEdit.toPlainText())
            
        # Show success message
        QMessageBox.information(
            self,
            "Success",
            f"File saved successfully:\n{FilePath}"
        )
        
    except Exception as e:
        QMessageBox.critical(
            self,
            "Error",
            f"Failed to save file: {str(e)}"
        )
```

### 3. GUI Implementation Example

```python
# Template selection section
TemplateGroupBox = QGroupBox("Template Selection")
TemplateLayout = QVBoxLayout()

TemplateLabel = QLabel("Select Template:")
self.TemplateComboBox = QComboBox()
self.TemplateComboBox.addItems(self.TemplateOptions.keys())
self.TemplateComboBox.currentTextChanged.connect(self.UpdatePreview)

TemplateLayout.addWidget(TemplateLabel)
TemplateLayout.addWidget(self.TemplateComboBox)
TemplateGroupBox.setLayout(TemplateLayout)
```

## Validation Rules

[Context: Standards_Enforcement]

### Level 1: Basic Compliance

[Pattern: Minimum_Requirements]

- Standard header present with correct timestamp format
- Special terms correctly capitalized
- System elements preserved
- Variable and function names use PascalCase

### Level 2: Full Compliance

[Pattern: Complete_Implementation]

- All Level 1 requirements
- Proper docstrings with standardized format
- Correct module organization
- Import statements properly organized
- Constants using ALL_CAPS

### Level 3: Strict Compliance

[Pattern: Maximum_Conformance]

- All Level 2 requirements
- Documentation follows all formatting standards
- Test files follow convention
- GUI elements follow naming conventions
- All edge cases handled properly

## Implementation Examples

### 1. Code Module Structure

```python
# File: ConfigManager.py
# Path: OllamaModelEditor/Core/ConfigManager.py
# Standard: AIDEV-PascalCase-1.3
# Created: 2025-03-15
# Last Modified: 2025-03-15  2:45PM
# Description: Manages application configuration settings

"""
Configuration management module for OllamaModelEditor.

This module handles loading, saving, and validating configuration
settings for the application.
"""

# Standard library imports
import os
import json
from datetime import datetime

# Third-party library imports
import jsonschema
from PySide6.QtCore import QStandardPaths

# Application imports
from Core.LoggingUtils import LogError, LogInfo

# Constants
DEFAULT_CONFIG_FILENAME = "config.json"
CONFIG_SCHEMA_VERSION = "1.0"
MAX_RECENT_FILES = 10

# Class implementation
class ConfigManager:
    """Manages application configuration settings.
    
    This class provides functionality to load, save, and validate
    configuration settings for the OllamaModelEditor application.
    """
    
    def __init__(self, ConfigPath: str = None):
        """Initialize the ConfigManager.
        
        Args:
            ConfigPath: Optional path to configuration file
        """
        self.ConfigPath = ConfigPath or self._GetDefaultConfigPath()
        self.CurrentConfig = {}
        self.DefaultConfig = self._GetDefaultConfig()
        self.IsModified = False
        
    def LoadConfig(self) -> bool:
        """Load configuration from file.
        
        Returns:
            bool: True if loading was successful, False otherwise
        """
        try:
            if not os.path.exists(self.ConfigPath):
                LogInfo(f"Config file not found at {self.ConfigPath}. Using defaults.")
                self.CurrentConfig = self.DefaultConfig.copy()
                return True
                
            with open(self.ConfigPath, 'r', encoding='utf-8') as f:
                LoadedConfig = json.load(f)
                
            if self._ValidateConfig(LoadedConfig):
                self.CurrentConfig = LoadedConfig
                LogInfo(f"Configuration loaded from {self.ConfigPath}")
                return True
            else:
                LogError("Invalid configuration format. Using defaults.")
                self.CurrentConfig = self.DefaultConfig.copy()
                return False
                
        except Exception as e:
            LogError(f"Error loading configuration: {str(e)}")
            self.CurrentConfig = self.DefaultConfig.copy()
            return False
            
    def _GetDefaultConfigPath(self) -> str:
        """Get the default path for configuration file.
        
        Returns:
            str: Default configuration file path
        """
        ConfigDir = QStandardPaths.writableLocation(QStandardPaths.AppConfigLocation)
        os.makedirs(ConfigDir, exist_ok=True)
        return os.path.join(ConfigDir, DEFAULT_CONFIG_FILENAME)
        
    def _GetDefaultConfig(self) -> dict:
        """Get the default configuration settings.
        
        Returns:
            dict: Default configuration settings
        """
        return {
            "schemaVersion": CONFIG_SCHEMA_VERSION,
            "theme": "Light",
            "recentFiles": [],
            "modelSettings": {
                "defaultModel": "llama2",
                "parameters": {
                    "temperature": 0.7,
                    "topP": 0.9,
                    "maxTokens": 2048
                }
            }
        }
        
    def _ValidateConfig(self, Config: dict) -> bool:
        """Validate the configuration against the schema.
        
        Args:
            Config: Configuration dictionary to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        # Basic validation for now, could use jsonschema in the future
        RequiredKeys = ["schemaVersion", "theme", "modelSettings"]
        return all(key in Config for key in RequiredKeys)


# Main entry point for testing
def main():
    """Test the ConfigManager functionality."""
    Manager = ConfigManager()
    Success = Manager.LoadConfig()
    print(f"Config loaded: {Success}")
    print(f"Current config: {Manager.CurrentConfig}")


if __name__ == "__main__":
    main()
```

## Final Notes

The AIDEV-PascalCase standard is designed to optimize visual clarity, reduce cognitive load, and create a consistent development experience. While it intentionally deviates from PEP 8, it does so with careful consideration of visual processing optimization, cross-language consistency, and modern development environments.

This standard acknowledges that while it differs from common Python conventions, these differences serve a specific purpose in creating visually distinct, readable, and harmonious code that reflects craftsmanship in software development.

---

Last Updated: 2025-03-15
Status: Active
Version: 1.3
