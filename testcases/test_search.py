# 被测类
import unittest


class Search:
    def search_fun(self):
        print("search")
        return True


class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    def test_search1(self):
        print("testsearch1")
        assert True == self.search.search_fun()

    def test_search2(self):
        print("testsearch2")
        assert True == self.search.search_fun()

    def test_search3(self):
        print("testsearch3")
        assert True == self.search.search_fun()

    def test_equal(self):
        print("断言相当")
        self.assertEqual(1, 1, "判断1==2")

    def test_notequal(self):
        print("测试不想当")
        self.assertNotEqual(1, 2, "判断1不等于2")
        self.assertTrue(1 == 1, "verify")


if __name__ == '__main__':

    # 执行当前文件所有的unittest测试用例
    # unittest.main()
    # 执行指定的额测试用例
    # 创建一个测试套件，批量执行测试方法
    # suite = unittest.TestSuite()
    # suite.addTest(TestSearch("test_search1"))
    # suite.addTest(TestSearch("test_search3"))
    # unittest.TextTestRunner.run(suite)

    # 执行某个测试类，讲测试类添加到测试套件里面，批量执行测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)

