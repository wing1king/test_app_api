#coding:utf-8
import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """关注、取关用户"""

    def setUp(self):
        self.url = url + "/friend/follow"

    def test_1(self):
        """关注用户"""
        datas['followUserId'] = 1491806239
        datas['type'] = 1
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def test_2(self):
        """取消关注用户"""
        datas['followUserId'] = 1491806239
        datas['type'] = 2
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
