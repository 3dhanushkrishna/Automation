import unittest
def add(x,y):
    return x+y
class Myapp(unittest.TestCase):
    def test_case_add(self):
        a=10
        b=12
        c=add(a,b)
        self.assertEqual(a+b,c)
    def test_case_add1(self):
        a=10.5
        b=4.5
        c=add(a,b)
        self.assertEqual(c,a+b)
    def test_case_add2(self):
        a = -2
        b = -1
        c =add(a,b)
        self.assertEqual(c,a+b)
if __name__=="__main__":
    unittest.main()