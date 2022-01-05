## @file test_driver.py
#  @author Mahad Aziz
#  @brief Test cases for complex_adt.py and triangle_adt.py
#  @date January 21, 2021

import math
from complex_adt import ComplexT
from triangle_adt import TriangleT, TriType

def complextestcases():
    test1 = ComplexT(0,0)
    test2 = ComplexT(0,1)
    test3 = ComplexT(1,0)
    test4 = ComplexT(-1,0)
    test5 = ComplexT(1,1)
    test6 = ComplexT(1,1)
    test7 = ComplexT(2,3)
    test8 = ComplexT(-1,-1)
    test9 = ComplexT(8,6)
    test10 = ComplexT(3,-4)
    test11 = ComplexT(-3,4)
    test12 = ComplexT(-0,-0)
    test13 = ComplexT(1,2)

    print("\nComplexT Testing:")

    #real and imag test cases
    assert(test1.real() == 0 and test1.imag() == 0)
    assert(test2.real() == 0 and test2.imag() == 1)
    assert(test3.real() == 1 and test3.imag() == 0)
    print("real and imag test cases passed")

    #get_r test cases
    assert(test1.get_r() == 0)
    assert(test2.get_r() == 1)
    assert(test3.get_r() == 1)
    assert(test10.get_r() == 5)
    assert(test11.get_r() == 5)
    print("get_r test cases passed")

    #get_phi
    assert(test4.get_phi() == math.pi)
    assert(test1.get_phi() == 0)
    assert(math.isclose(test5.get_phi(),0.7853981633974484))
    assert(math.isclose(test10.get_phi(),-0.9272952180016122))
    assert(math.isclose(test11.get_phi(),2.214297435588181))
    print("get_phi test cases passed")

    #equal
    assert(test1.equal(test5) == False)
    assert(test5.equal(test6) == True)
    assert(test2.equal(test2) == True)
    assert(test12.equal(test1) == True)
    assert(test9.equal(test9) == True)
    print("equal test cases passed")

    #conj
    assert(test2.conj().real() == 0 and test2.conj().imag() == -1)
    assert(test1.conj().real() == 0 and test1.conj().imag() == 0)
    assert(test5.conj().real() == 1 and test5.conj().imag() == -1)
    assert(test10.conj().real() == 3 and test10.conj().imag() == 4)
    assert(test11.conj().real() == -3 and test11.conj().imag() == -4)
    print("conj test cases passed")

    #add
    assert(test3.add(test4).real() == 0 and test3.add(test4).imag() == 0)
    assert(test1.add(test7).real() == 2 and test1.add(test7).imag() == 3)
    assert(test8.add(test2).real() == -1 and test8.add(test2).imag() == 0)
    assert(test1.add(test12).real() == 0 and test1.add(test12).imag() == 0)
    assert(test7.add(test11).real() == -1 and test7.add(test11).imag() == 7)
    print("add test cases passed")

    #sub
    assert(test1.sub(test8).real() == 1 and test1.sub(test8).imag() == 1)
    assert(test5.sub(test8).real() == 2 and test5.sub(test8).imag() == 2)
    assert(test7.sub(test1).real() == 2 and test7.sub(test1).imag() == 3)
    assert(test1.sub(test12).real() == 0 and test1.sub(test12).imag() == 0)
    assert(test7.sub(test11).real() == 5 and test7.sub(test11).imag() == -1)
    print("sub test cases passed")

    #mult
    assert(test1.mult(test8).real() == 0 and test1.mult(test8).imag() == 0)
    assert(test2.mult(test3).real() == 0 and test2.mult(test3).imag() == 1)
    assert(test7.mult(test8).real() == 1 and test7.mult(test8).imag() == -5)
    assert(test10.mult(test11).real() == 7 and test10.mult(test11).imag() == 24)
    assert(test9.mult(test10).real() == 48 and test9.mult(test10).imag() == -14)
    print("mult test cases passed")

    #recip
    assert(test5.recip().real() == 0.5 and test5.recip().imag() == -0.5)
    assert(test2.recip().real() == 0 and test2.recip().imag() == -1)
    assert(test8.recip().real() == -0.5 and test8.recip().imag() == 0.5)
    assert(test10.recip().real() == 0.12 and test10.recip().imag() == 0.16)
    assert(test11.recip().real() == -0.12 and test11.recip().imag() == -0.16)
    print("recip test cases passed")

    #div
    assert(test1.div(test8).real() == 0 and test1.div(test8).imag() == 0)
    assert(test7.div(test3).real() == 2 and test7.div(test3).imag() == 3)
    assert(test7.div(test8).real() == -2.5 and test7.div(test8).imag() == -0.5)
    assert(test10.div(test11).real() == -1 and test10.div(test11).imag() == 0)
    assert(test11.div(test10).real() == -1 and test11.div(test10).imag() == 0)
    print("div test cases passed")

    #sqrt
    assert(test1.sqrt().real() == 0 and test1.sqrt().imag() == 0)
    assert(test3.sqrt().real() == 1 and test3.sqrt().imag() == 0)
    assert(test9.sqrt().real() == 3 and test9.sqrt().imag() == 1)
    assert(test10.sqrt().real() == 2 and test10.sqrt().imag() == -1)
    assert(math.isclose(test13.sqrt().real(),1.272019649514069) and math.isclose(test13.sqrt().imag(),0.7861513777574233))
    print("sqrt test cases passed")

    print("ComplexT test cases passed\n")

def triangletestcases():
    test1 = TriangleT(0,0,0)
    test2 = TriangleT(-1,2,3)
    test3 = TriangleT(1,1,100)
    test4 = TriangleT(2,2,2)
    test5 = TriangleT(3,8,6)
    test6 = TriangleT(8,6,3)
    test7 = TriangleT(2,2,2)
    test8 = TriangleT(3,4,6)
    test9 = TriangleT(3,4,5)
    test10 = TriangleT(2,2,3)

    print("TriangleT testing:")
    
    #get_sides
    assert(test5.get_sides() == (3,8,6))
    assert(test7.get_sides() == (2,2,2))
    assert(test3.get_sides() == (1,1,100))
    print("get_sides test cases passed")

    #equal
    assert(test4.equal(test7) == True)
    assert(test5.equal(test6) == True)
    assert(test4.equal(test5) == False)
    assert(test7.equal(test10) == False)
    assert(test8.equal(test9) == False)
    print("equal test cases passed")

    #perim
    assert(test4.perim() == 6)
    assert(test5.perim() == 17)
    assert(test8.perim() == 13)
    assert(test6.perim() == 17)
    assert(test10.perim() == 7)
    print("perim test cases passed")

    #area
    assert(math.isclose(test4.area(),1.7320508075688772))
    assert(math.isclose(test5.area(),7.644442425710328))
    assert(math.isclose(test8.area(),5.332682251925386))
    assert(math.isclose(test6.area(),7.644442425710328))
    assert(math.isclose(test10.area(),1.984313483298443))
    print("area test cases passed")

    #is_valid
    assert(test1.is_valid() == False)
    assert(test2.is_valid() == False)
    assert(test3.is_valid() == False)
    assert(test4.is_valid() == True)
    assert(test5.is_valid() == True)
    print("is_valid test cases passed")

    #tri_type
    assert(test4.tri_type() == TriType.equilat)
    assert(test5.tri_type() == TriType.scalene)
    assert(test9.tri_type() == TriType.right)
    assert(test10.tri_type() == TriType.isosceles)
    print("tri_type test cases passed")

    print("TriangleT test cases passed\n")

complextestcases()
triangletestcases()
