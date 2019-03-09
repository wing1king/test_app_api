import unittest,time,requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """个人中心"""
    def setUp(self):
        self.url = url + "/user/info"

    def test_1(self):
        datas['userId'] = ''  # 2264982076
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
