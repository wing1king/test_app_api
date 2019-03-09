from get_token import *


class MyTestCase(unittest.TestCase):
    """话题点赞"""

    def setUp(self):
        self.url = url + "/game/praise-topic"

    def test_1(self):
        """点赞"""
        datas['gameId'] = get_gameId()
        datas['topicId'] = get_topicId()
        datas['type'] = 1
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def test_2(self):
        """取消点赞"""
        datas['gameId'] = get_gameId()
        datas['topicId'] = get_topicId()
        datas['type'] = 2
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
