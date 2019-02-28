#coding:utf-8
import unittest, time
from get_token import *
from ddt import *


@ddt
class MyTestCase(unittest.TestCase):
    """举报评论、话题"""

    def setUp(self):
        self.url = url + "/game/report-comment"

    @data(('reasonContent', '垃圾广告营销'),
          ('reasonContent', '嘲讽/不友善内容'),
          ('reasonContent', '侮辱谩骂内容'),
          ('reasonContent', '淫秽色情内容'),
          ('reasonContent', '违反有害信息'),
          ('reasonContent', '其他'))
    @unpack
    def test_1(self, key, value):
        """举报原因：垃圾广告营销"""
        datas['reportUserId'] = get_userid()
        datas['gameId'] = get_gameId()
        datas['topicId'] = 3
        datas['commentId'] = ''
        datas[key] = value
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
