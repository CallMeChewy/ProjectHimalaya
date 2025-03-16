#!/bin/bash
# File: GitHubSetup.sh
# Standard: AIDEV-PascalCase-1.3
# Created: 2025-03-15
# Last Modified: 2025-03-15
# Description: Script to create and update GitHub repository for ProjectHimalaya

# Configuration - Edit these variables
GITHUB_USERNAME="CallMeChewy"
REPO_NAME="ProjectHimalaya"
PROJECT_DIR="$HOME/Desktop/ProjectHimalaya"  # Path to your project directory

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to display usage information
ShowUsage() {
    echo -e "${YELLOW}Usage:${NC}"
    echo -e "  $0 [command]"
    echo
    echo -e "${YELLOW}Commands:${NC}"
    echo -e "  init      Initialize the repository and make first commit"
    echo -e "  update    Update the repository with latest changes"
    echo -e "  status    Check repository status"
    echo -e "  help      Show this help message"
    echo
    echo -e "${YELLOW}Examples:${NC}"
    echo -e "  $0 init"
    echo -e "  $0 update \"Added new framework components\""
}

# Function to check if Git is installed
CheckGitInstalled() {
    if ! command -v git &> /dev/null; then
        echo -e "${RED}Error: Git is not installed!${NC}"
        echo -e "Please install Git first with: sudo apt install git"
        exit 1
    fi
}

# Function to check if we're in a Git repository
CheckGitRepo() {
    if [ ! -d "$PROJECT_DIR/.git" ]; then
        echo -e "${RED}Error: Not a Git repository!${NC}"
        echo -e "Run '$0 init' first to initialize the repository."
        exit 1
    fi
}

# Function to initialize repository
InitializeRepo() {
    echo -e "${GREEN}Initializing Git repository for $REPO_NAME...${NC}"
    
    # Make sure we're in the project directory
    cd "$PROJECT_DIR" || { echo -e "${RED}Error: Cannot find project directory at $PROJECT_DIR${NC}"; exit 1; }
    
    # Check if .git already exists
    if [ -d ".git" ]; then
        echo -e "${YELLOW}Repository already initialized!${NC}"
        
        # Ask if user wants to reset it
        read -p "Do you want to reset the repository? This will delete all commit history! (y/N): " RESET
        if [[ $RESET == "y" || $RESET == "Y" ]]; then
            rm -rf .git
            echo -e "${GREEN}Repository reset.${NC}"
        else
            echo -e "${GREEN}Using existing repository.${NC}"
            return
        fi
    fi
    
    # Create .gitignore file if it doesn't exist
    if [ ! -f ".gitignore" ]; then
        echo -e "${GREEN}Creating .gitignore file...${NC}"
        cat > .gitignore << EOF
# Python
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

# Virtual Environment
venv/
.venv/
ENV/

# IDE files
.idea/
.vscode/*
!.vscode/settings.json

# OS specific files
.DS_Store
Thumbs.db
EOF
    fi
    
    # Initialize the local repository
    git init
    
    # Add all files
    git add .
    
    # Initial commit
    git commit -m "Initial commit"
    
    # Add GitHub remote
    echo -e "${GREEN}Adding GitHub remote...${NC}"
    git remote add origin "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"
    
    echo -e "${GREEN}Repository initialized successfully!${NC}"
    echo
    echo -e "${YELLOW}Next steps:${NC}"
    echo -e "1. Create a new repository on GitHub named '$REPO_NAME'"
    echo -e "   Visit: https://github.com/new"
    echo -e "2. Push your code with: $0 update"
}

# Function to update repository
UpdateRepo() {
    # Make sure we're in the project directory
    cd "$PROJECT_DIR" || { echo -e "${RED}Error: Cannot find project directory at $PROJECT_DIR${NC}"; exit 1; }
    
    # Check if it's a Git repository
    CheckGitRepo
    
    # Get commit message
    COMMIT_MSG="$1"
    if [ -z "$COMMIT_MSG" ]; then
        # No message provided, ask for one
        read -p "Enter commit message: " COMMIT_MSG
        if [ -z "$COMMIT_MSG" ]; then
            COMMIT_MSG="Updated repository"
        fi
    fi
    
    echo -e "${GREEN}Updating repository...${NC}"
    
    # Show status
    git status
    
    # Add all new and modified files
    git add .
    
    # Commit changes
    git commit -m "$COMMIT_MSG"
    
    # Pull latest changes from remote (to merge any changes)
    echo -e "${GREEN}Pulling latest changes from remote...${NC}"
    git pull origin main || git pull origin master || echo -e "${YELLOW}No remote changes to pull or remote not yet set up.${NC}"
    
    # Push changes to GitHub
    echo -e "${GREEN}Pushing changes to GitHub...${NC}"
    git push -u origin main || git push -u origin master || {
        echo -e "${YELLOW}First push to new repository...${NC}"
        # Ask which branch name to use (main or master)
        read -p "Which branch name do you want to use? (main/master) [main]: " BRANCH_NAME
        BRANCH_NAME=${BRANCH_NAME:-main}
        
        echo -e "${GREEN}Creating $BRANCH_NAME branch and pushing...${NC}"
        git branch -M $BRANCH_NAME
        git push -u origin $BRANCH_NAME
    }
    
    echo -e "${GREEN}Repository updated successfully!${NC}"
}

# Function to check repository status
CheckStatus() {
    # Make sure we're in the project directory
    cd "$PROJECT_DIR" || { echo -e "${RED}Error: Cannot find project directory at $PROJECT_DIR${NC}"; exit 1; }
    
    # Check if it's a Git repository
    CheckGitRepo
    
    echo -e "${GREEN}Repository status:${NC}"
    git status
    
    echo -e "\n${GREEN}Recent commits:${NC}"
    git log --oneline -n 5
}

# Main script execution
CheckGitInstalled

# Process command line arguments
COMMAND="$1"
shift  # Shift arguments to the left (remove $1)

case "$COMMAND" in
    "init")
        InitializeRepo
        ;;
    "update")
        UpdateRepo "$*"  # Pass all remaining args as commit message
        ;;
    "status")
        CheckStatus
        ;;
    "help"|"--help"|"-h"|"")
        ShowUsage
        ;;
    *)
        echo -e "${RED}Unknown command: $COMMAND${NC}"
        ShowUsage
        exit 1
        ;;
esac

exit 0
