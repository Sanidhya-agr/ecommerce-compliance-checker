import re
import json

def load_rules(rules_path=r'D:\Pyhton\ecommerce-compliance-checker\src\ocr\rules.json'):
    """
    Loads parsing rules from a JSON file.
    The path should be relative to your project's root folder.
    """
    try:
        with open(rules_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The rules file was not found at {rules_path}")
        print("Please ensure 'rules.json' exists in the 'src' directory.")
        return None

def parse_declarations(text, rules_config):
    """
    Parses a block of text using dynamically loaded rules from the config.
    """
    # Return an empty dictionary if the rules failed to load
    if not rules_config:
        return {}

    declarations = {}
    
    # Iterate through each rule defined in the JSON file
    for rule in rules_config['declarations']:
        key = rule['key']
        declarations[key] = None # Initialize the key with a null value

        # Try each pattern associated with the current rule
        for pattern in rule['patterns']:
            # Search for the pattern in the cleaned text (case-insensitive)
            match = re.search(pattern, text, re.IGNORECASE)
            
            if match:
                # If a match is found, store the first captured group (the value)
                value = match.group(1).strip()
                declarations[key] = value
                break # Move to the next rule once a match is found
    
    return declarations