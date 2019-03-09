from get_token import *


class MyTestCase(unittest.TestCase):
    """签到"""

    def setUp(self):
        self.url = url + "/user/sign"

    def test_1(self):
        datas['id'] = 'sign_' + str(get_time())
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
