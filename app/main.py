from fastapi import FastAPI, HTTPException
from app.utils import calculate_metrics, preprocess_data, generate_csv, fetch_reviews
from app.sentiment_analysis import analyze_sentiment, generate_insights
from app.visualization import generate_visualizations

app = FastAPI()

@app.get("/collect_reviews")
def collect_reviews(app_name: str, app_id: str):
    try:
        reviews = fetch_reviews(app_name, app_id)
        return reviews
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_metrics")
def get_metrics(app_name: str, app_id: str):
    try:
        reviews = fetch_reviews(app_name, app_id)
        data = preprocess_data(reviews)
        metrics = calculate_metrics(data)
        sentiments = analyze_sentiment(data.to_dict(orient="records"))
        data["sentiment"] = [s["sentiment"] for s in sentiments]
        generate_visualizations(data)
        return {
            "metrics": metrics,
            "visualizations": {
                "rating_distribution": "reports/rating_distribution.png",
                "sentiment_distribution": "reports/sentiment_distribution.png"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download_reviews")
def download_reviews(app_name: str, app_id: str):
    try:
        reviews = fetch_reviews(app_name, app_id)
        csv_file = generate_csv(reviews)
        return {"message": "CSV generated successfully", "file_path": csv_file}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  
    
@app.get("/get_sentiments")
def get_sentiments(app_name: str, app_id: str):
    try:
        reviews = fetch_reviews(app_name, app_id)
        data = preprocess_data(reviews)
        sentiments = analyze_sentiment(data.to_dict(orient="records"))
        return sentiments
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_insights")
def get_insights(app_name: str, app_id: str):
    try:
        reviews = fetch_reviews(app_name, app_id)
        data = preprocess_data(reviews)
        sentiments = analyze_sentiment(data.to_dict(orient="records"))
        review_texts = [review["review"] for review in sentiments if review["sentiment"] == "negative"]
        insights = generate_insights(review_texts)
        return insights
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))