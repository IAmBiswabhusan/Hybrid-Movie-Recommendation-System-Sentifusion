📽️ Hybrid Movie Recommendation System — Sentifusion
👤 By: Biswabhusan Mohapatra
⭐ Executive Summary

Sentifusion is a Hybrid Movie Recommendation System combining:

Content-Based Filtering

User-Based Collaborative Filtering

Sentiment Analysis

Hybrid Weighted Ranking

Using MovieLens, TMDB, and IMDb datasets, the system predicts a ranked list of movies that the user is likely to enjoy.
A fully functional Flask Web App is also included.

🎯 Problem Statement

Can we predict personalized movie recommendations using metadata + user behavior?

Yes — Sentifusion generates personalized, ranked recommendations using hybrid ML techniques.

📁 Data Sources
1️⃣ MovieLens Dataset

Used for:

User ratings

Collaborative filtering

2️⃣ TMDB Dataset

Used for metadata:

Genre

Overview

Tagline

Keywords

Director, Cast

3️⃣ Sentiment Analysis

Used for:

Generating sentiment_score from overview + keywords + tagline

⚠ Note: Large CSV files (>100 MB) are not included in the GitHub repository.

📊 Exploratory Data Analysis (EDA)






🧠 Approach (Hybrid Modeling)
1️⃣ Popularity-Based Recommender

Simple baseline based on globally popular movies.

2️⃣ Content-Based Filtering

Uses:

TF-IDF Vectorization

Cosine Similarity

Sentiment Scores

Features: overview, tagline, keywords, cast, director

Pros: Works for new users
Cons: Limited diversity

3️⃣ User-Based Collaborative Filtering

Steps:

Build user–movie matrix

Compute user-user cosine similarity

Predict unrated scores

Pros: Good diversity
Cons: Cold start problem

4️⃣ Hybrid Recommender (Sentifusion)

Final score:

Hybrid Score = (Content Score + Collaborative Score) / 2


Benefits:

Tackles cold start

Better diversity

More accurate & stable

📦 Workflow

Data Cleaning

EDA & Visualization

Feature Engineering

NLP (TF-IDF + Sentiment)

Content-Based Model

Collaborative Filtering Model

Hybrid Model

Flask App Implementation

📚 Data Dictionary
Feature	File	Type	Description
movie_id	content.csv	int	MovieLens ID
title	content.csv	object	Movie title
genres	content.csv	object	Genres
overview	content.csv	object	Movie summary
keywords	content.csv	object	Plot keywords
director	content.csv	object	Director
cast	content.csv	object	Cast members
sentiment_score	content.csv	float	Polarity score
user_id	ratings_title.csv	int	User ID
rating	ratings_title.csv	float	Rating (0.5–5)
🏁 Conclusion
✔ Content-Based Filtering

Great for metadata-driven suggestions.

✔ Collaborative Filtering

Captures behavioral patterns.

✔ Hybrid Model

Best overall performance
Better accuracy, diversity, and personalization.

⚠ Limitations

Assumes users only watched rated movies

Large-scale CF can be slow

Metadata files are too large for GitHub

🔧 Tools & Technologies

Languages:

Python

HTML/CSS/JS

ML & NLP:

Scikit-learn

TF-IDF

Sentiment Analysis

Cosine Similarity

Visualization:

Matplotlib

Seaborn

Web App:

Flask

📂 Recommended Project Structure
Hybrid-Movie-Recommender/
│── code/
│── recommender_app/
│── images/
│── data/  (ignored due to size)
│── requirements.txt
│── README.md
