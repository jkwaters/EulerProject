# Project Euler | Problem 3 | Jacob Waters
# What is the largest prime factor of the number 600851475143?
# 6857 
# date : 2013.12.10

def largestPrimeFactor(n):
  for i in xrange(3,int(n/2)+1,2):
    if n % i == 0 and isPrime(i):
      largest = i

  return largest

def isPrime(n):
  # **slow implementation and needs rework**
  isPrime = True
  for j in xrange(3,int(n**0.5)+1,2):
    if n % j == 0:
      isPrime = False
      break
  return isPrime

# print largestPrimeFactor(13195)
print largestPrimeFactor(600851475143)