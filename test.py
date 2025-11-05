import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)



for i in range(100000000):
    print(data[i]["title"])
    print(data[i]["year"])

movies = [
    {"title": "Inception", "year": 2010, "genre": "Sci-Fi"},
    {"title": "The Dark Knight", "year": 2008, "genre": "Action"},
    {"title": "Interstellar", "year": 2014, "genre": "Sci-Fi"},
    {"title": "The Lion King", "year": 1994, "genre": "Animation"},
    {"title": "Avengers: Endgame", "year": 2019, "genre": "Action"}
]
for movie in movies:
    print(movie["title"])

year = int(input("Enter a year: "))

for movie in movies:
    if movie["year"] > year:
        print(movie["title"], movie["year"])



start_year = int(input("Enter the starting year: "))
end_year = int(input("Enter the ending year: "))

for movie in movies:
    if start_year < movie["year"] < end_year:
        print(movie["title"], movie["year"])



year = int(input("Enter the year: "))

for movie in movies:
    if movie["year"] == year:
        print(movie["title"], movie["year"])



def search_movie(title):
    results = []
    for movie in movies:
        if title.lower() in movie["title"].lower():
            results.append(movie)
    return results

# Example Use:
name = input("Enter movie title to search: ")
found = search_movie(name)
print(found)


def search_by_genre(genre):
    results = []
    for movie in movies:
        if movie["genre"].lower() == genre.lower():
            results.append(movie)
    return results

# Example Use:
g = input("Enter a genre: ")
found = search_by_genre(g)
print(found)



