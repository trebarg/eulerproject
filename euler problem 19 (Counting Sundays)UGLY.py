import datetime



# startMonth = 1
# endMonth = 12
startYear = 1901
endYear = 2000
numberSundays = 0
i = startYear
while i <= endYear:
#     leapYear = 0
#     isLeapYear = "no"
#     isCentury = "no"
#     century = 0
#     century = i % 1000
#
#     if century == 0:
#         leapYear = i % 400
#         isCentury = "yes"
#         if leapYear == 0:
#                 isLeapYear = "yes"
#     else:
#         leapYear = i % 4
#         if leapYear == 0:
#             isLeapYear = "yes"
#     #print str(i)+" LeapYear:"+str(isLeapYear)+" Century:"+str(isCentury)

    x = 1
    # daysInYear = 0
    # monthsWith30Days = (4, 6, 9, 11)
    # monthsWith31Days = (1, 3, 5, 7, 8, 10, 12)

    while x <= 12:
        testDate = datetime.date(i, x, 1)
        if datetime.datetime.weekday(testDate) == 6:
            print str(x)+"/1/"+str(i)+" "+str(datetime.datetime.weekday(testDate))
            numberSundays += 1


        # if x in monthsWith30Days:
        #     daysInYear = daysInYear+30
        # if (x == 2):
        #     if isLeapYear == "yes":
        #         daysInYear += 29
        #     else:
        #         daysInYear += 28
        # if x in monthsWith31Days:
        #     daysInYear += 31

        x +=1

    #print str(i)+" "+str(daysInYear)
    i += 1
print numberSundays