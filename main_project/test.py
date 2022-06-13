
import unittest
from calc import isNumber, calculateQuadraticEquationRoots


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
            [1, None, 'a'],
            [0, 1, 1]
        ]

        for v in values:
            x1, x2 = calculateQuadraticEquationRoots(v[0], v[1], v[2])
            self.assertIsNone(x1)
            self.assertIsNone(x2)

    def test_twin_root(self):
        values = [
            [-1, 0, 0, 0],
            [1, 0, 0, 0]
        ]

        for v in values:
            x1, x2 = calculateQuadraticEquationRoots(v[0], v[1], v[2])
            self.assertEqual(x1, x2)
            self.assertIsNotNone(x1) # becouse is equal, not need test x2
            self.assertIsNotInstance(x1, list)
            self.assertTrue(isNumber(x1))
            self.assertEqual(x1, v[3])

    def test_real_root(self):
        values = [
            [1, -1, -1, (1-5**0.5)*0.5, (1+5**0.5)*0.5],
            [1, 0, -1, -1, 1],
            [1, 1, -1, (-1-5**0.5)*0.5, (-1+5**0.5)*0.5],
            [-1, -1, 0, 0, -1],
            [-1, 1, 0, 1, 0],
            [1, -1, 0, 0, 1],
            [1, 1, 0, -1, 0],
            [-1, -1, 1, (-1+5**0.5)*0.5, (-1-5**0.5)*0.5],
            [-1, 0, 1, 1, -1],
            [-1, 1, 1, (1+5**0.5)*0.5, (1-5**0.5)*0.5]
        ]

        for v in values:
            x1, x2 = calculateQuadraticEquationRoots(v[0], v[1], v[2])
            self.assertNotEqual(x1, x2)
            self.assertIsNotNone(x1)
            self.assertIsNotNone(x2)
            self.assertIsNotInstance(x1, list)
            self.assertIsNotInstance(x2, list)
            self.assertTrue(isNumber(x1))
            self.assertTrue(isNumber(x2))
            self.assertEqual(x1, v[3])
            self.assertEqual(x2, v[4])

    def test_complex_root(self):
        values = [
            [-1, -1, -1, [-0.5, (3**0.5)*-0.5], [-0.5, (3**0.5)*0.5]],
            [-1, 0, -1, [0, -1], [0, 1]],
            [-1, 1, -1, [0.5, (3**0.5)*-0.5], [0.5, (3**0.5)*0.5]],
            [1, -1, 1, [0.5, (3**0.5)*0.5], [0.5, (3**0.5)*-0.5]],
            [1, 0, 1, [0, 1], [0, -1]],
            [1, 1, 1, [-0.5, (3**0.5)*0.5], [-0.5, (3**0.5)*-0.5]]
        ]

        for v in values:
            x1, x2 = calculateQuadraticEquationRoots(v[0], v[1], v[2])
            self.assertIsInstance(x1, list)
            self.assertIsInstance(x2, list)
            self.assertFalse(x1[0] == x2[0] and x1[1] == x2[1])
            self.assertTrue(isNumber(x1[0]))
            self.assertTrue(isNumber(x2[0]))
            self.assertTrue(isNumber(x1[1]))
            self.assertTrue(isNumber(x2[1]))
            self.assertEqual(x1[0], v[3][0])
            self.assertEqual(x1[1], v[3][1])
            self.assertEqual(x2[0], v[4][0])
            self.assertEqual(x2[1], v[4][1])


if __name__ == '__main__':
    unittest.main()


