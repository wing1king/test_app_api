from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """ 领取活动礼包"""

    def setUp(self):
        self.url = url + "/activity/get-gift"

    def test_1(self):
        datas['key'] = 'jxb_book '
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
