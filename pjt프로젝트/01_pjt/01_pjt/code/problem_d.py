import json


def max_revenue(movies):

    id_ = []
    result = []

    for movie in movies:
        # movies.json에서 딕셔너리 단위로 모두 가져온 것이 = movie
        id_.append(movie.get('id'))
        # movie안에서 id 키에 연결된 value 값들을 id_에 추가함
    
    for id in id_:
        
        movie_json = open(f'data/movies/{id}.json', encoding='utf-8')
        movie_list = json.load(movie_json)
        
        # json 파일 끌어오는 코드

        result.append(movie_list.get('revenue'))
        # ~.json 파일들 중에서 'revenue' key에 해당하는 value들을 result 리스트에 모두 추가하기
        result_max = max(result)
        # result_max는 result안에서 가장 큰 값
    
    for id in id_:
        movie_json = open(f'data/movies/{id}.json', encoding='utf-8')
        movie_list = json.load(movie_json)

        if movie_list.get('revenue') ==  result_max:
            return movie_list.get('title')
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('/Users/goldgyu/Desktop/Algorithm/goldgyu/10_프로젝트/01_pjt/code/data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
