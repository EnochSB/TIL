import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('api_key')


def search_movie(title):
    base_url = 'https://api.themoviedb.org/3'
    search = '/search/movie'
    my_params = {
      'api_key' : api_key, 
      'language' : 'ko-KR',
      'region' : 'KR',
      'query' : f'{title}'
    }

    res = requests.get(base_url+search, params=my_params).json()
    if res['results'] == []:
        return None

    return res['results'][0]['id']


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None
