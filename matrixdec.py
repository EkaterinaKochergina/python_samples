#!/usr/bin/python

import unittest

class Matrixline(object):
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.dat = [0]*(w*h)

#    def __repr__(self):
#        return "MatrixDec({!r})".format(self.dat)

    def get(self, p, q):
        return self.dat[p*self.w + q]
          
    def set(self, p, q, value):
        self.dat[p*self.w + q] = value


class UnittestMatrixline(unittest.TestCase):
    
    def test_Matrixline_init(self):
        mat = Matrixline(3, 5)
        mat.set(1, 3, 24)
        self.assertEqual(mat.h, 3)
        self.assertEqual(mat.w, 5)
        self.assertEqual(mat.get(1, 3), 24)


if __name__=='__main__':
    unittest.main()
