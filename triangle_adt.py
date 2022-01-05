## @file triangle_adt.py
#  @author Mahad Aziz
#  @brief This python module implements an abstract data type for triangles and various functions that can be applied to triangles
#  @date January 21, 2021

import math
from enum import Enum, auto

## @brief This class implements the enumeration class for the different type of triangles
# @details The triangle type possibilities could be either equilateral, isosceles, right, or scalene
class TriType(Enum):
    equilat = auto()
    isosceles = auto()
    scalene = auto()
    right = auto()

## @brief This class implements common functions on triangles
# @details Triangles have 3 sides. The variables a, b, and c each represent a side length.
class TriangleT:

	## @brief Constructor for the TriangleT class that initializes the a, b, and c fields that represent the side lengths of the triangle
	# @param a Takes an integer and assigns that to the side length, a
	# @param b Takes an integer and assigns that to the side length, b
	# @param c Takes an integer and assigns that to the side length, c
	# @details An assumption for the constructor is that it is provided positive integers
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    ## @brief This function returns the side lengths of the triangle in a tuple
    # @return Returns the side lengths of a triangle in a tuple
    def get_sides(self):
        return (self.a, self.b, self.c)

    ## @brief This function checks to see if the triangle passed as an argument is equal to the triangle in the class
    # @param z Takes a TriangleT object and checks if the tuple of the side lengths after being sorted are equal to the sorted tuple of side lengths of the TriangleT object z
    # @return Returns true if the tuple of side lengths are equal, otherwise it returns false
    # @details An assumption for this function is that it is provided a valid TriangleT object
    def equal(self, z):
        if sorted(self.get_sides()) == sorted(z.get_sides()):
            return True
        return False

    ## @brief This function calculates and returns the perimeter of the triangle
    # @return Returns the sum of the side lengths of the triangle
    # @details An assumption for this function is that the triangle is valid
    def perim(self):
        return self.a + self.b + self.c

    ## @brief This function calculates and returns the area of the triangle
    # @return Returns the area of the triangle using Heron's formula
    # @details An assumption for this function is that the triangle is valid
    def area(self):
    	# Formula was found on https://www.mathsisfun.com/geometry/herons-formula.html
        x = self.perim() / 2
        a = math.sqrt(x * (x - self.a) * (x - self.b) * (x - self.c))
        return a

    ## @brief This function determines whether the triangle is valid given its side lengths
    # @return Returns false if any of the side lengths are less than or equal to 0 or if the sum of any two side lengths is less than the third side length. Otherwise it returns true
    def is_valid(self):
    	# Formula was found on https://www.mathsisfun.com/geometry/triangle-inequality-theorem.html
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        elif (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a):
            return False
        return True

    ## @brief This function determines what type of triangle it is given it's side lengths
    # @return Returns equilat if all sides are equal, isosceles if two sides are equal and the third isn't, right if the side lengths satisfy the Pythagorean Theorem, otherwise it returns scalene
    # @details An assumption for this triangle is that it is a valid triangle and that if a triangle is both isosceles and right then it will return it as an isosceles triangle
    def tri_type(self):
        if (self.a == self.b == self.c):
            return TriType.equilat
        elif (self.a == self.b) or (self.a == self.c) or (self.b == self.c):
            return TriType.isosceles
        elif (self.a ** 2 + self.b ** 2 == self.c ** 2) or (self.a ** 2 + self.c ** 2 == self.b ** 2) or (self.b ** 2 + self.c ** 2 == self.a ** 2):
            return TriType.right
        else:
            return TriType.scalene
