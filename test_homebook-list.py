import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """书本列表"""

    def setUp(self):
        self.url = url + "/home/book-list"

    def test_1(self):
        datas['page'] = 1
        datas['pageSize'] = 1
        datas['moduleId'] = 4
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
