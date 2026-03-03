🎬 IMDB 2024 Movie Recommendation System Using Storylines
A Content-Based Movie Recommendation System built using Web Scraping, NLP, and Machine Learning.
📌 Project Overview
The IMDB 2024 Movie Recommendation System is a content-based recommender system that suggests movies based on storyline similarity.

The system:
Scrapes 2024 movie data from IMDb using Selenium
Cleans and preprocesses storylines using NLP
Converts text into numerical vectors using TF-IDF
Applies Cosine Similarity to compute similarity scores
Provides Top 5 movie recommendations
Deploys an interactive UI using Streamlit

🚀 Features

Automated Web Scraping
NLP-based Text Cleaning
TF-IDF Vectorization
Cosine Similarity Matching
Interactive Streamlit Web App
Real-time Recommendations

🛠️ Tech Stack
Language
Python
Libraries & Tools
Selenium
Pandas
NLTK
Scikit-learn
Streamlit
WebDriver Manager

📂 Project Structure
IMDB-Movie-Recommendation/
│
├── data/
│   └── imdb_2024_movies.csv
│
├── web_scraping.py
├── preprocess.py
├── recommender.py
├── app.py
├── README.md
🕸️ 1️⃣ Web Scraping (web_scraping.py)

The script uses Selenium to:

Open IMDb 2024 feature films page
Click "50 more" until all movies load

Extract:

Movie Name
Storyline
Store data into CSV file

Output File:
imdb_2024_movies.csv

Data Columns:
Movie Name
Storyline

🧹 2️⃣ Text Preprocessing (preprocess.py)

Uses NLP techniques to clean storyline text.

Steps Performed:
Convert text to lowercase
Remove special characters
Remove stopwords
Apply lemmatization

Function:
clean_text(text)

🤖 3️⃣ Recommendation Engine (recommender.py)

Steps:
Load dataset
Clean storylines
Apply TF-IDF Vectorization
Compute Cosine Similarity
Return Top 5 similar movies

Core Algorithm:
TF-IDF Vectorizer
Cosine Similarity

Function:
recommend_movies(user_input, top_n=5)

Returns:
Movie Name
Storyline

🌐 4️⃣ Streamlit Application (app.py)

Provides interactive user interface.

Features:

Text area for storyline input
Recommend button
Displays Top 5 similar movies
Clean and responsive UI

Run the App:
streamlit run app.py
⚙️ Installation Guide
Step 1: Clone Repository
git clone <your-repo-link>
cd IMDB-Movie-Recommendation
Step 2: Install Dependencies
pip install -r requirements.txt

If no requirements file:

pip install selenium pandas nltk scikit-learn streamlit webdriver-manager
Step 3: Run Web Scraper
python web_scraping.py
Step 4: Run Streamlit App
streamlit run app.py
📊 How It Works

User Input
↓
Text Cleaning (NLP)
↓
TF-IDF Vectorization
↓
Cosine Similarity Calculation
↓
Top 5 Recommended Movies

🎯 Example Use Case
Input:
A young wizard discovers magical powers and fights dark forces.
Output:
Top 5 movies with similar fantasy-based storylines.

💼 Business Use Cases
OTT Platforms
Streaming Services
Personalized Content Engines
Entertainment Analytics
Content Discovery Systems

📈 Future Improvements

Add movie posters
Deploy on Streamlit Cloud
Add filtering by genre
Improve similarity using advanced NLP (BERT)
Store data in database instead of CSV

🏁 Conclusion

This project demonstrates:
Web Scraping using Selenium
NLP preprocessing using NLTK
Machine Learning using TF-IDF & Cosine Similarity
Full-stack ML deployment using Streamlit
It is a complete end-to-end real-world Recommender System project suitable for portfolio and industry applications.
