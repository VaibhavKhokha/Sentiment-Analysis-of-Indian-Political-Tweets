from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from transformers import pipeline
import json

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('Twitter_Data.csv')
df['category'] = df['category'].map({-1.0: 'negative', 0.0: 'neutral', 1.0: 'positive'})

# Load sentiment model
label_map = {'POS': 'positive', 'NEG': 'negative', 'NEU': 'neutral'}
sentiment_pipeline = pipeline("sentiment-analysis", 
                              model="finiteautomata/bertweet-base-sentiment-analysis", 
                              device=0)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    tweet = request.json.get('tweet', '')
    if not tweet:
        return jsonify({'error': 'No tweet provided'}), 400
    
    result = sentiment_pipeline(tweet[:128])
    sentiment = label_map[result[0]['label']]
    confidence = round(result[0]['score'] * 100, 2)
    
    return jsonify({
        'tweet': tweet,
        'sentiment': sentiment,
        'confidence': confidence
    })

@app.route('/stats')
def stats():
    # Return overall statistics
    return jsonify({
        'total_tweets': len(df),
        'positive': int(df['category'].value_counts().get('positive', 0)),
        'neutral': int(df['category'].value_counts().get('neutral', 0)),
        'negative': int(df['category'].value_counts().get('negative', 0))
    })

if __name__ == '__main__':
    print("Starting Flask server...")
    print("Open http://127.0.0.1:5000 in your browser")
    app.run(debug=True)