import math
import time
start_time = time.time()

bound = 28123


i = 1
perfectNumbers = list()
abundantNumbers = list()
deficientNumbers = list()

while i <= bound:
    currentAmicableSum = 0
    secondCurrentAmicableSum = 0
    halfEye = 0
    halfEye = math.ceil(i / 2)
    x = 1
    if i == 1:

        currentAmicableSum += 0

        numberType = ""
        if i == currentAmicableSum:
            numberType = "Perfect"
            perfectNumbers.append(i)
        elif i < currentAmicableSum:
            numberType = "Abundant"
            abundantNumbers.append(i)
        elif i > currentAmicableSum:
            numberType = "Deficient"
            deficientNumbers.append(i)
        print str(i) + " " + str(0) + " " + numberType
    else:
        while x <= halfEye:
            if (i % x == 0):

                currentAmicableSum +=x


            x += 1
        numberType = ""
        if i == currentAmicableSum:
            numberType = "Perfect"
            perfectNumbers.append(i)
        elif i < currentAmicableSum:
            numberType = "Abundant"
            abundantNumbers.append(i)
        elif i > currentAmicableSum:
            numberType = "Deficient"
            deficientNumbers.append(i)
        print str(i) + " " + str(currentAmicableSum)+" "+numberType
    i += 1

print "Perfect: "+str(len(perfectNumbers))
print "Abundant: "+str(len(abundantNumbers))
print "Deficient: "+str(len(deficientNumbers))

abundantSums = list()
for number in abundantNumbers:
    for innerNumber in abundantNumbers:
        if (number+innerNumber) < bound:
            abundantSums.append(number + innerNumber)
print len(abundantSums)
uniqueNumbers = list(set(abundantSums))
print len(uniqueNumbers)
finalAnswer = 0

i = 1

while i <= bound:
    if i not in uniqueNumbers:
        finalAnswer += i
    i += 1
print "FinalAnswer: "+str(finalAnswer)
print(time.time() - start_time, "seconds")
