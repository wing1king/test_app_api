from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """评论话题和回复评论"""

    def setUp(self):
        self.url = url + "/game/comment-topic"

    def test_1(self):
        datas['topicId'] = get_topicId()
        datas['gameId'] = get_gameId()
        datas['content'] = "看着挺不错的"
        datas['replyToTopicUserId'] = get_userid()
        datas['commentId'] = ''
        datas['replyToCommentUserId'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
