import json
from pprint import pprint


def movie_info(movie, genres):
    movie_dict ={}

    movie_dict["id"] = movie["id"]
    movie_dict["title"] = movie["title"]
    movie_dict["poster_path"] = movie["poster_path"]
    movie_dict["vote_average"] = movie["vote_average"]
    movie_dict["overview"] = movie["overview"]

    genre_ids = movie["genre_ids"]
    movie_dict["genre_names"] = []

    # print(genres)

    for id in genre_ids:
        for genre in genres:
            # if genre.get("id"):
            if id == genre["id"]:
                # id를 찾았으니 추가해주면 된다.
                movie_dict["genre_names"].append(genre["name"])

    return movie_dict
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
