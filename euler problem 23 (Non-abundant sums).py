import math
import time
start_time = time.time()

bound = 28123
i = 1


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
        elif i < currentAmicableSum:
            numberType = "Abundant"
        elif i > currentAmicableSum:
            numberType = "Deficient"
        print str(i) + " " + str(0) + " " + numberType
    else:
        while x <= halfEye:
            if (i % x == 0):

                currentAmicableSum +=x


            x += 1
        numberType = ""
        if i == currentAmicableSum:
                numberType = "Perfect"
        elif i < currentAmicableSum:
            numberType = "Abundant"
        elif i > currentAmicableSum:
            numberType = "Deficient"
        print str(i) + " " + str(currentAmicableSum)+" "+numberType
    i += 1

print(time.time() - start_time, "seconds")
