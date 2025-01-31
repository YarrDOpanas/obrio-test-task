# Apple Store Review Analysis API

## Overview
This API collects, processes, and analyzes user reviews from the Apple Store for a specified app, providing actionable insights and metrics.

## Features
- Fetch 100 reviews for a specified app.
- Calculate average ratings and rating distribution.
- Perform sentiment analysis on reviews.
- Provide raw review data for download.

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:YarrDOpanas/obrio-test-task.git
   cd obrio-test-task
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   cd app
   pip install -r requirements.txt
   ```

4. Run the API:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. Access the API documentation:
   ```
   http://127.0.0.1:8000/docs
   ```

## Example usage

### 1️⃣ Collect Reviews
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/collect_reviews?app_name=nebula-horoscope-astrology&app_id=1459969523' \
  -H 'accept: application/json'
```

### 2️⃣ Get Metrics & Visualizations
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/get_metrics?app_name=nebula-horoscope-astrology&app_id=1459969523' \
  -H 'accept: application/json'
```

### 3️⃣ Perform Sentiment Analysis
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/get_sentiments?app_name=nebula-horoscope-astrology&app_id=1459969523' \
  -H 'accept: application/json'
```

### 4️⃣ Get Insights (Actionable Improvements)
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/get_insights?app_name=nebula-horoscope-astrology&app_id=1459969523' \
  -H 'accept: application/json'
```

### 5️⃣ Download Reviews as CSV
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/download_reviews?app_name=nebula-horoscope-astrology&app_id=1459969523' \
  -H 'accept: application/json'
```