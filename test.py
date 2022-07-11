
from api import app
import unittest


class FlaskTest(unittest.TestCase):

    def test_root(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statusCode = response.status_code
        self.assertEqual(statusCode,200)

    def test_root_resp(self):
        tester = app.test_client(self)
        response = tester.get("/")
        text = response.text
        self.assertEqual(text,"Hello World")

    def test_version(self):
        tester = app.test_client(self)
        response = tester.get("/version")
        statusCode = response.status_code
        self.assertEqual(statusCode,200)

    def test_version_resp(self):
        tester = app.test_client(self)
        response = tester.get("/version")
        text = response.text
        self.assertEqual(text,"1.0.0")

    

if __name__ == "__main__":
    unittest.main()