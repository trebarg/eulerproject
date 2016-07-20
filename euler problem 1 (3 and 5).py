i = 1
z = 1000
sumEuler = 0
while i < z:
    if (i % 3 == 0) and (i % 5 == 0):
        #print "3&5-" + str(i)
        sumEuler += i
    elif (i % 3 == 0):
        #print "3-" + str(i)
        sumEuler += i
    elif (i % 5 == 0):
        #print "5-" + str(i)
        sumEuler += i
    i += 1
    
print sumEuler