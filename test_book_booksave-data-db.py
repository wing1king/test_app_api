import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """书数据保存到数据库"""

    def setUp(self):
        self.url = url + "/book/save-data-db"

    def test_1(self):
        datas['bookId'] = 1548763637327
        datas['cate'] = ''
        datas['data'] = {}
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
