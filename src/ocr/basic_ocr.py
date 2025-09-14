import easyocr
import time
from preprocessor import preprocess_text  # <-- IMPORT
from parser import parse_declarations, load_rules

# --- 1. Define the path to your image ---
IMAGE_PATH = r"D:\Pyhton\ecommerce-compliance-checker\data\Test_image_5.jpg"

print("Initializing EasyOCR reader...")
# --- 2. Initialize the EasyOCR reader ---
# This loads the English language model into memory. 
# You only need to do this once.
reader = easyocr.Reader(['en'], gpu=True) 
print("Reader initialized.")

print(f"\nProcessing image: {IMAGE_PATH}")
start_time = time.time()

# --- 3. Read text from the image ---
# This is where the magic happens. The model finds and reads text.
result = reader.readtext(IMAGE_PATH)

end_time = time.time()
print(f"Processing finished in {end_time - start_time:.2f} seconds.")

# --- 4. Process and print the results ---
print("\n--- OCR Raw Output ---")
# The 'result' is a list of tuples, where each tuple is (bounding_box, text, confidence)
# We loop through it to extract just the text.
extracted_text = ""
for (bbox, text, prob) in result:
    print(f'Detected text: "{text}" with confidence {prob:.4f}')
    extracted_text += text + " "

print("\n--- Combined Extracted Text ---")
print(extracted_text)




# 2. PRE-PROCESS THE TEXT
cleaned_text = preprocess_text(extracted_text)


# --- STEP 3: PARSE THE CLEANED TEXT ---
# Here we use the functions from your import
if cleaned_text:
    rules = load_rules(r'D:\Pyhton\ecommerce-compliance-checker\src\ocr\rules.json') # Load the regex patterns
    structured_data = parse_declarations(cleaned_text, rules) # Apply the patterns
    
    print("\n--- Final Structured Data ---")
    print(structured_data)
else:
    print("\nNo text extracted, skipping parsing.")