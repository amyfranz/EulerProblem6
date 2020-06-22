import math
def findSum(num):
  sumOfNum = 0
  sumOfSquares = 0
  for i in range(1, num+1):
    sumOfNum += i;
    sumOfSquares += math.pow(i, 2)
  return math.pow(sumOfNum, 2) - sumOfSquares




print(findSum(100))