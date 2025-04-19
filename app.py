import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from translator import translate_comments
from comment_fetcher import fetch_comments
from sentiment import analyze_sentiment
from viewer_suggestion import get_viewer_suggestions
from summarizer import summarize_comments  # Importing summarize function
from config import MAX_COMMENTS

# --- Helper Functions ---

def plot_sentiment_pie(df):
    st.subheader("Sentiment Distribution")
    sentiment_count = df['sentiment'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(sentiment_count, labels=sentiment_count.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Makes the pie a circle
    st.pyplot(fig)

def display_viewer_suggestions(suggestions):
    st.subheader("Viewer Suggestions")
    if suggestions:
        for idx, suggestion in enumerate(suggestions[:5], 1):
            st.markdown(f"{idx}. {suggestion}")
    else:
        st.info("No viewer suggestions found.")

def display_filtered_comments(df, search_query, sentiment_filter):
    filtered_df = df.copy()

    if search_query:
        filtered_df = filtered_df[filtered_df['comment'].str.contains(search_query, case=False, na=False)]

    if sentiment_filter != "All Sentiments":
        filtered_df = filtered_df[filtered_df['sentiment'] == sentiment_filter]

    if filtered_df.empty:
        st.warning("No comments match your filters.")
    else:
        st.write(f"Found {len(filtered_df)} comments:")
        st.dataframe(filtered_df[['user_name', 'comment', 'translated', 'sentiment']])


def display_summary(df):
    """Generate and display the summary of all comments."""
    summary = summarize_comments(df)
    st.subheader("Comments Summary")
    st.write(summary)

# --- Streamlit App ---

st.set_page_config(page_title="YouTube Comment Analyzer", layout="wide")
st.title("YouTube Comment Analyzer & Translator")

url = st.text_input("Enter a YouTube video URL:")

# Initialize session state for DataFrame if not exists
if 'df' not in st.session_state:
    st.session_state.df = None

if st.button("Process Comments") and url:
    with st.spinner("Fetching comments..."):
        st.session_state.df = fetch_comments(url, max_comments=MAX_COMMENTS)

    with st.spinner("Translating comments..."):
        st.session_state.df = translate_comments(st.session_state.df)

    with st.spinner("Analyzing sentiment..."):
        st.session_state.df = analyze_sentiment(st.session_state.df)

    st.success("All processing complete!")

# Displaying results
if st.session_state.df is not None:
    df = st.session_state.df

    # Tabs for better UI
    tab1, tab2, tab3, tab4 = st.tabs(["Sentiment", "Suggestions", "Search & Filter", "Summary"])

    with tab1:
        plot_sentiment_pie(df)

    with tab2:
        suggestions = get_viewer_suggestions(df)
        display_viewer_suggestions(suggestions)

    with tab3:
        st.subheader("Search and Filter Comments")
        search_query = st.text_input("Search by keyword:")
        sentiment_filter = st.selectbox(
            "Filter by sentiment:",
            options=["All Sentiments", "Positive", "Negative", "Neutral"]
        )
        display_filtered_comments(df, search_query, sentiment_filter)

    with tab4:
        display_summary(df)
