import unittest

def multiply(x, y):
    return x * y

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(2, 0), 0)
        self.assertEqual(multiply(-2, 5), -10)

if __name__ == '__main__':
    unittest.main()