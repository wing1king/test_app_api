from get_token import *


class MyTestCase(unittest.TestCase):
    """获取用户钱包"""

    def setUp(self):
        self.url = url + "/user/get-wallet"

    def test_1(self):
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"VCDIA" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
