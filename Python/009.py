# Project Euler | Problem 9 | Jacob Waters
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# 31875000
# date : 2015.01.19


def pythagTriplet(n):
    for a in range(1, n/3):
        for b in range(a, n/2):
            c = n - a - b
            if (a**2 + b**2 == c**2):
                return a*b*c


print pythagTriplet(1000)
