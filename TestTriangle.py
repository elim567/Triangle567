# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right', '5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral', '3,4,5 should be equilateral')
        
    def testEquilaterialTriangleA(self):
        self.assertEqual(classifyTriangle(10,10,10), 'Equilateral', '10,10,10 is a Right triangle')
        
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(10,15,30), 'NotATriangle', '10,4,5 is an invalid input')
    
    def testIsoscelesTriangle(self):
        self. assertEqual(classifyTriangle(3,5,5), 'Isosceles', '3,5,5 should be isosceles')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(3,4,6), 'Scalene', '3,4,6 should be scalene')
        
    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(8,8,16), 'NotATriangle', '8,8,16 is an invalid input')
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

