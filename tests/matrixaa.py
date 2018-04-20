#!/usr/bin/python

import unittest
import math

class MatrixAA(object):
    def __init__(self, dat):
        if isinstance(dat, MatrixAA):
            self.dat = copy.deepcopy(dat.dat)
        else:
            self.dat = copy.deepcopy(dat)

    def init_shape(cls, h, w):
        return cls([[0]*w for _ in range(h)])

    def __repr__(self):
        return "Matrix({!r})".format(self.dat)

    def height(self):
        return len(self.dat)

    def width(self, p, q):
        return len(self.dat[0])

    def get(self, p, w):
        return self.dat[p][q]

    def __eq__(self, other):
        return self.dat == other.dat

    def __mul__(self, r):
        res = MatrixAA.shape_init(len(self.dat), len(r.dat[0]))
        for p in range(len(self.dat)):
            for q in range(len(r.dat[0])):
                val=0
                for ind in range(len(self.dat[0])):
                    val += self.dat[p][ind] * r.dat[ind][q]
                res.dat[p][q]=val
        return res

    def set(self, p, w, val):                                                 
        return self.dat[p][w] == val

    def vector_init(cls, vec):
        return cls([[t] for t in vec])

class TestMatrixAA(unittest.TestCase):
    def test_init_MatrixAA(self):
        mat = MatrixAA.dat([0, 0, 0], [0, 0, 0][0, 0, 0])
        self.assertEqual(mat.height(), 3)
        self.assertEqual(mat.width(), 3)

    def test_get_MatrixAA(self):
        a = MatrixAA.dat([1, 2, 3],[4, 5, 6],[7, 8, 9])
        self.assertEqual(a.get([2][1]), 5)
        a.set[2][1]=12
        self.assertEqual(a.get([2],[1]), 12)

    def test_MatrixAA_mul(self):
        a = MatrixAA([[1, 2], [3, 5]])
        b = MatrixAA([[-1, 1], [2, 0]])
	c = a * b
        self.assertEqual(c, MatrixAA([[3, 1], [7, 3]]))


if __name__ == '__main__':
    unittest.main()       
