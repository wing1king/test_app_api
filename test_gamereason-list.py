from get_token import *


class MyTestCase(unittest.TestCase):
    """获取举报原因列表（暂不用）"""

    def setUp(self):
        self.url = url + "/game/reason-list"

    def test_1(self):
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
