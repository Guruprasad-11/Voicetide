import pandas as pd
import re
from translator import translate_comments

# Clean text by removing URLs, mentions, special characters, etc.
def clean_text(text: str) -> str:
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r'\@\w+|\#', '', text)
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    return text.lower().strip()

# Extract viewer suggestions based on keyword phrases
def extract_suggestions(df: pd.DataFrame) -> list:
    keywords = ["should", "make", "video on", "talk about", "cover", "do a video on"]
    suggestions = []

    for comment in df['translated']:
        if any(keyword in comment for keyword in keywords):
            suggestions.append(comment)

    return suggestions

# Full pipeline: clean, translate, extract suggestions
def get_viewer_suggestions(df: pd.DataFrame) -> list:
    df['cleaned_comment'] = df['comment'].astype(str).apply(clean_text)
    df = translate_comments(df)
    return extract_suggestions(df)
