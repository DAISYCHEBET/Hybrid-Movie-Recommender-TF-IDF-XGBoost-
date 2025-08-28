from fastapi import FastAPI, Query
import pandas as pd
import joblib

app = FastAPI(title="Hybrid Movie Recommendation API")


@app.get("/")
def root():
    return {
        "message": (
            "Welcome to the Hybrid Movie Recommendation API! "
            "Use /recommend?title=MovieTitle or "
            "visit Swagger UI at /docs: http://127.0.0.1:8000/docs"
        )
    }

# --- Load saved files ---
cosine_sim = joblib.load("cosine_similarity.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")
mlb = joblib.load("mlb.pkl")
features = joblib.load("features.pkl")
scaler = joblib.load("scaler.pkl")
model = joblib.load("xgb_best_model.pkl")

# Load movie dataset
full_df = pd.read_json("omdb_movie_data.json")
movies_list = full_df['Title'].tolist()

# Create a lowercase mapping for easy lookup
movies_lower_map = {title.lower(): title for title in movies_list}

@app.get("/recommend")
def recommend_movie(title: str = Query(..., description="Enter a movie title")):
    user_input = title.strip().lower()

    # Try to match ignoring case
    if user_input not in movies_lower_map:
        return {"error": f"Movie '{title}' not found in dataset."}

    # Get the correct title (original formatting)
    matched_title = movies_lower_map[user_input]

    # --- Step 1: Find index ---
    idx = movies_list.index(matched_title)

    # --- Step 2: Get similarity scores ---
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # --- Step 3: Get top 10 similar movies ---
    top_movies_idx = [i for i, _ in sim_scores[1:11]]  # exclude the same movie
    recommended_titles = [movies_list[i] for i in top_movies_idx]

    return {
        "requested_movie": matched_title,  # always returns with proper casing
        "recommended_movies": recommended_titles
    }
