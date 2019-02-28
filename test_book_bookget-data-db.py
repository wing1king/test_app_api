import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """从数据库中获取保存的书数据"""

    def setUp(self):
        self.url = url + "/book/get-data-db"

    def test_1(self):
        datas['bookId'] = ''
        datas['cate'] = []
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
