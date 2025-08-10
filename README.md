# Hybrid Movie Recommendation System

This project is a movie recommendation system that combines content-based features and machine learning classification to predict and recommend movies. Using data scraped from the OMDb API, the system leverages TF-IDF vectorization to transform textual metadata into numerical features, and an XGBoost classifier to predict movie preferences.

The project demonstrates how natural language processing and machine learning can be integrated for building recommendation systems.

📊Data Collection & Preprocessing

Movie metadata was scraped using the OMDb API.

Textual features (e.g., plot summaries, genres, keywords) were transformed into numerical vectors using TF-IDF (Term Frequency–Inverse Document Frequency).

The processed data was then used to train and evaluate the model.

🤖Model Training

XGBoost Classifier was used for classification.

A custom threshold of 0.6 was applied to balance precision and recall.

The model was trained on the processed dataset and evaluated using classification metrics.

📈 Model Evaluation
Classification Report (Threshold = 0.6)
Class	Precision	Recall	F1-Score	Support
0 (Not Recommended)	0.84	0.80	0.82	46
1 (Recommended)	0.67	0.72	0.69	25

Accuracy: 0.77
Macro Avg F1-Score: 0.76
Weighted Avg F1-Score: 0.78

Confusion Matrix
[[37   9]
 [ 7  18]]


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

