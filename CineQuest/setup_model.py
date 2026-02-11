import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def create_model():
    print("Loading datasets...")
    movies = pd.read_csv('tmdb_5000_movies.csv')
    credits = pd.read_csv('tmdb_5000_credits.csv')

    # Merge datasets
    movies = movies.merge(credits, on='title')
    
    # Keep relevant columns
    movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
    movies.dropna(inplace=True)

    # Helper function to extract text from JSON-like columns
    import ast
    def convert(obj):
        L = []
        for i in ast.literal_eval(obj):
            L.append(i['name'])
        return L

    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    
    # Simplified text processing for tags
    movies['tags'] = movies['overview'].apply(lambda x: x.split()) + movies['genres'] + movies['keywords']
    movies['tags'] = movies['tags'].apply(lambda x: " ".join(x))
    
    new_df = movies[['movie_id', 'title', 'tags']]
    new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

    print("Training model (creating similarity matrix)...")
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(new_df['tags']).toarray()
    
    similarity = cosine_similarity(vectors)

    # Save the files
    pickle.dump(new_df.to_dict(), open('movie_dict.pkl', 'wb'))
    pickle.dump(similarity, open('similarity.pkl', 'wb'))
    print("Model saved successfully!")

if __name__ == "__main__":
    create_model()