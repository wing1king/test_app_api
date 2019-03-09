#coding:utf-8
import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """重读章节"""

    def setUp(self):
        self.url = url + "/play/chapter-restart"

    def test_1(self):
        datas['gameId'] = get_gameId()
        datas['chapterId'] = get_chapterId()
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
