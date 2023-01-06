import json
from pprint import pprint

# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성
key_list = ["id", "title", "vote_average", "overview", "genre_ids"]
check_list = []
check_dict = {}
for movie in movies_list:
    for key in key_list:
        check_dict[key] = movie[key]
    check_list.append(check_dict)
    check_dict = {}
pprint(check_list, sort_dicts=False)
