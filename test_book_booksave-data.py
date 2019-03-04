import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """ 书数据保存"""

    def setUp(self):
        self.url = url + "/book/save-data"

    def test_1(self):
        datas['bookId'] = 1548763637327
        datas['file'] = 'jxb_save_data.json'
        datas['fileInfo'] = '{"url":"\/bookdata\/2147483641\/1548763637327\/jxb_save_data.json"}'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
