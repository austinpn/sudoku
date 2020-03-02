import requests
from json import loads
def fetchBoard():
    parsedBoard = loads(requests.get("https://sugoku.herokuapp.com/board?difficulty=hard").text)['board']
    return(parsedBoard)

