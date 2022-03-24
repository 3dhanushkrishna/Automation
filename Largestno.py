import unittest
def checklargestnoamong2(x,y):
    if x>y:
        return True
    else:
        return False
class mychecklargestno(unittest.TestCase):
    def test_check_1(self):
        a=10
        b=9
        c=checklargestnoamong2(a,b)
        self.assertTrue(c)

    def test_case_2(self):
        a=10
        b=20
        c=checklargestnoamong2(a,b)
        self.assertFalse(c)
if __name__=="__main__":
    unittest.main()
