#coding:utf-8
import unittest, time, requests
from get_token import *
from ddt import *


class MyTestCase(unittest.TestCase):
    """游戏点赞"""

    def setUp(self):
        self.url = url + "/game/game-praise"

    def test_1(self):
        """点赞"""
        datas['gameId'] = get_gameId()
        datas['type'] = 0
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_2(self):
        """取消点赞"""
        datas['gameId'] = get_gameId()
        datas['type'] = 1
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
