# Project Euler | Problem 4 | Jacob Waters
# Find the largest palindrome made from the product of two 3-digit numbers.
# 906609
# date : 2013.12.10


def largestPalindromeProduct():
  largestPalindrome = 0
  for i in range(1000,100,-1):
    for j in range(1000,100,-1):
      product = i*j
      if str(product) == str(product)[::-1]:
        # print i, j, product
        if product > largestPalindrome:
          largestPalindrome = product
  
  return largestPalindrome

print largestPalindromeProduct()