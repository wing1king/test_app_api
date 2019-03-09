from get_token import *


class MyTestCase(unittest.TestCase):
    """根据类型获取配置"""

    def setUp(self):
        self.url = url + "/common/get-config"

    def test_1(self):
        datas['channel'] = 'iOS'
        datas['app_ver'] = '1.0.1'
        datas['type'] = 2
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
