i = 10000
loopLimit = 15000

highestNumDivisors = 0

while True:
    triangleNumber = 0
    numFactors = 0
 

    ##calculate triangleNumber
    triangleNumber = int((i * .5) * (i + 1))
    ##print(triangleNumber)

    x = 1
    while x*x < triangleNumber:
        if triangleNumber % x == 0:
            numFactors +=2
        if x*x == triangleNumber:
            numFactors +=1
        x += 1
        
    if triangleNumber == 1:
        numFactors = 1
        
    if highestNumDivisors < numFactors:
        highestNumDivisors = numFactors

    ##print(str(triangleNumber) + " " + str(numFactors))
    i += 1

    if highestNumDivisors > 500:
        print(str(i) + " " + str(triangleNumber)+ " " + str(highestNumDivisors))
        break

