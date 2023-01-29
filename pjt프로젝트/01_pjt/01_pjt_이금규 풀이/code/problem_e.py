import json


def dec_movies(movies):

    id_ = []

    last_list = []

    for movie in movies:
        # movie.json에서 딕셔너리 단위로 모두 가져온 것이 = movie
        id_.append(movie.get('id'))
        # movie안에서 id 키에 연결된 value 값들을 id.list에 추가함

    for id in id_:
        
        movie_json = open(f'data/movies/{id}.json', encoding='utf-8')
        movie_list = json.load(movie_json)
        
        # json 파일 끌어오는 코드

        release = movie_list.get('release_date')
        
        # ~.json 파일들 중에서 'release_date' key에 해당하는 value들을 result 리스트에 모두 추가하기
    # for id in id_list:
        
        # movie_json = open(f'data/movies/{id}.json', encoding='utf-8')
        # movie_list = json.load(movie_json)
        if release[5:7] == "12":
            last_list.append(movie_list.get('title'))
    return last_list
    # 굳이 리스트를 만들 필요가 없었다.
    
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
