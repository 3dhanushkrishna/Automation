import unittest
def checkevenoroddno(x):
    if x%2==0:
        return "even"
    else:
        return "odd"
class MyevenorOddApp(unittest.TestCase):
    def test_case_even_or_odd(self):
        result=checkevenoroddno(2)
        self.assertEqual("even",result)
    def test_case_even_or_odd1(self):
        result=checkevenoroddno(9)
        self.assertEqual("odd",result)
if __name__=="__main__":
    unittest.main()