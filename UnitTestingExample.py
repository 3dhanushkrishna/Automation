import unittest
class myapp2(unittest.TestCase):
    def test_case3(self):
        self.assertEqual("hello","hello")

    def test_case4(self):
        self.assertNotEqual("hello","ho")

class myapp(unittest.TestCase):

    def test_case1(self):
        a=12
        b=4
        c=a+b
        self.assertEqual(16,c)
    def test_case2(self):
        pass
if __name__== "__main__":
    unittest.main()