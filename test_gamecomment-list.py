from get_token import *


class MyTestCase(unittest.TestCase):
    """游戏评论列表"""

    def setUp(self):
        self.url = url + "/game/comment-list"

    def test_1(self):
        """获取精评列表"""
        datas['gameId'] = get_gameId()
        datas['type'] = '1'
        datas['page'] = '1'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def test_2(self):
        """获取所有评论列表"""
        datas['gameId'] = get_gameId()
        datas['type'] = '2'
        datas['page'] = '1'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
