import re

def to_lowercase(text):
    """Converts text to lowercase."""
    return text.lower()

def remove_special_characters(text):
    """Removes unwanted special characters, keeping essentials."""
    # This regex keeps letters, numbers, spaces, and essential punctuation (.,/,:)
    pattern = r'[^a-z0-9\s\.,/:₹]'
    return re.sub(pattern, '', text)

def standardize_terms(text):
    """Standardizes common variations of key terms."""
    # This dictionary maps variations to a standard term.
    # This is a critical step for reliable parsing.
    corrections = {
        r'm\.?r\.?p\.?': 'mrp',
        r'max retail price': 'mrp',
        r'net\s*wt\.?' : 'net wt',
        r'net\s*quantity' : 'net wt',
        r'pkd\.?' : 'mfg date',
        r'mfg\.?' : 'mfg date',
        r'mfd\.?' : 'mfg date',
        r'made\s+in': 'country of origin'
    }
    
    for pattern, replacement in corrections.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        
    return text

def preprocess_text(text):
    """
    The main pre-processing pipeline that applies all cleaning steps.
    """
    print("\n--- Pre-processing Text ---")
    
    # Step 1: Convert to lowercase
    text = to_lowercase(text)
    
    # Step 2: Standardize key terms (e.g., "M.R.P." becomes "mrp")
    text = standardize_terms(text)
    
    # Step 3: Remove any remaining non-essential special characters
    text = remove_special_characters(text)
    
    print("Cleaned Text:", text)
    return text


