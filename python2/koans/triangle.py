#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    if a >= b+c or b >= a+c or c >= a+b:
	raise TriangleError

    sides = {a, b, c}
    if len(sides) == 1: # if all 3 are equal, 2 should be ignored in the set, leaving just 1
	return 'equilateral'
    elif len(sides) == 2: # if two are equal, there must be 2 distinct values left
	return 'isosceles'
    elif len(sides) == 3: # if no sides are equal, we will get three distinct values
	return 'scalene'
    


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
