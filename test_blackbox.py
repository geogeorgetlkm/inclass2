import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome to the Flask App!", response.get_json()["message"])

    def test_api_data_route_valid(self):
        response = self.app.post("/api/data", json={"a": 5, "b": 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["result"], 8)

    def test_api_data_route_invalid(self):
        response = self.app.post("/api/data", json={"x": 5})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid input", response.get_json()["error"])

if __name__ == "__main__":
    unittest.main()


