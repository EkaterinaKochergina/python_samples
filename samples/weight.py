import unittest

def find_weight(a, b):
    x0, y0 = 1, 0
    x1, y1 = 0, 1
    while b:
        q = a//b
        a, b = b, a%b
        x0, y0, x1, y1 = x1, y1, x0-q*x1, y0-q*y1
    return x0, y0


class Unittest_TestWeight(unittest.TestCase):
    def test_weight00(self):
        assertEqual(find_weight(2, 1), (1, 0))
        assertEqual(find_weight(5, 7), (3, -2))
        assertEqual(find_weight(10, 4), (1, -2))
find_weight(40, 39)
if __name__=='__main__':
    unittest.main()
