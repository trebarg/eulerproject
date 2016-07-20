import math

i = math.factorial(100)
print i
numLength = len(str(i))
print numLength

x = 0
sumChars = 0
while x < numLength:
    print str(i)[x]
    sumChars +=int(str(i)[x])
    x += 1
print sumChars
