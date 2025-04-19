from deep_translator import GoogleTranslator
from langdetect import DetectorFactory
import re
import emoji
import time
import pandas as pd

# Ensure consistent language detection
DetectorFactory.seed = 0

# Retry config
MAX_RETRIES = 3
RETRY_DELAY = 1.0
RATE_LIMIT_SLEEP = 0.5

def needs_translation(text: str) -> bool:
    """
    Checks if a given text likely needs translation to English.
    """
    if not text or len(text.strip()) == 0:
        return False

    # Remove emojis for language detection
    clean_text = emoji.replace_emoji(text, replace='')

    if len(clean_text.strip()) == 0:
        return False

    # If the text contains 3 or more English letters, assume it's English
    if re.search(r'[a-zA-Z]{3,}', clean_text):
        return False

    return True

def translate_comments(df: pd.DataFrame) -> pd.DataFrame:
    """
    Translates non-English comments in a DataFrame to English.
    Adds a new column 'translated'.
    """
    if 'comment' not in df.columns:
        raise ValueError("Missing 'comment' column in DataFrame.")

    translations = []

    # Ensure no NaNs in 'comment'
    df['comment'] = df['comment'].fillna('')

    for i, comment in enumerate(df['comment']):
        try:
            if not needs_translation(comment):
                translations.append(comment)
                continue

            for attempt in range(MAX_RETRIES):
                try:
                    translated = GoogleTranslator(source='auto', target='en').translate(comment)
                    break
                except Exception as e:
                    if attempt == MAX_RETRIES - 1:
                        print(f"[ERROR] Translation failed: '{comment}'")
                        translated = f"[TRANSLATION FAILED] {comment}"
                    time.sleep(RETRY_DELAY)

            translations.append(translated)

            # Rate limiting
            if i % 5 == 0:
                time.sleep(RATE_LIMIT_SLEEP)

        except Exception as e:
            print(f"[ERROR] Unexpected error translating comment: {e}")
            translations.append(comment)

    df['translated'] = translations
    return df
