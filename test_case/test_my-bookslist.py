from tool.get_token import *


@ddt
class MyTestCase(unittest.TestCase):
    """我的作品列表"""
    global test_info    # 定义全局变量
    test_info = []
    for i in range(1):  # 执行次数
        tese_data = (i, i + 1)
        test_info.append(tese_data)

    def setUp(self):
        self.url = url + "/my-books/list"

    @data(*test_info)
    def test_1(self,test_info):
        datas['page'] = '1'
        datas['pageSize'] = '1'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
