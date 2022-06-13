
import unittest
from calc import calculateQuadraticEquationRoots


def isanumber(a):
    try:
        float(repr(a))
        return True
    except:
        return False


class Testing(unittest.TestCase):
    def test_wrong_values(self):
        values = [
            ['a', 'b', 'c'],
            ['a', 'b', 1],
            ['a', 1, 'c'],
            [1, 'b', 'c'],
            ['a', 1, 1],
            [1, 'b', 1],
            [1, 1, 'c'],
            [None, 1, 1],
            [1, 1, None],
            [1, None, 1],
            [1, None, 'a']
        ]

        for v in values:
            x1, x2 = calculateQuadraticEquationRoots(v[0], v[1], v[2])
            self.assertIsNone(x1)
            self.assertIsNone(x2)

    def test_twin_root(self):
        values = [
            [0, 0, -1],
            [-1, 0, 0],
            [0, 0, 0],
            [1, 0, 0],
            [0, 0, 1]
        ]

        for v in values:
            x1, x2 = calculateQuadraticEquationRoots(v[0], v[1], v[2])
            self.assertEqual(x1, x2)
            self.assertIsNotNone(x1) # becouse is equal, not need test x2
            self.assertIsNotInstance(x1, list)
            self.assertTrue(isanumber(x1))

    def test_real_root(self):
        values = [
            [0, -1, -1],
            [0, 1, -1],
            [1, -1, -1],
            [1, 0, -1],
            [1, 1, -1],
            [-1, -1, 0],
            [-1, 1, 0],
            [0, -1, 0],
            [0, 1, 0],
            [1, -1, 0],
            [1, 1, 0],
            [-1, -1, 1],
            [-1, 0, 1],
            [-1, 1, 1],
            [0, -1, 1],
            [0, 1, 1]
        ]

        for v in values:
            x1, x2 = calculateQuadraticEquationRoots(v[0], v[1], v[2])
            self.assertNotEqual(x1, x2)
            self.assertIsNotNone(x1)
            self.assertIsNotNone(x2)
            self.assertIsNotInstance(x1, list)
            self.assertIsNotInstance(x2, list)
            self.assertTrue(isanumber(x1))
            self.assertTrue(isanumber(x2))

    def test_complex_root(self):
        values = [
            [-1, -1, -1],
            [-1, 0, -1],
            [-1, 1, -1],
            [1, -1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]

        for v in values:
            x1, x2 = calculateQuadraticEquationRoots(v[0], v[1], v[2])
            self.assertIsInstance(x1, list)
            self.assertIsInstance(x2, list)
            self.assertFalse(x1[0] == x2[0] and x1[1] == x2[1])
            self.assertTrue(isanumber(x1[0]))
            self.assertTrue(isanumber(x2[0]))
            self.assertTrue(isanumber(x1[1]))
            self.assertTrue(isanumber(x2[1]))


if __name__ == '__main__':
    unittest.main()
