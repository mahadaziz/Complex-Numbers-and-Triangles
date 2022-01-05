## @file complex_adt.py
#  @author Mahad Aziz
#  @brief This python module implements an abstract data type for complex numbers and various functions that can be applied to complex numbers.
#  @date January 21, 2021

import math

## @brief This class implements common functions on complex numbers
# @details Complex numbers have a real and imaginary part. The variable x is used for the real part and y is used for the imaginary part
class ComplexT:

    ## @brief Constructor for the ComplexT class that initializes the x and y fields that represent the real and the imaginary parts of the complex number
    # @param x Takes a float and assigns that to the real part of the complex number
    # @param y Takes a float and assigns that to the imaginary part of the complex number
    # @details An assumption for the constructor is that it is provided a non-zero float 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    ## @brief Getter function for the real part of the complex number
    # @return Returns the real part of the complex number which is stored in the variable x
    def real(self):
        return self.x

    ## @brief Getter function for the imaginary part of the complex number
    # @return Returns the imaginary part of the complex number which is stored in the variable y
    def imag(self):
        return self.y

    ## @brief This function calculates and returns the absolute value of the complex number
    # @return Returns the absolute value of the complex number
    def get_r(self):
        # Formula was found on https://en.wikipedia.org/wiki/Complex_number
        z = math.sqrt((self.x ** 2) + (self.y ** 2))
        return z

    ## @brief This function calculates and returns the argument or phase of the complex number
    # @return Returns the argument or phase of the complex number
    # @details An assumption for this function is that the real and imaginary parts of the complex number are not zero, If it is a zero complex number then it returns 0.
    def get_phi(self):
        # Formula was found on https://en.wikipedia.org/wiki/Complex_number
        if self.x > 0 or self.y != 0:
            return 2 * math.atan2(self.y, self.get_r() + self.x)
        elif self.x < 0 and self.y == 0:
            return math.pi
        elif self.x == 0 and self.y == 0:
            return math.atan2(self.y,self.x)

    ## @brief This function checks to see if the complex number passed as an argument is equal to the complex number in the class
    # @param z Takes a ComplexT object and checks if the complex number's real and imaginary parts are equal to the real and imaginary parts of the ComplexT object z
    # @return Returns true if the complex numbers are equal, otherwise it returns false
    # @details An assumption for this function is that it is provided a ComplexT object
    def equal(self, z):
        # Formula was found on https://en.wikipedia.org/wiki/Complex_number
        if self.x == z.real() and self.y == z.imag():
            return True
        return False

    ## @brief This function returns the complex conjugate of the complex number
    # @return Returns a ComplexT object of the complex number but the imaginary part is multiplied by -1
    def conj(self):
        # Formula was found on https://en.wikipedia.org/wiki/Complex_number
        return ComplexT(self.x, self.y * -1)

    ## @brief This function adds two complex numbers together and returns the sum
    # @param z Takes a ComplexT object and adds the real and imaginary parts to the complex number
    # @return Returns a ComplexT object where the real and imaginary parts are the sum of the real and imaginary parts of the two complex numbers
    # @details An assumption for this function is that it is provided a ComplexT object
    def add(self, z):
        # Formula was found on https://en.wikipedia.org/wiki/Complex_number
        return ComplexT(self.x + z.real(), self.y + z.imag())

    ## @brief This function subtracts two complex numbers together and returns the difference
    # @param z Takes a ComplexT object and subtracts the real and imaginary parts from the complex number
    # @return Returns a ComplexT object where the real and imaginary parts are the difference of the real and imaginary parts of the two complex numbers
    # @details An assumption for this function is that it is provided a ComplexT object
    def sub(self, z):
        # Formula was found on https://en.wikipedia.org/wiki/Complex_number
        return ComplexT(self.x - z.real(), self.y - z.imag())

    ## @brief This function multiplies two complex numbers together and returns the product
    # @param z Takes a ComplexT object and multiplies it to the complex number
    # @return Returns a ComplexT object that is the product of two multiplied complex numbers
    # @details An assumption for this function is that it is provided a ComplexT object
    def mult(self, z):
        # Formula was found on https://en.wikipedia.org/wiki/Complex_number
        return ComplexT(self.x * z.real() - self.y * z.imag(), self.x * z.imag() + self.y * z.real())

    ## @brief This function calculates and returns the reciprocal of a complex number
    # @return Returns a ComplexT object that is the reciprocal of the complex number
    # @details An assumption for this function is that it is provided a non-zero ComplexT object
    def recip(self):
        # Formula was found on https://en.wikipedia.org/wiki/Complex_number
        r = self.x / (self.x ** 2 + self.y ** 2)
        i = self.y * -1 / (self.x ** 2 + self.y ** 2)
        return ComplexT(r, i)

    ## @brief This function finds the quotient of two complex number by taking the complex number from the object and dividing it by the argument
    # @param z Takes a ComplexT object and the complex number is then divided by the argument
    # @return Returns a ComplexT object that is the quotient of the complex numbers
    # @details An assumption for this function is that it is provided a non-zero ComplexT object
    def div(self, z):
        # Formula was found on https://en.wikipedia.org/wiki/Complex_number
        cons = 1 / (z.real() ** 2 + z.imag() ** 2)
        r = cons * (z.real() * self.x + z.imag() * self.y)
        i = cons * (z.real() * self.y - z.imag() * self.x)
        return ComplexT(r, i)

    ## @brief This function calculates and returns the square root of a complex number
    # @return Returns a ComplexT object that is the square root of the complex number
    def sqrt(self):
        # Formula was found on https://en.wikipedia.org/wiki/Complex_number
        r = math.sqrt((self.x + self.get_r()) / 2)
        if self.y < 0:
            i = -1 * math.sqrt((-1 * self.x + self.get_r()) / 2)
        elif self.y > 0:
            i = math.sqrt((-1 * self.x + self.get_r()) / 2)
        else:
            i = 0
        return ComplexT(r, i)
