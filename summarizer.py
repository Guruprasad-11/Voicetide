from transformers import pipeline

# Load the summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_comments(df):
    """
    Summarizes the comments from the DataFrame and returns the summary.
    """
    # Ensure 'comment' column exists and is not empty
    comments_text = " ".join(df['comment'].dropna())  # Join all comments together

    # Check if there is any comment text to summarize
    if not comments_text.strip():
        return "No comments to summarize."

    # Limit the input text to the model's maximum input length
    max_input_length = 1024  # Adjust as needed

    # Tokenize the input and ensure it doesn't exceed max input length
    tokenized_input = summarizer.tokenizer(comments_text)
    if len(tokenized_input['input_ids']) > max_input_length:
        comments_text = comments_text[:max_input_length]  # Truncate to fit

    # Summarize the comments
    summary = summarizer(comments_text, do_sample=False)

    return summary[0]['summary_text'] if summary else "Error generating summary."
