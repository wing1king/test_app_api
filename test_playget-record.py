from get_token import *


class MyTestCase(unittest.TestCase):
    """获取用户游戏消费记录"""

    def setUp(self):
        self.url = url + "/play/get-record"

    def test_1(self):
        datas['gameId'] = get_gameId()
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_2(self):
        datas['gameId'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
