# Sentiment Analysis of Indian Political Tweets

## Overview
This project analyzes the sentiment of Indian political tweets using Deep Learning (BERT) and compares it with VADER. It also includes topic modeling (LDA) and an interactive Flask web dashboard.

## Dataset
- **Source**: Kaggle - Indian Political Tweets Sentiment Analysis (saurabhshahane)
- **Total Tweets**: 162,980
- **Working Sample**: 20,000 tweets
- **Categories**: Positive, Neutral, Negative

## Models Used
1. **BERT (finiteautomata/bertweet-base-sentiment-analysis)** - Transformer-based deep learning model
2. **VADER** - Rule-based lexicon approach for comparison
3. **LDA (Latent Dirichlet Allocation)** - Topic modeling to discover 5 key discussion topics

## Key Findings
- BERT Overall Accuracy: ~46%
- Topic 3 (India, nation, space mission) has highest positive sentiment (33.7%)
- Topic 4 (Gandhi, Nehru references) has highest negative sentiment (44.5%)
- BJP tweets show higher positive sentiment (15.9%) vs INC (9.5%)
- VADER classifies more tweets as positive compared to BERT

## Files
- app.py - Flask web application
- templates/index.html - Web dashboard UI
- sentiment_analysis_results.csv - Complete predictions
- project_statistics.json - All numerical results
- topic_modeling_stats.json - LDA topic analysis
- requirements.txt - Python dependencies

## Running the Dashboard
Then open http://127.0.0.1:5000 in your browser.

## Requirements
pip install transformers pandas numpy matplotlib seaborn wordcloud scikit-learn vaderSentiment flask torch

## Author
Project developed by Vaibhav Khokha
