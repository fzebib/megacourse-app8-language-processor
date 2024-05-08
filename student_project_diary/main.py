import glob
import streamlit as st
import plotly.express as px

from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("*.txt"))

analyzer = SentimentIntensityAnalyzer()

negativity = []
positivity = []

for filepath in filepaths:
    with open(filepath, "r") as f:
        scores = analyzer.polarity_scores(f.read())
        positivity.append(scores["pos"])
        negativity.append(scores["neg"])

dates = [filepath.replace(".txt", "") for filepath in filepaths]


print(negativity)
print(positivity)
print(dates)
