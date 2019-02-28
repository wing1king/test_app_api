#coding:utf-8
import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """游戏详情"""

    def setUp(self):
        self.url = url + "/game/detail"

    def test_1(self):
        datas['gameId'] = get_gameId()
        data = datas
        res = requests.post(url=self.url, data=data)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
