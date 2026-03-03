import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import clean_text

df = pd.read_csv("data/imdb_2024_movies.csv")
df["Cleaned_Storyline"] = df["Storyline"].apply(clean_text)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["Cleaned_Storyline"])

def recommend_movies(user_input, top_n=5):
    cleaned_input = clean_text(user_input)
    input_vector = vectorizer.transform([cleaned_input])

    similarity_scores = cosine_similarity(input_vector, tfidf_matrix)
    similarity_scores = similarity_scores.flatten()

    top_indices = similarity_scores.argsort()[-top_n:][::-1]

    recommendations = df.iloc[top_indices][["Movie Name", "Storyline"]]
    return recommendations