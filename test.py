import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)


user=int(input("What year:"))
for i in range(100000000):
    print(data[i]["title"])
    if data[i]["year"] >= user:
        print(data[i]["year"])



