#coding:utf-8
import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """获取聊天的sig"""

    def setUp(self):
        self.url = url + "/chat/get-sig"

    def test_1(self):
        datas['userId'] = 1491806239
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
