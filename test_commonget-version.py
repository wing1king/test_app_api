from get_token import *


class MyTestCase(unittest.TestCase):
    """检测版本更新"""

    def setUp(self):
        self.url = url + "/common/get-version"

    def test_1(self):
        """当前有新版本"""
        datas['channel'] = 'iOS'
        datas['app_ver'] = '1.0.1'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
