# File: BadSample.py
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
