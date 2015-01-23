# Project Euler | Problem 9 | Jacob Waters
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
# 
# date : 2015.01.19

def pythagTriplet(n):
  for a in range(1,n):
    for b in range(1,n-a):
      for c in range(1,n):
        if (a + b + c == n and a**2 + b**2 == c**2):
          return a*b*c

print pythagTriplet(1000)