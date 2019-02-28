#coding:utf-8
import requests
import datetime

# 开发环境
# url = "http://192.168.143.21:8055/v1"
# 测试环境
url = "http://10.72.12.43:8055/v1"


def get_token():
    data = {
            'openid': '164b4571e4542ca8f2cc19776f7fd2f211111',
            'sessionid': 'a9d384dd8ca7a22ec38505ddaf03eb6605b6a62661',
            'userid': 2147483641,
            'password': 'sddd',
            'login_type': 'ledou',
            'from_pf': 'ledou',
            'productId': 'sddd1',
            'debug': 'test',
            'from': 2,
            'os': 1,
            'app_id': 123,
            'app_ver': 1.0,
            'engine_ver': 1.0,
            'time': 1,
            }
    res = requests.post(url=url + '/oauth/login-by-openid', data=data)
    return res.json()['data']['access_token']


datas = {'access_token': get_token(),
         'app_id': 123,
         'app_ver': '1.0.1',
         'engine_ver': 1.0,
         'from': 2,
         'os': 1,
         'debug': 'test',
         'time': '1',
         }


def get_userid():
    """获取评论列表"""
    datas['gameId'] = 1534162849059  # 相见言欢
    datas['page'] = 2
    datas['type'] = 1
    res = requests.post(url=url + "/game/comment-list", data=datas)
    return res.json()['data'][0]['userId']


def get_gameId():
    res = requests.post(url=url + "/home/index", data=datas)
    return res.json()["data"][1]["gameId"]


def get_topicId():
    """获取评论列表"""
    datas['gameId'] = get_gameId()
    datas['page'] = 1
    datas['type'] = 2
    res = requests.post(url=url + "/game/comment-list", data=datas)
    return res.json()["data"][1]["topicId"]


def get_roleId():
    datas['gameId'] = get_gameId()
    datas['page'] = 1
    datas['type'] = 2
    res = requests.post(url=url + "/game/detail", data=datas)
    return res.json()["data"]['gameData']['mainRoles'][0]['roleId']


def get_gsId():
    res = requests.post(url=url + "/golden-sentences/list", data=datas)
    return res.json()["data"][0]['id']


def get_jjtopicID():
    datas['gsId'] = get_gsId()
    datas['page'] = 1
    datas['type'] = 2
    res = requests.post(url=url + "/golden-sentences/comment-list", data=datas)
    return res.json()['data'][0]['topicId']


def get_jjuserid():
    datas['gsId'] = get_gsId()
    datas['page'] = 1
    datas['type'] = 2
    res = requests.post(url=url + "/golden-sentences/comment-list", data=datas)
    return res.json()['data'][0]['userId']


def get_search():
    datas['page'] = 1
    datas['pageSize'] = 10
    res = requests.post(url=url + "/home/hot-search", data=datas)
    return res.json()['data'][0]['name']


def get_chapterId():
    datas['gameId'] = get_gameId()
    res = requests.post(url=url + "/game/chapters", data=datas)
    return res.json()['data'][0]['id']


def get_time():
    today = datetime.date.today()
    thistime = today.isoweekday()
    return thistime


def get_bug_id():
    datas['page'] = 1
    datas['pageSize'] = 10
    res = requests.post(url=url + "/customer/question-list", data=datas)
    return res.json()['data'][0]['bug_id']











