from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY, MAX_COMMENTS
import pandas as pd
from time import sleep
import re

def extract_video_id(url: str) -> str:
    """
    Extracts the video ID from a YouTube URL.
    """
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return match.group(1) if match else url

def fetch_comments(video_url: str, max_comments: int = MAX_COMMENTS) -> pd.DataFrame:
    """
    Fetches up to `max_comments` comments from a YouTube video.
    """
    video_id = extract_video_id(video_url)
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    comments_data = []
    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )

    while request and len(comments_data) < max_comments:
        try:
            response = request.execute()

            for item in response['items']:
                snippet = item['snippet']['topLevelComment']['snippet']
                replies = item.get("replies", {}).get("comments", [])

                comment_entry = {
                    "comment": snippet.get('textDisplay', ''),
                    "user_name": snippet.get('authorDisplayName', ''),
                    "date": snippet.get('publishedAt', ''),
                    "replies": [reply['snippet'].get('textDisplay', '') for reply in replies]
                }

                comments_data.append(comment_entry)
                if len(comments_data) >= max_comments:
                    break

            request = youtube.commentThreads().list_next(request, response)
            sleep(1)

        except Exception as e:
            print(f"[ERROR] Failed to fetch comments: {e}")
            sleep(5)
            break

    return pd.DataFrame(comments_data)
