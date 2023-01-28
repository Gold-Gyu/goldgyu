import requests
from pprint import pprint


def recommendation(title):
    url = 'https://api.themoviedb.org/3/search/movie?api_key=bfbb47f47b0229def79825a170a5682b&query=' + title

    response = requests.get(url).json() #response는 딕셔너리

    search_movie = response.get('results') # serach_movie는 리스트

    # 첫 번째 데이터 중 id에 해당하는 값 가져오기
    # seach_movie 값이 없으면 none
    if search_movie == []:
        return None
    else:
        movie_id = search_movie[0].get("id")
    
    # url2 가져오기
    url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=bfbb47f47b0229def79825a170a5682b&language=en-US&page=1'
    response2 = requests.get(url2).json()
    
    
    response3 = response2.get('results')
    
    lst = []

    for i in response3:
        title_name = i.get('title')
        lst.append(title_name)
    return(lst)



if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
