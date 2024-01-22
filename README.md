# 🎬 Netflix Content Recommender System

## Description

The project aimed to design a recommendation system for Netflix content, be it movies or TV shows. Starting with data cleaning and preprocessing, missing values in various columns were handled, and date-related features were engineered. In the exploratory data analysis phase, the distribution of content types and ratings was visualized, providing insights into the nature of available content. Feature engineering led to the creation of the 'content' feature, a combination of several textual attributes. The crux of the recommendation system involved transforming this 'content' feature into a matrix of TF-IDF (Term Frequency-Inverse Document Frequency) features. Using the TF-IDF matrix, a cosine similarity matrix was computed, which served as the basis for recommending similar content. The cosine similarity matrix captures the similarity between content items, thus enabling personalized recommendations for users based on their viewing history or specific content preferences.

## Skills

- Data cleaning and pre-processing
- Exploratory Data Analysis (EDA)
- Data visualization: bar chart
- Feature engineering
- Content-based recommendation system
- TF-IDF transformation (NLP)
- Cosine similarity calculation

## Tools

- **`Python`** (**`Pandas`**, **`Matplotlib`**, **`Scikit-learn`**)

## Results

- Designed a content-based recommendation system capable of suggesting similar movies or TV shows.
- Uncovered insights into the nature of content available on Netflix through data visualization.
- Successfully transformed textual content attributes into a format suitable for similarity computations, paving the way for personalized content recommendations.
