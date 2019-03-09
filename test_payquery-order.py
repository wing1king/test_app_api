from get_token import *


class MyTestCase(unittest.TestCase):
    """查询订单状态"""

    def setUp(self):
        self.url = url + "/pay/query-order"

    def test_1(self):
        datas['order_id'] = '153664688432516239'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
