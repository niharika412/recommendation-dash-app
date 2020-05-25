import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_data(x):
	return str.lower(x.replace(" ", ""))

def create_soup(x):
	return x['original_title']+ ' ' + x['authors'] + ' ' + x['average_rating']
	
def get_recommendations_new(title):
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(fbooks['soup'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    title=title.replace(' ','').lower()
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:15]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return list(books['original_title'].iloc[movie_indices])
	
books=pd.read_csv(r'books.csv',error_bad_lines = False)
books=books.dropna()

features=['original_title','authors','average_rating']
fbooks=books[features]
fbooks = fbooks.astype(str)
#print(list(fbooks['original_title']))
for feature in features:
    fbooks[feature] = fbooks[feature].apply(clean_data)
    
#fbooks.head(2)

fbooks['soup'] = fbooks.apply(create_soup, axis=1)


fbooks=fbooks.reset_index()
indices = pd.Series(fbooks.index, index=fbooks['original_title'])




