eulerNumber = 2**1000
digitString = list(str(eulerNumber))
##print(eulerNumber)

##print(len(digitString))

i = 0
digitSum = 0
while i < len(digitString):
    ##print(i)
    digitSum += int(digitString[i])
    i += 1
    
print(digitSum)