import re
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
import streamlit as st
import plotly.express as px
from process_diary import get_list_of_files, read_diary

list_of_files = get_list_of_files(".")
book = read_diary(list_of_files)
#A way to check pre-filtering word length
# for date, value in book.items():
#     print("pre-filtered")
#     print(date)
#     print(len(value)) 
english_stopwords = stopwords.words("english")
english_stopwords
analyzer = SentimentIntensityAnalyzer()
regex = re.compile("[a-zA-Z]+")
filtered_book = {}

for date, value in book.items():
    pattern = re.findall(regex, value.lower())
    for word in pattern:
        if word not in english_stopwords:
            if date not in filtered_book.keys():
                filtered_book[date] = word  + " "
            else:
                filtered_book[date] += word + " "

sentiment_scores = {}
for date, value in filtered_book.items():
    scores = analyzer.polarity_scores(value)
    if date not in sentiment_scores.keys():
        sentiment_scores[date] = scores
    else:
        sentiment_scores[date] += scores


# st.title("Diary Sentiment Analysis")
dates = [date for date in sentiment_scores.keys()]
dates_sorted = sorted(dates)
positive_sentimate = [ dict["pos"] for dict in sentiment_scores.values() ]
negative_sentimate =  [ dict["neg"] for dict in sentiment_scores.values()]
print(positive_sentimate)
print(negative_sentimate)

# st.title("Positive Sentiment Analysis")
# positive_figures = px.line(x=dates_sorted, y=positive_sentimate, labels={"x": "Date", "y": "Senstiment value"})
# st.plotly_chart(positive_figures)

# st.title("Negative Sentiment Analysis")
# positive_figures = px.line(x=dates_sorted, y=negative_sentimate, labels={"x": "Date", "y": "Senstiment value"})
# st.plotly_chart(positive_figures)


