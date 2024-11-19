# Naming of this file is important, it must be in the form of test_<something>.py
from app import app
import unittest
from dotenv import load_dotenv


class RouteTest(unittest.TestCase):
    # setUp function, creates the application test instance
    def setUp(self):
        load_dotenv("../.env")
        self.app = app.test_client()
        self.app.testing = True

    # Test functions must be named as test_<name>
    def test_index_get(self):
        # mock sending a request to the index page
        response = self.app.get("/")

        # check if the response is 200
        self.assertEqual(response.status_code, 200)

    def test_index_post(self):
        # mock sending a request to the index page
        response = self.app.post("/")

        # check if the response is 405
        self.assertEqual(response.status_code, 405)

    def test_products(self):
        # mock sending a request to the index page
        response = self.app.get("/products")

        # check if the response is 200
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
