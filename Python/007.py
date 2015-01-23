# Project Euler | Problem 7 | Jacob Waters
# What is the 10 001st prime number?
# 104743
# date : 2013.12.10

def primeNumber(n):
  i = 1
  num = 1
  isPrime = True

  # **needs rework** slow implementation, could be faster
  while i <= n:
    isPrime = True
    num += 1
    for j in range(2,(num)):
      if num % j == 0:
        isPrime = False
        break
    if isPrime == True:
      i += 1
  return num

print primeNumber(10001)