from get_token import *


class MyTestCase(unittest.TestCase):
    """增加游戏时长人气"""

    def setUp(self):
        self.url = url + "/play/play-data"

    def test_1(self):
        datas['gameId'] = get_gameId()
        datas['playTime'] = 0
        datas['clickNum'] = 1
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
