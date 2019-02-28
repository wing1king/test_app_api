import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """金句话题详情"""

    def setUp(self):
        self.url = url + "/golden-sentences/topic-detail"

    def test_1(self):
        datas['gsId'] = get_gsId()
        datas['topicId'] = get_jjtopicID()
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
