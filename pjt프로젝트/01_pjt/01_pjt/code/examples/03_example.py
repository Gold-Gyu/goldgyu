# open 및 json 모듈 사용예시

import json


movie = open('C:/Users/SSAFY/Desktop/ssafy_gitlab/goldgyu/10_프로젝트/01_pjt/code/data/movie.json', encoding='utf-8')
movie_detail = json.load(movie)

print(movie_detail)
