import re
import numpy as np
import spacy

def recommend_movie(input_desc, movie_file):
    # Load movie descriptions from txt file
    with open(movie_file, 'r') as f:
        movie_data = f.readlines()

    # Preprocess movie descriptions
    nlp = spacy.load("en_core_web_md")
    movie_descriptions = []
    movie_titles = []
    for movie in movie_data:
        title, desc = re.findall(r"Movie (\w) :(.*)", movie)[0]
        movie_titles.append(title)
        desc = desc.lower()
        desc = re.sub(r'[^\w\s]', '', desc)
        doc = nlp(desc)
        movie_descriptions.append(doc)

    # Calculate similarity between input and each movie
    input_desc = input_desc.lower()
    input_desc = re.sub(r'[^\w\s]', '', input_desc)
    input_doc = nlp(input_desc)
    sim_scores = []
    for doc in movie_descriptions:
        sim_scores.append(input_doc.similarity(doc))

    # Get index of highest similarity score and return corresponding movie title
    max_idx = np.argmax(sim_scores)
    recommended_movie = f"Movie {movie_titles[max_idx]}"
    return f"Next recommended movie: {recommended_movie} - {movie_data[max_idx]}"


input_desc = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
movie_file = "movies.txt"
print(recommend_movie(input_desc, movie_file))


# Ref: import re - https://www.w3schools.com/python/python_regex.asp
# and https://www.geeksforgeeks.org/python-regex/
# Ref: import numpy as np - https://codesource.io/how-to-import-numpy-as-np-and-use-it-in-python/

