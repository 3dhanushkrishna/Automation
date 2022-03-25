import unittest
def LogIn(username,password):
    if username == "admin" and password == "12345":
        return True
    else:
        return False
class LogInCheck(unittest.TestCase):
    def test_login(self):
        username="admin"
        password="12345"
        result=LogIn(username,password)
        self.assertTrue(result)
    def test_login_1(self):
        username = "admin1"
        password = "12345"
        result = LogIn(username, password)
        self.assertFalse(result)
if __name__== "__main__":
    unittest.main()
