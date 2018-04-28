#!/usr/bin/python

import unittest
import itertools 

def permutation(p):
    list(itertools.permutations(p))

class Combination(object):
    def __inint__(self, p):
        self.p = []

class TestCombination(unittest.
TestCase):
    def test_init_comb(self):
        p = Combination[1, 2, 3]
    
    def test_comb_1(self):
        assertEqual(Combination([1,2,3]), [1,3,2])





if __name__ = '__mai__':
    unittest.main()
