from __future__ import print_function
import sys

def triangle(s1, s2, s3):
    if s1 <= 0 or s2 <= 0 or s3 <= 0:
        return 'INVALID'

    # Check triangle inequality
    if s1+s2 <= s3 or s2+s3 <= s1 or s1+s3 <= s2:
        return 'INVALID'

    # Identify equilateral triangles
    if s1 == s2 == s3:
        return 'EQUILATERAL'

    # Identify isosceles triangles
    if s1 == s2 or s1 == s3 or s2 == s3:
        return 'ISOSCELES'

    return 'SCALENE'


if __name__ == '__main__':
    sys.exit(return 0)
