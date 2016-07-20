import math
import time
start_time = time.time()
eulerNumber = 1000
letterCounts = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "onehundred", 200: "twohundred", 300: "threehundred", 400: "fourhundred", 500: "fivehundred", 600: "sixhundred", 700: "sevenhundred", 800: "eighthundred", 900: "ninehundred", 1000: "onethousand" }
i = 1

charCount = 0
bigString = ""

while i <= eulerNumber:
    if len(str(i)) == 1:
        if i in letterCounts:
            currentOutput = letterCounts[i]
            charCount += len(currentOutput)
            bigString = bigString + currentOutput
            ##print(currentOutput, len(currentOutput))
            
    elif len(str(i)) == 2:
        x = int(str(i)[0]) * 10
        y = int(str(i)[1])
        if int(str(i)[0]) == 1:
            if i in letterCounts:
                currentOutput = letterCounts[i]
                charCount += len(currentOutput)
                bigString = bigString + currentOutput
                ##print(currentOutput, len(currentOutput))

        else:
            
            if y in letterCounts:
                currentOutput = letterCounts[x] + letterCounts[y]
                charCount += len(currentOutput)
                bigString = bigString + currentOutput
                ##print(currentOutput, len(currentOutput))

            else:
                currentOutput = letterCounts[x]
                charCount += len(currentOutput)
                bigString = bigString + currentOutput
                ##print(currentOutput, len(currentOutput))
            
             
    elif len(str(i)) == 3:
        x = int(str(i)[0]) * 100
        y = int(str(i)[1]) * 10
        z = int(str(i)[2])
        ##print(x,y,z)
        if z == 0 and y == 0:
            if x in letterCounts:
                currentOutput = letterCounts[x]
                charCount += len(currentOutput)
                bigString = bigString + currentOutput
                ##print(currentOutput, len(currentOutput))
        elif y == 0:
            if z in letterCounts:
                currentOutput = letterCounts[x] + "and" + letterCounts[z]
                charCount += len(currentOutput)
                bigString = bigString + currentOutput
                ##print(currentOutput, len(currentOutput))
        elif y == 10:
            yz = y + z
            if yz in letterCounts:
                currentOutput = letterCounts[x] + "and" + letterCounts[yz]
                charCount += len(currentOutput)
                bigString = bigString + currentOutput
                ##print(currentOutput, len(currentOutput))

        else: 
            if z == 0:
                currentOutput = letterCounts[x] +  "and" + letterCounts[y]
                charCount += len(currentOutput)
                bigString = bigString + currentOutput
                ##print(currentOutput, len(currentOutput))
            else:
                currentOutput = letterCounts[x] +  "and" +  letterCounts[y] +  letterCounts[z]
                charCount += len(currentOutput)
                bigString = bigString + currentOutput
                ##print(currentOutput, len(currentOutput))
        ##else:
            
    else:
        currentOutput = letterCounts[i]
        charCount += len(currentOutput)
        bigString = bigString + currentOutput
        ##print(currentOutput, len(currentOutput))
    i += 1
##print(charCount)
print(bigString)
print(len(bigString))
print(time.time() - start_time, "seconds")