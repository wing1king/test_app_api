from get_token import *


@ddt
class MyTestCase(unittest.TestCase):
    """编辑个人信息"""
    def setUp(self):
        self.url = url + "/user/info-edit"

    @data(('avatar', 'http://abc-1253117418.cos.ap-guangzhou.myqcloud.com/ac007e80bf5d092c236d32286bba8dd553c6b322.png'),
          ('bgImg', 'http://abc-1253117418.cos.ap-guangzhou.myqcloud.com/ac007e80bf5d092c236d32286bba8dd553c6b322.png'),
          ('nickName', '二次元'),
          ('desc', '迎难而上'),
          ('gender', '2'),
          ('birthday', '1993—12—12'),
          ('location', '南山区'))
    @unpack
    def test_1(self, k1, v1):
        """编辑昵称"""
        datas[k1] = v1
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" or u"南山区" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
