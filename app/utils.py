import pandas as pd
import os
import string
from app_store_scraper import AppStore


def preprocess_data(reviews):
    df = pd.DataFrame(reviews)
    df["cleaned_review"] = df["review"].str.lower().str.replace(r'[^\w\s]', '')
    df["cleaned_review"] = df["cleaned_review"].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
    return df

def calculate_metrics(data):
    avg_rating = data["rating"].mean()
    rating_dist = data["rating"].value_counts(normalize=True) * 100
    rating_dist = rating_dist.astype(int)
    return {
        "average_rating": avg_rating,
        "rating_distribution": rating_dist.to_dict()
    }

def generate_csv(reviews):
    df = pd.DataFrame(reviews)
    file_path = os.path.join("reports", "reviews.csv")
    df.to_csv(file_path, index=False)
    return file_path

def fetch_reviews(app_name, app_id, country='us', num_reviews=100):
    app = AppStore(country=country, app_name = app_name, app_id = app_id)
    app.review(how_many=num_reviews)
    return app.reviews