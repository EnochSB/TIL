import json
from pprint import pprint

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
check_list = ["id", "title", "vote_average", "overview", "genre_ids"]
check_dict = {}
for i in check_list:
     if i in movie:
        check_dict[i] = movie[i]

pprint(check_dict, sort_dicts=False)