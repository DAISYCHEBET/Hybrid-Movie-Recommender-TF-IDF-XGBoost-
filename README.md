This project is a Hybrid Movie Recommender that combines content-based filtering using TF-IDF Vectorization with a machine learning classifier (XGBoost) to provide personalized movie suggestions. The dataset used for training was scraped from the OMDb API, containing key movie attributes such as title, genre, plot, director, actors, and IMDb ratings.

The goal of the project is to leverage both the semantic similarity of movie descriptions (via TF-IDF) and predictive modeling (via XGBoost) to recommend movies that closely align with user preferences.

📖 Project Description

Movie recommendation systems are widely used by streaming platforms to enhance user experience. Traditional recommendation systems are either:
Content-based: Recommend movies similar to what a user has already liked, based on metadata (plot, genre, etc.)
Collaborative filtering: Recommend movies based on patterns of user behavior and preferences.
This project introduces a hybrid approach:

Scraping Movie Data

Movie details were collected from the OMDb API.

The dataset includes fields like Title, Year, Genre, Plot, Director, Actors, IMDb Rating, etc.

Text Preprocessing

Movie plots and metadata were cleaned and normalized.

Stopwords were removed and text was transformed into numerical vectors.

Feature Extraction (TF-IDF)

TF-IDF (Term Frequency – Inverse Document Frequency) was used to convert movie descriptions into vectorized form.

This allowed the system to measure semantic similarity between different movies.

Model Training (XGBoost Classifier)

An XGBoost classifier was trained on the vectorized dataset to learn patterns in user preferences.

The model predicts whether a user is likely to enjoy a movie based on extracted features.

Hybrid Recommendation

Movies are ranked based on both cosine similarity (TF-IDF) and model predictions (XGBoost).

This ensures recommendations are not only similar in description but also optimized by learned patterns.


🚀 Project Workflow

Data Scraping → Movie data fetched from OMDb API.

Preprocessing → Cleaning and preparing metadata (plots, genres, actors).

TF-IDF Vectorization → Converting text into numerical feature vectors.

Model Training (XGBoost) → Training and evaluating the classifier.

Recommendation Engine → Hybrid approach using TF-IDF + XGBoost for final recommendations.

🔑 Key Features

Uses real-world movie metadata scraped from OMDb.

TF-IDF captures semantic similarity between movie descriptions.

XGBoost classifier improves prediction accuracy.

Hybrid recommendation balances content similarity and machine learning predictions.

Exploratory Data Analysis (EDA) with visual insights on the dataset.


📌Interpretation:

The model achieved a good balance between precision and recall.

It correctly identified 37 non-recommended movies and 18 recommended movies, with some trade-offs in misclassifications.

🛠️Libraries Used

The project was implemented using the following main libraries:

pandas → Data manipulation

numpy → Numerical computations

scikit-learn → TF-IDF vectorization & evaluation metrics

xgboost → Machine learning classifier


⚙️Requirements

You can then install dependencies with:
pip install -r requirements.txt


📈 Future Improvements

Deploy the recommendation engine with FastAPI/Streamlit.
