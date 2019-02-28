#coding:utf-8
import unittest, time, requests
from get_token import *


class MyTestCase(unittest.TestCase):
    """保存章节状态"""

    def setUp(self):
        self.url = url + "/play/save-chapter-states"

    def test_1(self):
        datas['gameId'] = 1533895574615
        datas['chapterId'] = 1534402457381
        datas['state'] = '{"type":"chapter-save-state","savedEntityId":"1534402457381","chapterNumber":1,' \
                         '"currentState":"Playing","episodeId":"5b5185b575268acfa8255d65",' \
                         '"episodeSaveState":{"type":"episode-save-state","savedEntityId":"5b5185b575268acfa8255d65",' \
                         '"currentNodeId":"5b57129875268a7cb9256e55",' \
                         '"currentComponentSaveStates":[{"type":"graphic-novel-component-save-state",' \
                         '"savedEntityId":"75c1b412-3619-4be5-8149-e4eac834631c","currentMessageId":"3scg0"}],' \
                         '"markers":[{"type":"asset","id":"5b576a7175268ab035257777",' \
                         '"value":"5b576a2675268a4441257774","title":"ib - outfit"},' \
                         '{"type":"asset","id":"5b576b3275268a4e80257781","value":"5b576c5b75268a1fb425778b",' \
                         '"title":"kazuto-outfit"},{"type":"asset","id":"5b576fb575268a6b0c2577a4",' \
                         '"value":"5b576fdf75268a3e752577a6","title":"makino-outfit"},' \
                         '{"type":"asset","id":"5b577bb175268a6868257a16","value":"5b577b2075268a80bd257a13",' \
                         '"title":"mc-outfit"},{"type":"asset","id":"5b577e2275268a6300257a3f",' \
                         '"value":"5b577e4b75268ae460257a40","title":"mifuyu-outfit"},' \
                         '{"type":"asset","id":"5b57884175268a81c8257ad5","value":"5b57886075268a66e1257ad6",' \
                         '"title":"saito-outfit"},{"type":"asset","id":"5b5788ea75268a76c9257adb",' \
                         '"value":"5b57890875268a2a3b257adc","title":"sakaki-outfit"},' \
                         '{"type":"asset","id":"5b578c7a75268ac3af257ae2","value":"5b578c9d75268a30e2257ae3",' \
                         '"title":"saya-outfit"},{"type":"achievement","id":"5b62cc8cf1ef61903e7b7ad8",' \
                         '"value":"false","title":"ending 1","titleContentId":"5b62cc8cf1ef61903e7b7ad8:title",' \
                         '"descriptionContentId":"5b62cc8cf1ef61903e7b7ad8:description"},{"type":"achievement",' \
                         '"id":"5b62cc9bf1ef6119127b7ad9","value":"false","title":"ending 2",' \
                         '"titleContentId":"5b62cc9bf1ef6119127b7ad9:title",' \
                         '"descriptionContentId":"5b62cc9bf1ef6119127b7ad9:description"},' \
                         '{"type":"asset","id":"5b7a66b7c5d57a0164423cd6","value":"5b5689fe75268a20f62569e9",' \
                         '"title":"a和人 - face"},{"type":"asset","id":"5b7a66c3c5d57af74d423cd7",' \
                         '"value":"5b55e6fe75268a126c2569ce","title":"a凛 - face"},' \
                         '{"type":"asset","id":"5b55e7b175268ae17a2569d1","value":"5b57823e75268a59d8257a75",' \
                         '"title":"rin-outfit"}],"activeAssetSaveStates":[{"type":"graphic-novel-location-save-state",' \
                         '"savedEntityId":"5b51930775268a3faa2563f3","currentZoneId":"null"},' \
                         '{"type":"looping-audio-save-state","savedEntityId":"5b569b4775268a467d2569fd",' \
                         '"audioType":"music","pitch":1.0,"volume":1.0}]}}'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
