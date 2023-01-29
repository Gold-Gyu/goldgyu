import requests

# https://developers.themoviedb.org/3/movies/get-popular-movies
def popular_count():
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=bfbb47f47b0229def79825a170a5682b'
    # 여기에 코드를 작성합니다.  
    response = requests.get(url).json()
    a = response.get("results")
    cnt = 0
    for b in a:
        cnt += 1

    return cnt

    # for i in response_results:
        
    #         count += 1
    # print(count)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
