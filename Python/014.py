# Project Euler | Problem 14 | Jacob Waters
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Which starting number, under one million, produces the longest chain?
# date : 2015.01.25

def collatzSequence(n):
  # linked list type solution could be quicker
  maxChainLength = maxSequence = 0
  for i in range(2,n):
    j = i
    count = 0
    while i > 1:
      if i % 2 == 0: # even
        i /= 2
      else:
        i = 3 * i + 1
      count+=1

    # print j, count
    if count > maxChainLength:
      maxChainLength = count
      maxSequence = j

  return maxSequence

print collatzSequence(1000000)
