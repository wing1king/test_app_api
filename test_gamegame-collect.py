#coding:utf-8
import unittest, time, requests
from get_token import *
from ddt import *


@ddt
class MyTestCase(unittest.TestCase):
    """游戏收藏"""

    def setUp(self):
        self.url = url + "/game/game-collect"

    @data(('type', 0),
          ('type', 1))
    @unpack
    def test_1(self, k1, v2):
        """收藏/取消收藏作品"""
        datas['gameId'] = get_gameId()
        datas[k1] = v2
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
