import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """ 书数据保存"""

    def setUp(self):
        self.url = url + "/book/save-data"

    def test_1(self):
        datas['bookId'] = ''
        datas['file'] = ''
        datas['fileInfo'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
