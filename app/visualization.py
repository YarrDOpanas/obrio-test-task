import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_visualizations(data):
    os.makedirs("reports", exist_ok=True)
    
    # Rating Distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(x=data['rating'], palette='viridis')
    plt.title("Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.savefig("reports/rating_distribution.png")
    plt.close()
    
    # Sentiment Distribution
    plt.figure(figsize=(8, 6))
    sentiment_counts = data['sentiment'].value_counts()
    sentiment_counts.plot(kind='bar', color=['green', 'gray', 'red'])
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.savefig("reports/sentiment_distribution.png")
    plt.close()