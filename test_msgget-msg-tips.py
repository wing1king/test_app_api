#coding:utf-8
import unittest, time, requests
from get_token import *
from ddt import *


@ddt
class MyTestCase(unittest.TestCase):
    """获取我的消息是否有未读消息"""

    def setUp(self):
        self.url = url + "/msg/get-msg-tips"

    @data(('type', 'all'),
          ('type', 'sys'),
          ('type', 'user'))
    @unpack
    def test_1(self, k1, v1):
        datas[k1] = v1
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
