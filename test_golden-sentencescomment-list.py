import unittest, time, requests
from get_token import *
from ddt import *


@ddt
class MyTestCase(unittest.TestCase):
    """金句评论列表"""

    def setUp(self):
        self.url = url + "/golden-sentences/comment-list"

    @data(('type', 1),
          ('type', 2))  # 评论类型：1：精评，2：所有评论
    @unpack
    def test_1(self, k1, v1):
        datas['gsId'] = get_gsId()
        datas['page'] = 1
        datas[k1] = v1
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
