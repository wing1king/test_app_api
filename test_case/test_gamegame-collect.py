from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """游戏收藏"""

    def setUp(self):
        self.url = url + "/game/game-collect"

    def test_1(self):
        """收藏作品"""
        datas['gameId'] = get_gameId()
        datas['type'] = 0
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def test_2(self):
        """取消收藏作品"""
        datas['gameId'] = get_gameId()
        datas['type'] = 1
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
