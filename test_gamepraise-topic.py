#coding:utf-8
import unittest, time, requests
from get_token import *
from ddt import *


@ddt
class MyTestCase(unittest.TestCase):
    """话题点赞"""

    def setUp(self):
        self.url = url + "/game/praise-topic"

    @data(('type', 1),
          ('type', 2))  # 动作类型：1，点赞，2：取消点赞
    @unpack
    def test_1(self, k1, v1):
        """点赞"""
        datas['gameId'] = get_gameId()
        datas['topicId'] = get_topicId()
        datas[k1] = v1
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
