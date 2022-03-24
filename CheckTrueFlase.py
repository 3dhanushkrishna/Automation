import unittest
def check_divisible_by7(x):
    if x%7==0:
        return True
    else:
        return False
class Mycheck_divisible_by7(unittest.TestCase):
    def test_case_trueorfalse_1(self):
        result=check_divisible_by7(4)
        self.assertFalse(result)
    def test_case_trueorfalse_2(self):
        result=check_divisible_by7(14)
        self.assertTrue(result)
if __name__=="__main__":
    unittest.main()
