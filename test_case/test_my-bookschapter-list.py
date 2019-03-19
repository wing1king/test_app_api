from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """我的作品--章节列表"""

    def setUp(self):
        self.url = url + "/my-books/chapter-list"

    def test_1(self):
        datas['bookId'] = '123124'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
