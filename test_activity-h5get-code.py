from get_token import *


class MyTestCase(unittest.TestCase):
    """ 获取验证码"""

    def setUp(self):
        self.url = url + "/activity-h5/get-code"

    def test_1(self):
        datas['mobile'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
