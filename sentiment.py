from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(df):
    """
    Analyzes sentiment of each comment and adds a 'sentiment' column.
    Classifies into Positive, Negative, or Neutral based on the compound score.
    """
    # List to store sentiment classifications
    sentiments = []

    for comment in df['translated']:
        # Get the sentiment score from VADER
        sentiment_score = analyzer.polarity_scores(comment)
        
        # Extract compound score
        compound = sentiment_score['compound']
        
        # Classify based on compound score
        if compound >= 0.05:
            sentiments.append('Positive')
        elif compound <= -0.05:
            sentiments.append('Negative')
        else:
            sentiments.append('Neutral')
    
    # Add a new column 'sentiment' to the DataFrame
    df['sentiment'] = sentiments
    return df
