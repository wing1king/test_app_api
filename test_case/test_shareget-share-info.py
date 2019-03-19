from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """获取分享信息"""

    def setUp(self):
        self.url = url + "/share/get-share-info"

    def test_1(self):
        datas['gameId'] = get_gameId()
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
