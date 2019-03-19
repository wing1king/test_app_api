from tool.get_token import *


@ddt
class MyTestCase(unittest.TestCase):
    """角色点赞"""

    def setUp(self):
        self.url = url + "/game/role-praise"

    @data(('type', 0),
          ('type', 1))  # 0：点赞，1：取消点赞
    @unpack
    def test_1(self, k1, v2):
        """点赞"""
        datas['roleId'] = get_roleId()
        datas[k1] = v2
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
