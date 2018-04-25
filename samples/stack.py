#!/usr/bin/python

import unittest


def braces(s):
    x = []
    for t in s:
        if t == '(' or t == '[':
            x.append(t)
        elif len(x)==0:
            return False
        else:
            v = x[-1]
            if t==')' and v!='(' or t==']' and v!='[':
                return False
            x.pop()
    return len(x) == 0
            
bra = braces

class Unittest_Stack(unittest.TestCase):
    def test_fact00(self):
        self.assertTrue(bra('()()[]'))

    def test_fact01(self):
        self.assertFalse(bra('('))

    def test_fact02(self):
        self.assertFalse(bra('()))'))


if __name__=='__main__':
    unittest.main()
