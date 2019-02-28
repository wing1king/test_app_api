#coding:utf-8
import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """章节结束"""

    def setUp(self):
        self.url = url + "/play/chapter-finished"

    def test_1(self):
        datas['gameId'] = 1533895574615
        datas['chapterId'] = 1534402457381
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
