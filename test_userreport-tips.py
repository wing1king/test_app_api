#coding:utf-8
import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """上报提示"""

    def setUp(self):
        self.url = url + "/user/report-tips"

    def test_1(self):
        datas['type'] = ''
        datas['friendUserId'] = ''
        datas['fansUserId'] = ''
        datas['id'] = ''
        datas['date'] = ''
        datas['reportId'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
