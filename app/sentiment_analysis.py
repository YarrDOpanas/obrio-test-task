from textblob import TextBlob
from collections import Counter
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
import re

STOPWORDS = set(stopwords.words('english'))


def analyze_sentiment(reviews):
    sentiment_results = []
    for review in reviews:
        analysis = TextBlob(review["cleaned_review"])
        polarity = analysis.sentiment.polarity
        sentiment = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
        sentiment_results.append({
            "title": review["title"],
            "sentiment": sentiment,
            "review": review["review"], 
            "cleaned_review": review["cleaned_review"]
        })
    return sentiment_results

def generate_insights(reviews):
    text = " ".join(reviews).lower()
    text = re.sub(r"[^a-z\s]", "", text)  # Remove special characters

    words = [word for word in text.split() if word not in STOPWORDS]  # Remove stopwords

    # print("Words:", words)

    # Extract bigrams & trigrams
    bigrams = list(nltk.bigrams(words))
    trigrams = list(nltk.trigrams(words))
    
    # Convert to readable phrases
    bigram_phrases = [" ".join(b) for b in bigrams]
    trigram_phrases = [" ".join(t) for t in trigrams]

    # Count occurrences
    all_phrases = bigram_phrases + trigram_phrases
    phrase_counts = Counter(all_phrases)

    # Filter only relevant issues
    common_issues = [(phrase, count) for phrase, count in phrase_counts.most_common(20)]
    
    suggestions = []
    for issue, _ in common_issues:
        if "crash" in issue or "freeze" in issue:
            suggestions.append("Fix crashes and freezing issues.")
        elif "slow" in issue or "lag" in issue:
            suggestions.append("Improve app performance and speed.")
        elif "ads" in issue:
            suggestions.append("Reduce the number of ads or provide an ad-free option.")
        elif "battery drain" in issue:
            suggestions.append("Optimize battery consumption.")
        elif "not work" in issue or "error" in issue:
            suggestions.append("Fix critical errors preventing the app from functioning properly.")
        elif "card" in issue or "subscription" in issue or "charge" in issue:
            suggestions.append("Fix subscription and payment issues.")
    
    insights = {
        "common_negative_phrases": common_issues,
        "suggested_improvements": list(set(suggestions))
    }
    
    return insights