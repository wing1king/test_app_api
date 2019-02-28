import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """活动预约"""

    def setUp(self):
        self.url = url + "/activity-h5/book"

    def test_1(self):
        datas['key'] = ''
        datas['mobile'] = ''
        datas['code'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
