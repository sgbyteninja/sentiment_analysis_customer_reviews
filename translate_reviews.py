
from langdetect import detect
from googletrans import Translator

def translate_if_not_english(text):
    try:
        if detect(text) != 'en':  # If not English
            translator = Translator()
            translated = translator.translate(text, src=detect(text), dest='en')
            return translated.text
        else:
            return text  # Return the original text if it's in English
    except Exception as e:
        print(f"An error occurred while translating the text: {e}")
        return text

def translate_reviews(df):
    try:
        df['review'] = df['review'].apply(translate_if_not_english)
        print("Translation completed successfully without errors.")
    except Exception as e:
        print(f"An error occurred during the translation process: {e}")


