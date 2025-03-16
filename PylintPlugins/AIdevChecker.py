
"""Pylint plugin for AIDEV-PascalCase standards."""

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker
from astroid import nodes
import re

class AIDevPascalCaseChecker(BaseChecker):
    """Checker enforcing AIDEV-PascalCase naming conventions."""
    
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
        """Check if a name follows PascalCase convention."""
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
        """Check if special terms are capitalized correctly."""
        for term, correct in self.special_terms.items():
            pattern = re.compile(r'\b' + term + r'\b', re.IGNORECASE)
            if pattern.search(name) and correct not in name:
                return False
        return True
    
    def visit_assignname(self, node):
        """Check variable names."""
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
        """Check function and method names."""
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
    """Register the checker."""
    linter.register_checker(AIDevPascalCaseChecker(linter))
