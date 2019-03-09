from get_token import *


@ddt
class MyTestCase(unittest.TestCase):
    """书本列表"""

    def setUp(self):
        self.url = url + "/home/book-list"

    @data(('moduleId', '2'), ('moduleId', '3'), ('moduleId', '4'), ('moduleId', '5'), ('moduleId', '6'))
    @unpack
    def test_1(self, k1, v1):
        datas['page'] = 1
        datas['pageSize'] = 9
        datas[k1] = v1
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
