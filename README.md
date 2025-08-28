🎬 Hybrid Movie Recommendation System (FastAPI + XGBoost + TF-IDF)

This project is a Hybrid Movie Recommender that combines content-based filtering using TF-IDF Vectorization with a machine learning classifier (XGBoost) to provide personalized movie suggestions. The dataset used for training was scraped from the OMDb API, containing key attributes such as title, genre, plot, director, actors, and IMDb ratings.

The goal of this project is to leverage both the semantic similarity of movie descriptions (via TF-IDF) and predictive modeling (via XGBoost) to recommend movies that closely align with user preferences. It also includes a FastAPI-powered backend to serve recommendations through a RESTful API.

📖 Project Description

Movie recommendation systems are widely used by streaming platforms to enhance user experience. Traditional systems are typically:

Content-based: Recommend movies similar to those a user has already liked, based on metadata (plot, genre, etc.).

Collaborative filtering: Recommend movies based on user behavior and preference patterns.

This project introduces a hybrid approach:

Scraping Movie Data

Movie details were collected from the OMDb API.

The dataset includes fields like Title, Year, Genre, Plot, Director, Actors, IMDb Rating, etc.

Text Preprocessing

Movie plots and metadata were cleaned and normalized.

Stopwords were removed, and text was transformed into numerical vectors.

Feature Extraction (TF-IDF)

TF-IDF (Term Frequency – Inverse Document Frequency) converts movie descriptions into vectorized form.

This enables the system to measure semantic similarity between different movies.

Model Training (XGBoost Classifier)

An XGBoost classifier was trained on the vectorized dataset to learn patterns in user preferences.

The model predicts whether a user is likely to enjoy a movie based on extracted features.

Hybrid Recommendation

Movies are ranked using both cosine similarity (TF-IDF) and model predictions (XGBoost).

This ensures recommendations are both semantically similar and machine learning optimized.



🚀 Project Workflow

Data Scraping → Movie data fetched from OMDb API.

Preprocessing → Cleaning and preparing metadata (plots, genres, actors).

TF-IDF Vectorization → Converting text into numerical feature vectors.

Model Training (XGBoost) → Training and evaluating the classifier.

API Deployment → Exposing the recommendation engine via FastAPI.

Recommendation Engine → Hybrid approach using TF-IDF + XGBoost for final recommendations.


🌐 FastAPI Backend

This project includes a FastAPI-based API that allows you to query movie recommendations.

Key Endpoints

GET / – Welcome message & usage guide.

GET /recommend?title=MovieTitle – Returns top 10 similar movies based on the provided title.



Running the FastAPI Server
uvicorn app2:app --reload


Base URL: http://127.0.0.1:8000

Swagger Docs: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc



🔑 Key Features

Real-world movie metadata scraped from OMDb.

TF-IDF captures semantic similarity between movie descriptions.

XGBoost classifier improves prediction accuracy.

FastAPI backend enables easy integration with web or mobile apps.

Swagger & ReDoc documentation for easy testing.

Exploratory Data Analysis (EDA) included for insights.



📌 Interpretation

The model achieved a good balance between precision and recall:

Correctly identified 37 non-recommended movies and 18 recommended movies.

Some trade-offs in misclassifications remain.



🛠️ Libraries Used

pandas → Data manipulation

numpy → Numerical computations

scikit-learn → TF-IDF vectorization & evaluation metrics

xgboost → Machine learning classifier

fastapi → API framework

uvicorn → ASGI server

joblib → Model persistence


⚙️ Installation & Setup

Clone this repository

Install dependencies:
pip install -r requirements.txt


Run FastAPI:

uvicorn app2:app --reload



📈 Future Improvements

Deploy a frontend (Gradio/Streamlit) to interact with the API.

Add movie posters & trailers to enrich the experience.

Support user-based collaborative filtering.

Deploy to cloud platforms (Render, Railway, AWS, etc.).
