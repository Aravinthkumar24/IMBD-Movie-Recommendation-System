import streamlit as st
from recommender import recommend_movies

st.title("🎬 IMDB 2024 Movie Recommendation System")

user_input = st.text_area("Enter a Movie Storyline")

if st.button("Recommend Movies"):
    if user_input.strip() != "":
        results = recommend_movies(user_input)

        st.subheader("Top 5 Recommended Movies")
        for index, row in results.iterrows():
            st.write("###", row["Movie Name"])
            st.write(row["Storyline"])
            st.write("---")
    else:
        st.warning("Please enter a storyline.")