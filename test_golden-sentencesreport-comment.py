from get_token import *


class MyTestCase(unittest.TestCase):
    """ 举报评论、话题"""

    def setUp(self):
        self.url = url + "/golden-sentences/report-comment"

    def test_1(self):
        datas['reportUserId'] = get_jjuserid()
        datas['gsId'] = get_gsId()
        datas['topicId'] = get_jjtopicID()
        datas['commentId'] = ''
        datas['reasonContent'] = '其他'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
