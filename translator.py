# translator.py

from deep_translator import GoogleTranslator
from langdetect import detect

# Global variable to track translations
translations_count = 0

# Function to translate reviews using Deep Translator
def translate_review(review):
    global translations_count  # Use the global variable to track the count of translations
    try:
        if not review:
            return review  # If empty or None, return the original review
        
        # Detect the language of the review
        detected_language = detect(review)
        
        # Translate only if the review is not in English
        if detected_language != 'en':
            translated = GoogleTranslator(source='auto', target='en').translate(review)
            translations_count += 1  # Increment the count for each translation
            return translated  # Return the translated text
        else:
            return review  # If it's already in English, return the original review
    except Exception as e:
        print(f"Error during translation: {e}")
        return review  # If error occurs, return the original review

# Function to get the current translation count
def get_translations_count():
    return translations_count












