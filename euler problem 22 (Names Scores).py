import time

start_time = time.time()

letter_count = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

f = open('p022_names.txt', 'r')
namesString = f.readline()
f.close()

namesString = namesString.replace('\"','')
listOfNames = namesString.split(',')

sortedListofNames = sorted(listOfNames)

namesScore = 0
nameOrderInList = 1
for name in sortedListofNames:
    localCharacterSum = 0
    splitOutName = list(name)
    for character in splitOutName:
            localCharacterSum += letter_count[str(character)]

    #print splitOutName
    #print nameOrderInList
    print str(nameOrderInList)+" "+str(name)+" "+str(localCharacterSum)+ " "+str(nameOrderInList * localCharacterSum)
    namesScore += (nameOrderInList * localCharacterSum)
    nameOrderInList += 1
#print listOfNames
#print sortedListofNames

print namesScore

print(time.time() - start_time, "seconds")
