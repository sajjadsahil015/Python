import unittest
from calculator import add

# class TestAddFunction(unittest.TestCase):
#     def test_add_positive(self):
#         self.assertEqual(add(2, 3), 5)

#     def test_add_negative(self):
#         self.assertEqual(add(-1, -4), -5)

# if __name__ == '__main__':
#     unittest.main()

def even(n):
    if n%2 == 0:
        return True
    else:
        return False

class TestEvenFunction(unittest.TestCase):
    def test_even(self):
        self.assertTrue(even(4))
    def test_even_false(self):
        self.assertFalse(even(9))

if __name__ == '__main__':
    unittest.main()