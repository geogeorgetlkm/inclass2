import unittest
from app import calculate_sum, get_status

class TestInternalFunctions(unittest.TestCase):
    def test_calculate_sum_valid(self):
        self.assertEqual(calculate_sum(5, 3), 8)
        self.assertAlmostEqual(calculate_sum(1.2, 3.4), 4.6)

    def test_calculate_sum_invalid(self):
        with self.assertRaises(ValueError):
            calculate_sum("5", 3)
        with self.assertRaises(ValueError):
            calculate_sum(None, 3)

    def test_get_status(self):
        self.assertEqual(get_status(), "healthy")

if __name__ == "__main__":
    unittest.main()
