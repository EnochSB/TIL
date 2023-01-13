import requests
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('api_key')


def recommendation(title):
    base_url = 'https://api.themoviedb.org/3'
    search = '/search/movie'
    my_params = {
      'api_key' : api_key, 
      'language' : 'ko-KR',
      'region' : 'KR',
      'query' : f'{title}'
    }
    rec_params = {
      'api_key' : api_key, 
      'language' : 'ko-KR',
      'region' : 'KR'
    }

    res = requests.get(base_url+search, params=my_params).json()
    if res['results'] == []:
        return None

    movie_id = res['results'][0]['id']
    recommend = f'/movie/{movie_id}/recommendations'
    res_rec = requests.get(base_url+recommend, params=rec_params).json()
    rec_list = [res_rec['results'][i]['title'] for i in range(len(res_rec['results']))]

    return rec_list



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
