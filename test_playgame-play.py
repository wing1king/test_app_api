from get_token import *


class MyTestCase(unittest.TestCase):
    """游戏章节开始"""

    def setUp(self):
        self.url = url + "/play/game-play"

    def test_1(self):
        datas['gameId'] = get_gameId()
        datas['chapterId'] = get_chapterId()
        datas['type'] = ''
        datas['version'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
