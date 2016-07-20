import datetime

startYear = 1901
endYear = 2000
numberSundays = 0
i = startYear
while i <= endYear:
    x = 1
    while x <= 12:
        testDate = datetime.date(i, x, 1)
        if datetime.datetime.weekday(testDate) == 6:
            #print str(x)+"/1/"+str(i)+" "+str(datetime.datetime.weekday(testDate))
            numberSundays += 1
        x +=1
    i += 1
print numberSundays