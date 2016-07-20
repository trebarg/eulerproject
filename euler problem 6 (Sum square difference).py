
eulerNumber = 100

i = 1
sumSquare = 0
squareSum = 0

while i <= eulerNumber:
##        print(i)
        sumSquare += i*i
        squareSum += i
        i += 1

squareSum = squareSum * squareSum
difference = squareSum - sumSquare
print(sumSquare)
print(squareSum)
print(difference)
