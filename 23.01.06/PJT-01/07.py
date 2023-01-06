import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성 
movie_genres = []
for id in movie['genre_ids']:
    for genre in genres_list:
        if id == genre["id"]:
            movie_genres.append(genre["name"])
print(movie_genres)