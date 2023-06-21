import spacy

nlp = spacy.load('en_core_web_md')

def find_similar_movie(description):
    with open('movies.txt', 'r') as file:
        movies = file.readlines()

    max_similarity = 0
    most_similar_movie = ''

    description_doc = nlp(description.lower())

    for movie in movies:
        movie_title, movie_description = movie.split(':')
        movie_doc = nlp(movie_description.lower().strip())

        similarity = description_doc.similarity(movie_doc)

        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_movie = movie_title.strip()

    return most_similar_movie

description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace."
similar_movie = find_similar_movie(description)
print(similar_movie)