import math
import time
start_time = time.time()

bound = 10000
i = 1

amicableSum = 0
while i <= bound:
    currentAmicableSum = 0
    secondCurrentAmicableSum = 0
    halfEye = 0
    halfEye = math.ceil(i / 2)
    x = 1
    if i == 1:

        #amicableSum += 0
        currentAmicableSum += 0
        print str(i)+" 0"
    else:
        while x <= halfEye:
            if (i % x == 0):
                #amicableSum += x
                currentAmicableSum +=x
                #print str(i)+" "+str(x)

            x += 1
        secondHalfEye = math.ceil(currentAmicableSum / 2)
        y = 1
        while y <= secondHalfEye:
            if (currentAmicableSum % y == 0):
                #amicableSum += y
                secondCurrentAmicableSum += y
                #print str(i) + " " + str(x) + " " + str(y)
            y += 1


    if (secondCurrentAmicableSum == i) and (i != currentAmicableSum):
        amicableSum += i
        amicableSum += currentAmicableSum
        print str(i) + " " + str(currentAmicableSum)+" "+str(secondCurrentAmicableSum)+" "+str(amicableSum)
    i += 1

print "Sum: "+str(amicableSum/2)

print(time.time() - start_time, "seconds")
