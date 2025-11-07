import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

for movie in data:
    print(movie["title"])

year = int(input("Enter a year: "))

for movie in data:
    if movie["year"] > year:
        print(movie["title"], movie["year"])



start_year = int(input("Enter the starting year: "))
end_year = int(input("Enter the ending year: "))

for movie in data:
    if start_year < movie["year"] < end_year:
        print(movie["title"], movie["year"])

years = int(input("Enter the year: "))

for movie in data:
    if movie["year"] == years:
        print(movie["title"], movie["year"])


def search_movie(title):
    results = []
    for movie in data:
        if title in movie["title"]:
            results.append(movie)
    return results

name = input("Enter movie title: ")
found = search_movie(name)
print(found)



def genres(genre):
    for movie in data:
        if genre in movie["genres"]:
           print(movie["title"], movie["genres"])

genres("Action")

#for this function, I made it you don't need to worry about the capitalization when using the function for ex: genres(SCIFI), genres(action)
def genres(genre):
    genre = genre.lower()
    for movie in data:
        for g in movie["genres"]:
            if genre == g.lower():
                print(movie["title"], movie["genres"])
               

genres("action")













                                     


                                     
