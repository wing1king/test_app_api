import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """评论金句"""

    def setUp(self):
        self.url = url + "/golden-sentences/comment-gs"

    def test_1(self):
        datas['gsId'] = get_gsId()
        datas['content'] = '喜欢❤'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
