#coding:utf-8
import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """我的粉丝"""

    def setUp(self):
        self.url = url + "/friend/fans-list"

    def test_1(self):
        """查看我的粉丝"""
        datas['page'] = 1
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
