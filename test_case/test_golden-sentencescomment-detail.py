from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """ 评论详情"""

    def setUp(self):
        self.url = url + "/golden-sentences/comment-detail"

    def test_1(self):
        datas['gsId'] = get_gsId()
        datas['topicId'] = get_jjtopicID()
        datas['page'] = 1
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
