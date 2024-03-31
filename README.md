# 🎬 Netflix Content Recommender System

## Description

This project aims to design an interactive recommendation system for Netflix content, encompassing both movies and TV shows. The project began with meticulous data cleaning and preprocessing to handle missing values across various columns and engineer date-related features. During the exploratory data analysis phase, content types and ratings were visualized to gain insights into the diversity of available content. A key step in feature engineering was the creation of the 'content' feature, aggregating several textual attributes to represent each content item uniquely.

The core of the recommendation system involves transforming this 'content' feature into a TF-IDF (Term Frequency-Inverse Document Frequency) matrix. Utilizing this matrix, a cosine similarity matrix was computed to capture the likeness between content items, facilitating personalized recommendations based on user preferences or viewing history.

To enhance user engagement and accessibility, the project leveraged Streamlit to develop an interactive web application. This addition allows users to easily select movies or TV shows from a dropdown menu and receive tailored content recommendations, significantly improving the user experience.


## Skills

- Data cleaning and pre-processing
- Exploratory Data Analysis (EDA)
- Data visualization: bar chart
- Feature engineering
- Content-based recommendation system
- Natural Language Processing (NLP) with TF-IDF Transformation
- Cosine Similarity Calculation
- Interactive Web Application Development with Streamlit

## Tools

- **`Python`** (**`Pandas`**, **`Matplotlib`**, **`Scikit-learn`, `Streamlit`**)

## Results

- Developed a content-based recommendation system with an interactive web interface, capable of suggesting similar movies or TV shows based on user selection.
- Uncovered insights into the nature of content available on Netflix through data visualization.
- Successfully transformed textual content attributes into a format suitable for similarity computations, paving the way for personalized content recommendations.
- Enhanced the accessibility and usability of the recommendation system through the integration of Streamlit, providing a seamless experience for users to interact with the model.
