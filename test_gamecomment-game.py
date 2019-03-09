from get_token import *
# @ddt


class MyTestCase(unittest.TestCase):
    """评论游戏"""

    def setUp(self):
        self.url = url + "/game/comment-game"

    # @data(('content', '1刷了，准备在看一遍'),
    #       ('content', '2刷了，准备在看一遍'),
    #       ('content', '3刷了，准备在看一遍'))
    # @unpack
    def test_1(self):
        datas['gameId'] = get_gameId()
        datas['content'] = "1刷了，准备在看一遍"
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
