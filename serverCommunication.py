import requests
import json


def login():
    url = 'http://aibg2022.com:8081/user/login'
    myjson = {'username': 'Deep_bAlt1', 'password': '#rS@T!$&Sz'}

    response = requests.post(url, json=myjson)

    data = json.loads(response.text)

    print(data)
    return data['token']


def join_game(token):
    url = 'http://aibg2022.com:8081/game/joinGame'
    response = requests.get(url, headers={"Authorization": f"Bearer {token}"})

    data = json.loads(response.text)

    return data


def game_do_action(token, action, x, y):
    url = 'http://aibg2022.com:8081/game/doAction'

    action_string = f"{action},{x},{y}"
    myjson = {'action': action_string}

    response = requests.post(url, headers={"Authorization": f"Bearer {token}"}, json=myjson)

    data = json.loads(response.text)

    print(data)


def game_train(token,mapName, playerIdx, time):
    url = 'http://aibg2022.com:8081/game/train'

    myjson = {'mapName': mapName, 'playerIdx': playerIdx, 'time': time}

    response = requests.post(url, headers={"Authorization": f"Bearer {token}"}, json=myjson)

    print(response.text)
    return response.text


def game_action_train(token, action, x, y):
    url = 'http://aibg2022.com:8081/game/actionTrain'

    action_string = f"{action},{x},{y}"
    myjson = {'action': action_string}

    response = requests.post(url, headers={"Authorization": f"Bearer {token}"}, json=myjson)

    #data = json.loads(response.text)

    print(response.text)
    return response.text

