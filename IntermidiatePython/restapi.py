import requests

def checkSatusCode(url):
    response = requests.get(url)
    return response
 


print(checkSatusCode("https://jsonplaceholder.typicode.com/posts/1"))