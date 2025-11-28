# Hybrid Movie Recommendation System — Sentifusion
### By **Biswabhusan Mohapatra**

---

## 1. Overview
**Sentifusion** is a Hybrid Movie Recommendation System combining:

- **Content-Based Filtering**
- **User-Based Collaborative Filtering**
- **Sentiment Analysis on Movie Metadata**
- **Hybrid Weighted Scoring**

The system uses metadata from **TMDB**, ratings from **MovieLens**, and emotional tone extracted from text features to generate highly personalized recommendations.  
A complete **Flask-based Web Application** is also included.

---

## 2. Problem Statement
Can we generate a *ranked list* of movie recommendations for a user using:

- Movie features (overview, tagline, cast, keywords)
- User–movie interactions
- Sentiment analysis  
- Hybrid ML techniques

Sentifusion answers this question with a combined scoring approach.

---

## 3. Data Sources

### **• MovieLens Dataset**
Contains user ratings and is used for collaborative filtering.

### **• TMDB Metadata**
Includes:
- Overview  
- Tagline  
- Keywords  
- Genres  
- Director  
- Cast  

Used for text processing and TF-IDF modeling.

### **• Sentiment Scores**
Calculated from:
- Overview  
- Tagline  
- Keywords  

Used to enhance similarity metrics.

> **Note:** Large CSV files are not stored on GitHub due to the 100MB limit.

---

## 4. Exploratory Data Analysis

Visualizations available in the repository:

- Ratings Distribution  
- Average Rating per Movie  
- Genre Popularity  
- Genre-based Rating Comparison  
- Ratings per Movie  

(Images stored under `images/` directory)

---

## 5. Approach

### **5.1 Popularity-Based Recommender**
A baseline model ranking movies by their overall popularity.

---

### **5.2 Content-Based Filtering**
Uses:

- **TF-IDF Vectorization**
- **Cosine Similarity**
- **Sentiment Polarity**
- Combined metadata features:
  - overview, tagline, keywords  
  - director  
  - cast  

Strengths:
- Works for new users  
- Does not require other users’ ratings  

Limitations:
- Less diverse recommendations  
- Dependent on metadata quality  

---

### **5.3 Collaborative Filtering (User–User)**

Steps:
1. Build user–movie matrix  
2. Compute similarity between users  
3. Predict scores for unseen movies  
4. Recommend movies with highest predicted ratings  

Strengths:
- Better diversity  
- Learns from community preferences  

Limitations:
- Cold-start issue  
- Sparse matrices  

---

### **5.4 Hybrid Model (Sentifusion)**

Final score:

```
Hybrid Score = (Content-Based Score + Collaborative Score) / 2
```

Advantages:
- Reduces cold-start  
- Balances relevance + diversity  
- Produces more stable recommendations  

---

## 6. Workflow

1. Data Cleaning & Integration  
2. EDA & Visualization  
3. Feature Engineering  
4. Natural Language Processing  
5. Content-Based Model  
6. Collaborative Filtering  
7. Hybrid Recommender  
8. Flask Web Application  

---

## 7. Data Dictionary

| Feature | File | Type | Description |
|--------|------|------|-------------|
| movie_id | content.csv | int | Unique MovieLens movie ID |
| title | content.csv | object | Movie title |
| overview | content.csv | object | Plot summary |
| tagline | content.csv | object | Movie tagline |
| keywords | content.csv | object | Plot keywords |
| director | content.csv | object | Director name |
| cast | content.csv | object | Top 4 cast |
| sentiment_score | content.csv | float | Polarity score |
| user_id | ratings_title.csv | int | MovieLens user ID |
| rating | ratings_title.csv | float | Rating (0.5–5) |

---

## 8. Conclusion

Sentifusion integrates:

- **Content-Based Filtering** for metadata similarity  
- **Collaborative Filtering** for user preference learning  
- **Hybrid Ensemble** for best overall performance  

This results in:
- Higher accuracy  
- Better diversity  
- Improved personalization  

Future work:
- Matrix factorization (SVD / SVD++)  
- Real-world A/B testing  
- Neural recommendation models  

---

## 9. Technologies Used

**Languages**
- Python  
- HTML, CSS, JavaScript  

**ML & NLP**
- scikit-learn  
- pandas, numpy  
- TextBlob / VADER  
- TF-IDF Vectorizer  
- Cosine Similarity  

**Visualization**
- matplotlib  
- seaborn  

**Web App**
- Streamlit  

---

## 10. Project Structure

```
Hybrid-Movie-Recommender/
│── code/
│── recommender_app/
│── images/
│── data/  (ignored due to large size)
│── README.md
│── requirements.txt
```

---

