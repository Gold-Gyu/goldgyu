# import os
# import sys
# import urllib.request
# client_id = "gsPYK3zLs_MA55JuiCTk"
# client_secret = 
# encText = urllib.parse.quote("컴퓨터")
# url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText # JSON 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     print(response_body.decode('utf-8'))
# else:
#     print("Error Code:" + rescode)

#import
import urllib.request

#애플리케이션 클라이언트 id 및 secret
client_id = "gsPYK3zLs_MA55JuiCTk" 
client_secret = 

#도서검색 url
#디폴트(json) https://openapi.naver.com/v1/search/book?query=python&display=3&sort=count
#json 방식 https://openapi.naver.com/v1/search/book.json?query=python&display=3&sort=count
#xml 방식  https://openapi.naver.com/v1/search/book.xml?query=python&display=3&sort=count
url = "https://openapi.naver.com/v1/search/book.json"
option = "&display=3&sort=count"
query = "?query="+urllib.parse.quote(input("질의:"))
url_query = url + query + option

#Open API 검색 요청 개체 설정
request = urllib.request.Request(url_query)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

#검색 요청 및 처리
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode == 200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error code:"+rescode)