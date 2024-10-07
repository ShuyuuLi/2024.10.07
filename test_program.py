import unittest
from source.program import add
from source.program import divide

class TestAdd(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(add(1, 2), 3)

    def test_add2(self):
        self.assertNotEqual(add(1, 2), 2)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)

if __name__ == '__main__':
    unittest.main()