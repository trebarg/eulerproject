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

    halfEye = math.ceil(i / 2)
    x = 1

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
    #print str(i) + " " + str(currentAmicableSum)+" "+numberType
    i += 1
print(time.time() - start_time, "seconds")
#print "Perfect: "+str(len(perfectNumbers))
print "Abundant: "+str(len(abundantNumbers))
#print "Deficient: "+str(len(deficientNumbers))

abundantSums = list()
i = 0
j = 0
for i in range(0, len(abundantNumbers)):
  for j in range(i, len(abundantNumbers)):

        if (abundantNumbers[i]+abundantNumbers[j]) < bound:
            abundantSums.append(abundantNumbers[i]+abundantNumbers[j])
        j += 1
  i += 1
print "Sums: "+str(len(abundantSums))
uniqueNumbers = list(set(abundantSums))
print "Unique: "+str(len(uniqueNumbers))
print(time.time() - start_time, "seconds")
finalAnswer = 0

i = 0

while i < bound:
    if i not in uniqueNumbers:
        finalAnswer += i
    i += 1
print "FinalAnswer: "+str(finalAnswer)
print(time.time() - start_time, "seconds")
