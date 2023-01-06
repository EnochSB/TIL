import json
from pprint import pprint

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성
genre_names = []
key_list = ["id", "title", "vote_average", "overview", "genre_names"]
check_dict = {}
for id in movie["genre_ids"]:
    for genre in genres_list:
        if id == genre["id"]:
            genre_names.append(genre["name"])
for key in key_list:
    if key in movie:
        check_dict[key] = movie[key]
    else:
        check_dict[key] = genre_names
pprint(check_dict, sort_dicts=False)
