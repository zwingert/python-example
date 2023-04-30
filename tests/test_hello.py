import hello
import random

def test_triangle():
    assert hello.triangle(2 ,2 ,2) == 'EQUILATERAL'
    assert hello.triangle(3 ,3 ,3) == 'EQUILATERAL'
    assert hello.triangle(2 ,2 ,random.randint(0,1)) == 'INVALID'
