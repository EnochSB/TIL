import requests
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('api_key')


def credits(title):
    base_url = 'https://api.themoviedb.org/3'
    search = '/search/movie'
    s_params = {
      'api_key' : api_key, 
      'language' : 'ko-KR',
      'region' : 'KR',
      'query' : f'{title}'
    }
    c_params = {
      'api_key' : api_key
    }

    res = requests.get(base_url+search, params=s_params).json()
    if res['results'] == []:
        return None

    movie_id = res['results'][0]['id']
    movie_credits = f'/movie/{movie_id}/credits'
    res_cre = requests.get(base_url+movie_credits, params=c_params).json()
    cre_dict = {}
    cst_list = []
    crw_list = []
    for i in range(len(res_cre['cast'])):
        cst_list.append(res_cre['cast'][i]['name'])
        
    for i in range(len(res_cre['crew'])):
        crw_list.append(res_cre['crew'][i]['name'])
    
    cre_dict['cast'] = cst_list
    cre_dict['crew'] = crw_list

    return cre_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
