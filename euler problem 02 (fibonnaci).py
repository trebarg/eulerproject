i = 1
z = 4000000

lastOne = 0
lastTwo = 1

sumEuler = 0
while i < z:
    i = lastOne + lastTwo
    if (i % 2 == 0):
        print i
        sumEuler += i
    lastOne = lastTwo
    lastTwo = i
    
print sumEuler