#!/usr/bin/python

import unittest

def next_permutation(perm):
    n = len(perm)
    for i in range(n):
        if i == n-1:
            return False
        if perm[n-2-i] < perm[n-1-i]:
            break
    for j in range(0, i+1):
        if perm[n-2-i] < perm[n-1-j]:
            break
    perm[n-2-i], perm[n-1-j] = perm[n-1-j], perm[n-2-i]
    perm[n - 1 - i:]=sorted(perm[n - 1 - i:])
    return True

def gen_permutations(n):
    permutation = list(range(1, n+1))
    while True:
        yield list(permutation)
        if not next_permutation(permutation):
            break

class TestGenPermutations(unittest.TestCase):
    def test_2(self):
        self.assertEqual(list(gen_permutations(2)), [[1, 2], [2, 1]])

    def test_3(self):
        perms3 = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(list(gen_permutations(3)), perms3)


class TestPerm(unittest.TestCase):
    def test_perm3_can_go(self):
        self.assertTrue(next_permutation([1, 2, 3]))
    
    def test_perm3_cant_go(self):
        self.assertFalse(next_permutation([3, 2, 1]))

    def test_perm3_step1(self):
        p = [1, 2, 3]
        self.assertTrue(next_permutation(p))
        self.assertEqual(p, [1, 3, 2])
    
    def test_perm3_step2(self):
        p = [1, 3, 2]
        self.assertTrue(next_permutation(p))
        self.assertEqual(p, [2, 1, 3])

    def test_perm3_step3(self):
        p = [2, 1, 3]
        self.assertTrue(next_permutation(p))
        self.assertEqual(p, [2, 3, 1])

    def test_perm3_step4(self):
        p = [2, 3, 1]
        self.assertTrue(next_permutation(p))
        self.assertEqual(p, [3, 1, 2])

    def test_perm3_step5(self):
        p = [3, 1, 2]
        self.assertTrue(next_permutation(p))
        self.assertEqual(p, [3, 2, 1])

    def test_perm3_step6(self):
        p = [3, 2, 1]
        self.assertFalse(next_permutation(p))

if __name__=='__main__':
    unittest.main()
