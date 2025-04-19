# Voicetide

**Voicetide** is an intelligent YouTube comment analysis and translation platform. It helps you uncover sentiment, generate viewer suggestions, and summarize audience feedback — all from a single video URL. Ideal for content creators, marketers, and researchers seeking actionable insights from real audience engagement.

---

## Features

- **Fetch YouTube Comments**  
  Collects a specified number of comments from any public YouTube video using the YouTube Data API.

- **Translate Comments**  
  Automatically translates multilingual comments into English using deep translation tools.

- **Sentiment Analysis**  
  Uses VADER NLP to classify each comment as Positive, Negative, or Neutral.

- **Viewer Suggestions**  
  Suggests viewer-centric ideas or topics based on common patterns and themes in comments.

- **Comment Summarization**  
  Summarizes the full body of comments using a transformer model (BART) to generate concise summaries.

- **Search & Filter**  
  Allows users to search by keyword and filter by sentiment to explore specific feedback.

- **Visualized Insights**  
  Provides interactive charts and comment tables via a clean Streamlit interface.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- A Google API key with access to the YouTube Data API v3

### Setup Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/voicetide.git
   cd voicetide
   ```

2. Create a virtual environment:
   ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set Up Environment Variables:
    Create a `.env` file in the root directory of the project and add your YouTube API key:
    ```ini
    YOUTUBE_API_KEY=your_google_api_key
    MAX_COMMENTS=100  # Set the max number of comments you want to fetch
    ```

5. Run the application:
    ```bash
    streamlit run app.py
    ```
The app will open in your browser, where you can input a YouTube video URL, fetch and analyze comments.

## Project Structure

The project consists of several Python files and folders that are used for different functionalities.

| File | Description |
|------|-------------|
| `app.py` | The main file for running the Streamlit app |
| `config.py` | Configuration file for constants like the API key and max comments limit |
| `translator.py` | Contains functions to translate comments to English |
| `comment_fetcher.py` | Fetches comments from a YouTube video using the YouTube API |
| `sentiment.py` | Contains sentiment analysis functions using the VADER sentiment analyzer |
| `summarizer.py` | Summarizes the fetched comments using a transformer-based model |
| `viewer_suggestion.py` | Generates viewer suggestions based on the comments |
| `requirements.txt` | A file listing all the dependencies for the project |

## How It Works

1. **Input YouTube Video URL**  
   The user enters a YouTube video URL, and the app fetches the comments from the video using the YouTube Data API.

2. **Translate Comments**  
   The app automatically translates all comments into English (or a specified language) to ensure consistency for analysis.

3. **Sentiment Analysis**  
   Each comment's sentiment is analyzed using VADER Sentiment Analysis, which classifies comments as:
   - Positive
   - Negative
   - Neutral

4. **Viewer Suggestions**  
   Based on the analyzed comments, the app generates a list of viewer suggestions to recommend relevant videos or topics.

5. **Summary**  
   All comments are summarized using a transformer model, which condenses the key points from the comments.

6. **Search and Filter**  
   Users can:
   - Search for specific keywords in the comments
   - Filter the results by sentiment (Positive, Negative, Neutral)

7. **Visualization**  
   The app uses Streamlit's interactive components to display results, including:
   - Sentiment pie charts
   - Tables showing the comments

## Usage

Once the app is running, follow these steps:

1. **Enter a YouTube Video URL**  
   In the input field, paste the URL of a YouTube video.

2. **Click "Process Comments"**  
   The app will:
   - Fetch comments from the video
   - Translate them
   - Analyze their sentiment

3. **Navigate Through Tabs**:
   - **Sentiment**: View the sentiment distribution of comments in a pie chart
   - **Suggestions**: View viewer suggestions generated from the comments
   - **Search & Filter**: Search for keywords and filter by sentiment
   - **Summary**: View a summary of the comments

## Contributor Guide
### Setting Up for Development
    git clone https://github.com/Guruprasad-11/Voicetide.git
    cd Voicetide
    git checkout -b feature-name
    pip install -r requirements.txt

### Development Workflow
1. Make your changes

2. Test locally:
    ```bash
    streamlit run app.py
    ```

3. Commit changes:
    ```bash
    git add .
    git commit -m "Your commit message"
    git push origin feature-name
    ```

4. Open a pull request

### Code Style
- Follow PEP8 guidelines
- Use descriptive docstrings
- Maintain consistent naming conventions

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.