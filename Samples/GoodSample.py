# File: GoodSample.py
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
