#!/usr/bin/python/

import unittest


class Reshape(object):

    def __init__(self, dat, r, c):
        self.r = r
        self.c = c


    def shape(self, dat, r, c):
        mat = [[0]*c for _ in range(r)]
        h = len(self.dat)
        w = len(self.dat[0])
        if h*w != r*c:
            return self.dat
        for t in range(h*w):
            mat[t/c][t%c] = self.dat[t/w][t%w]
        return mat

class Test_Reshape(self):
    def test_init_reshape(self, r, c)

if __name__ == '__main__':
    unittest.main()
