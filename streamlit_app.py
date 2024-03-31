import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load data and preprocess
@st.cache_data
def load_data():
    df = pd.read_csv("./netflix_titles.csv")
    df['director'].fillna('Unknown', inplace=True)
    df['cast'].fillna('Unknown', inplace=True)
    df['country'].fillna(df['country'].mode()[0], inplace=True)
    df['rating'].fillna(df['rating'].mode()[0], inplace=True)
    df['date_added'].fillna(df['date_added'].mode()[0], inplace=True)
    df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    df['month_added'] = df['date_added'].dt.month
    df['duration_min'] = df.loc[df['type'] == 'Movie', 'duration'].str.extract('(\d+)').astype(float)
    df['seasons'] = df.loc[df['type'] == 'TV Show', 'duration'].str.extract('(\d+)').astype(float)
    df[['duration_min', 'seasons']] = df[['duration_min', 'seasons']].fillna(0)
    df.drop('duration', axis=1, inplace=True)
    df['content'] = df['title'] + ' ' + df['director'] + ' ' + df['cast'] + ' ' + df['listed_in'] + ' ' + df['description']
    return df

df = load_data()

# Setup TF-IDF and calculate cosine similarity
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['content'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Recommendation function
def get_recommendations(title, cosine_sim=cosine_sim):
    if title not in df['title'].values:
        return "The title is not in the database. Please try another one."
    else:
        idx = df[df['title'] == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]
        
        recommendations = df.iloc[movie_indices][['title', 'release_year', 'type', 'director', 'listed_in']]
        return recommendations

# Streamlit UI setup
def main():
    st.image("./Vector__3_.svg", width=700)
    st.title("Movie/Show Recommendation System")

    movie_titles = df['title'].sort_values().unique()
    selected_movie = st.selectbox('Choose or type a movie from the list', movie_titles)

    if st.button('Get Recommendations'):
        recommendations = get_recommendations(selected_movie)
        if isinstance(recommendations, str):
            st.write(recommendations)
        else:
            st.write(f"Movies/Shows similar to {selected_movie}:")
            for rank, (index, row) in enumerate(recommendations.iterrows(), start=1):
                # Custom colors
                type_color = "#ffa6c4"
                director_color = "#b5ffa6"
                genre_color = "#a9e5ff"
                
                # Building the HTML string with inline styles for colors
                output_html = f"""
                **({rank}) {row['title']} ({row['release_year']})**  
                Type: <span style='color: {type_color};'>{row['type']}</span>  
                Director: <span style='color: {director_color};'>{row['director']}</span>  
                Genre: <span style='color: {genre_color};'>{row['listed_in']}</span>
                """
                
                st.markdown(output_html, unsafe_allow_html=True)
                st.write("---")

if __name__ == "__main__":
    main()
