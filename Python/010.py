# Project Euler | Problem 10 | Jacob Waters
# Find the sum of all the primes below two million.
# 142913828922
# date : 2014.01.20


def sumOfPrimes(n):
    # slow implementation
    num = 3
    isPrime = True
    primeSum = 2

    while num < n:
        isPrime = True
        for j in xrange(3, int(num**0.5)+1, 2):
            if num % j == 0:
                isPrime = False
                break
        if isPrime:
            # print num
            primeSum += num
        num += 2

    return primeSum


def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    sieve = [True] * n
    for i in xrange(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)/(2*i)+1)
    return sum([2] + [i for i in xrange(3, n, 2) if sieve[i]])

# Time difference between my implementation of finding prime vs using a sieve
import time
start_time = time.time()
print sumOfPrimes(2000000)
# print rwh_primes(2000000)
print time.time() - start_time, "seconds"
