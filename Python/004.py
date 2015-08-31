# Project Euler | Problem 4 | Jacob Waters
# Find the largest palindrome made from the product of two 3-digit numbers.
# 906609
# date : 2013.12.10


def largestPalindromeProduct():
    largestPalindrome = 0
    for i in xrange(999, 100, -1):
        for j in xrange(999, 100, -1):
            if str(i*j) == str(i*j)[::-1] and i*j > largestPalindrome:
                largestPalindrome = i*j

    return largestPalindrome

print largestPalindromeProduct()
