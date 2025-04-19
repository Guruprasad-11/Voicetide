import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
MAX_COMMENTS = int(os.getenv("MAX_COMMENTS", 100))

# Optional safety check
if not YOUTUBE_API_KEY:
    raise ValueError("Missing YOUTUBE_API_KEY in environment variables.")
