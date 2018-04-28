#!/usr/bin/python

import unittest


class Stack(object):
    def __init__(self):
        self.x = [0]*10000
        self.n = 0
    
    def size(self):
        return self.n

    def push(self, a):
        self.x[self.n] = a
        self.n +=1 

    def top(self):
        return self.x[self.n - 1]

    def pop(self):
        self.n -= 1


def Navigator_dfs(root, country_map, theaters):
    q = Stack()
    q.push(root)
    while q.size() != 0:
        current = q.top()
#        print(current)
        q.pop()
        if current in theaters:
            print(current)
        for child in country_map[current]:
            q.push(child)

root = 1
country_map = [[], [0, 2], [5, 3], [0], [3], [7, 6], [], []]
theaters = [3, 5, 6]

class Unittest_testcase_Navigator_dfs(unittest.TestCase):
    def test_nav_00(self):
        self.assertEqual(Navigator_dfs(root, country_map, theaters), 5)

#class TetsStack(unittest.TestCase):
#    def teststack_00(self):
#        s = Stack()
#        self.assertEqual(s.size(), 0)
#        s.push(5)
#        self.assertEqual(s.size(), 1)
#        self.assertEqual(s.top(), 5)
#        s.pop()
#        self.assertEqual(s.size(), 0)

if __name__=='__main__':
    unittest.main()
    
