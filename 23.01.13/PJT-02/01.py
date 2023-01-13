import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('api_key')

def popular_count():
    base_url = 'https://api.themoviedb.org/3'
    popular = '/movie/popular'
    my_params = {
        'api_key' : api_key, 
        'language' : 'ko-KR',
        'region' : 'KR'
    }

    response = requests.get(base_url + popular , params=my_params).json()
    return len(response['results'])



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
