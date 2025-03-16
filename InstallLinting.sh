#!/bin/bash
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
