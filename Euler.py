def sumSquareDiff():
  # Problem 6
  # 25164150
  sumOfSquare = 0
  sum = 0
  
  for i in range(1,101):
    sumOfSquare += i**2
    sum += i
  squareOfSum = sum**2
  diff = squareOfSum - sumOfSquare
  print diff

# sumSquareDiff()


def smallestMultiple():
  # Problem 5
  # 232792560
  n = 2520
  divide = True
  
  while divide:
    n += 1
    divide = False
    
    for i in range(1,21):
      if n % i != 0:
        divide = True
    if n % 1000000 == 0:
      print n
  
  print n

# smallestMultiple()


def largestPalindromeProduct():
  # Problem 4
  # 906609
  largestPalindrome = 0
  for i in range(1000,100,-1):
    for j in range(1000,100,-1):
      product = i*j
      if str(product) == str(product)[::-1]:
        print i, j, product
        if product > largestPalindrome:
          largestPalindrome = product
  
  print largestPalindrome
    
# largestPalindromeProduct()


def primeNumber(n):
  # Problem 7
  # 104743
  i = 1
  num = 1
  isPrime = True

  while i <= n:
    isPrime = True
    num += 1
    for j in range(2,(num)):
      if num % j == 0:
        isPrime = False
        # print "no", num
        break
    if isPrime == True:
      #print i, num
      i += 1

  print num

# primeNumber(10001)


def productInSeries():
  # Problem 8
  # 40824
  number = "73167176531330624919225119674426574742355349194934" + \
  "96983520312774506326239578318016984801869478851843" + \
  "85861560789112949495459501737958331952853208805511" + \
  "12540698747158523863050715693290963295227443043557" + \
  "66896648950445244523161731856403098711121722383113" + \
  "62229893423380308135336276614282806444486645238749" + \
  "30358907296290491560440772390713810515859307960866" + \
  "70172427121883998797908792274921901699720888093776" + \
  "65727333001053367881220235421809751254540594752243" + \
  "52584907711670556013604839586446706324415722155397" + \
  "53697817977846174064955149290862569321978468622482" + \
  "83972241375657056057490261407972968652414535100474" + \
  "82166370484403199890008895243450658541227588666881" + \
  "16427171479924442928230863465674813919123162824586" + \
  "17866458359124566529476545682848912883142607690042" + \
  "24219022671055626321111109370544217506941658960408" + \
  "07198403850962455444362981230987879927244284909188" + \
  "84580156166097919133875499200524063689912560717606" + \
  "05886116467109405077541002256983155200055935729725" + \
  "71636269561882670428252483600823257530420752963450"
  series = [int(x) for x in number]
  largestProduct = 0

  for i in range(0,len(series)-4):
    product = series[i] * series[i+1] * series[i+2] * series[i+3] * series[i+4]
    if product > largestProduct:
      largestProduct = product
  
  print largestProduct

productInSeries()


def sumOfPrimes(n):
  num = 3
  isPrime = True
  primeSum = 2

  while num < n:
    isPrime = True
    for j in xrange(3,int(num**0.5)+1,2):
      if num % j == 0:
        isPrime = False
        break
    if isPrime == True:
      # print num 
      primeSum += num
    num += 2

  print primeSum


def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    print sum([2] + [i for i in xrange(3,n,2) if sieve[i]])

# import time
# start_time = time.time()
# sumOfPrimes(2000000)
# rwh_primes(2000000)
# print time.time() - start_time, "seconds"


def productGrid():
  largestProduct = 0
  grid = [[8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8],
  [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0],
  [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,03,49,13,36,65],
  [52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91],
  [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
  [24,47,32,60,99,03,45,2,44,75,33,53,78,36,84,20,35,17,12,50],
  [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
  [67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21],
  [24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
  [21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95],
  [78,17,53,28,22,75,31,67,15,94,03,80,4,62,16,14,9,53,56,92],
  [16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57],
  [86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58],
  [19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40],
  [4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66],
  [88,36,68,87,57,62,20,72,03,46,33,67,46,55,12,32,63,93,53,69],
  [4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36],
  [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16],
  [20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54],
  [1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]]
  
  # verticle
  for i in range(0,20): # row
    for j in range(0,17): # column
      calc = grid[i][j] * grid[i][j+1] * grid[i][j+2] *grid[i][j+3]
      if calc > largestProduct:
        largestProduct = calc

  # horizontal
  for i in range(0,17): # row
    for j in range(0,20): # column
      calc = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
      if calc > largestProduct:
        largestProduct = calc

  # diagonal forward
  for i in range(0,17):
    for j in range(0,17):
      calc = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
      if calc > largestProduct:
        largestProduct = calc

  # diagonal back
  for i in range(3,21): # row
    for j in range(3,21):
      calc = grid[i][j] * grid[i-1][j-1] * grid[i-2][j-2] * grid[i-3][j-3]
      if calc > largestProduct:
        largestProduct = calc

productGrid()