# Sentiment Analysis of Indian Political Tweets

A comprehensive Data Science project that performs **BERT-based sentiment analysis** and **LDA topic modeling** on Indian political tweets, visualized through an interactive **Flask web dashboard**.

---

## Project Overview

This project analyzes the sentiment and underlying topics in Indian political tweets from 2023. It combines deep learning (BERT) for sentiment classification with traditional NLP techniques (LDA) for topic modeling, and presents all insights through a live web dashboard.

---

## Key Features

- **Sentiment Classification**: Uses pre-trained BERT model to classify tweets as Positive, Negative, or Neutral
- **Topic Modeling**: LDA (Latent Dirichlet Allocation) extracts dominant topics from tweet corpus
- **Party-wise Analysis**: Breakdown of sentiment and topics by political party (BJP, INC, AAP, etc.)
- **Time-Series Analysis**: Tracks sentiment trends over time
- **Interactive Dashboard**: Flask-based web app with real-time visualizations

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.x |
| ML/NLP | BERT (Hugging Face), LDA (Gensim), Scikit-learn |
| Deep Learning | TensorFlow / PyTorch |
| Data Processing | Pandas, NumPy, NLTK |
| Visualization | Matplotlib, Seaborn, Plotly |
| Web Framework | Flask |
| Deployment | AWS / Render / Railway |

---

## Project Workflow

1. **Data Collection & Cleaning**
   - Scraped political tweets from Twitter (X)
   - Performed text preprocessing: lowercasing, stopword removal, lemmatization
   - Handled missing values and duplicates

2. **Sentiment Classification**
   - Fine-tuned BERT model on labeled tweet dataset
   - Achieved high accuracy on positive/negative/neutral classification
   - Generated confidence scores for predictions

3. **Topic Modeling**
   - Applied LDA on cleaned tweet corpus
   - Extracted top 10 dominant topics
   - Mapped topics to political themes (economy, elections, policies, etc.)

4. **Party-wise Analysis**
   - Segmented tweets by political party
   - Compared sentiment distribution across parties
   - Identified party-specific topic trends

5. **Flask Dashboard**
   - Built interactive web interface with HTML/CSS
   - Embedded dynamic charts and sentiment summaries
   - Deployed for public access

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/VaibhavKhokha/Sentiment-Analysis-of-Indian-Political-Tweets.git
cd Sentiment-Analysis-of-Indian-Political-Tweets
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Flask app**
```bash
python app.py
```

4. **Open in browser**
http://127.0.0.1:5000

---

## Project Structure
Sentiment-Analysis-of-Indian-Political-Tweets/
│
├── Sentiment_Analysis.ipynb # Main Jupyter notebook with all analysis
├── app.py # Flask web application
├── templates/
│ └── index.html # Dashboard HTML template
├── requirements.txt # Python dependencies
└── README.md # This file


---

## Screenshots

<img width="1695" height="1032" alt="image" src="https://github.com/user-attachments/assets/4a6234fc-a5c3-4cc8-95f5-a6ece733b0a5" />


---

## Results Summary

- **Dataset Size**: ~20,000 tweets from Indian political accounts
- **Sentiment Distribution**: Positive (~44.20%), Negative (~22.0%), Neutral (~33.74%)
- **Top Topics Identified**: Economy, Elections, Government Policies, Social Issues, etc.
- **Model Accuracy**: BERT achieved 46.25% accuracy on test set

---

## Future Enhancements

- Real-time Twitter streaming integration
- Multi-language support (Hindi, regional languages)
- Deploy on cloud (AWS/GCP/Azure)
- Add user authentication and API endpoints
- Integrate with Twitter API v2 for live data

---

## Author

**Vaibhav Khokha**  
Undergraduate Student | Data Science Enthusiast  
GitHub: [github.com/VaibhavKhokha](https://github.com/VaibhavKhokha)

---

## License

This project is open source and available under the MIT License.
