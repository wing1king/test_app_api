from tool.get_token import *


@ddt
class MyTestCase(unittest.TestCase):
    """打赏游戏"""

    def setUp(self):
        self.url = url + "/game/reward"

    @data(('1534129524834', '2', '1'),
          ('1534129524834', '4', '2'),
          ('1534129524834', '6', '3'),
          ('1534129524834', '8', '4'),
          ('1534129524834', '10', '5'),
          ('1534129524834', '12', '6'))
    @unpack
    def test_1(self, v1, v2, v3):
        """打CALL"""
        datas['gameId'] = v1
        datas['VCDIA'] = v2
        datas['reward_id'] = v3
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
