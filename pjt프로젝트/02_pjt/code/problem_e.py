import requests
from pprint import pprint


def credits(title):
    url = 'https://api.themoviedb.org/3/search/movie?api_key=bfbb47f47b0229def79825a170a5682b&query=' + title
    response = requests.get(url).json() #response는 딕셔너리

    search_movie = response.get('results') # serach_movie는 리스트

    # 첫 번째 데이터 중 id에 해당하는 값 가져오기
    if search_movie == []:
        return None
    else:
        movie_id = search_movie[0].get("id")
    
    # url2 가져오기

    url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=bfbb47f47b0229def79825a170a5682b&language=en-US'
    response2 = requests.get(url2).json()

    # cast 리스트

    movie_cast = response2.get('cast')

    
    cast_lst = []
    
    
    for i in movie_cast:
        
        castid = i.get('cast_id')
        department = i.get('known_for_department')
        
        if castid < 10:
            cast_lst.append(i.get('name'))
    
    # crew 리스트

    movie_crew = response2.get('crew')

    crew_lst = []
    answer_dic = {}

    
    for i in movie_crew:
        
        
        department = i.get('department')
        
        if department == 'Directing':
            crew_lst.append(i.get('name'))

    # 딕셔너리에 추가    
    answer_dic['cast'] = cast_lst
    answer_dic['directing'] = crew_lst

    return answer_dic
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
