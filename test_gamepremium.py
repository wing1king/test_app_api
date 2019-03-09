from get_token import *


class MyTestCase(unittest.TestCase):
    """Premium选项扣费"""

    def setUp(self):
        self.url = url + "/game/premium"

    def test_1(self):
        datas['gameId'] = get_gameId()
        datas['chapterId'] = ''
        datas['optionType'] = ''
        datas['optionId'] = ''
        datas['type'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
