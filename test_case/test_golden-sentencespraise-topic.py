from tool.get_token import *


@ddt
class MyTestCase(unittest.TestCase):
    """话题点赞"""

    def setUp(self):
        self.url = url + "/golden-sentences/praise-topic"

    @data(('type', 1),
          ('type', 2))  # 动作类型：1，点赞，2：取消点赞
    @unpack
    def test_1(self, k1, v1):
        datas['gsId'] = get_gsId()
        datas['topicId'] = get_jjtopicID()
        datas[k1] = v1
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
