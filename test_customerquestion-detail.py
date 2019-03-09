from get_token import *


class MyTestCase(unittest.TestCase):
    """问题详细"""

    def setUp(self):
        self.url = url + "/customer/question-detail"

    def test_1(self):
        datas['bug_id'] = get_bug_id()
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
