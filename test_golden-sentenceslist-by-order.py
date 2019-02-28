import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """根据id获取金句"""

    def setUp(self):
        self.url = url + "/golden-sentences/list-by-order"

    def test_1(self):
        datas['order'] = ''
        datas['direction'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
