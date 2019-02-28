#coding:utf-8
import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """保存游戏状态"""

    def setUp(self):
        self.url = url + "/play/save-game-states"

    def test_1(self):
        datas['gameId'] = get_gameId()
        datas['state'] = '{"type": "book-save-state-non-chapter",' \
                         ' "savedEntityId":"1536817660145",' \
                         '"timestamp":1542953873000,' \
                         '"currentChapterNumber":1,' \
                         '"isPinned":true,' \
                         '"purchasedPremiumOptions":[],' \
                         '"chapterCompletionCounts":{"1536817712210":8}}'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
