#largest 3 digit number
eulerNumber = 999

def isPalindrome(n):
        ##convert to string
        forwards = str(n)
        ##reverse string
        backwards = forwards[::-1]
##      print(forwards)
##      print(forwards[::-1])
        ##if number matches, it is palindrome
        if (int(forwards) == int(backwards)):
                return True
        else:
                return False

##Code from the Interwebs for fast unique-i-fication
def uniqueList(n):
        noDupes = []
        [noDupes.append(i) for i in n if not noDupes.count(i)]
        return noDupes

##smallest 3 digit number
i = 100

##list to hold palindromes
palindromes = []

#loop through 100-999
while i <= eulerNumber:
##        print(i)

        ##smallest 3 digit number
        n = 100
        ##loop through multiplying current outer loop by 100-999
        while n <= eulerNumber:
                testNumber = i * n
                ##print(testNumber)
                ##check if Palindrome and add to list if it is
                if isPalindrome(testNumber):
                        palindromes.append(testNumber)
                        ##print(testNumber)
                n += 1
        i += 1

##print out palindromes.  There WILL be duplicates
##print(palindromes)

##make list unique
palindromes = uniqueList(palindromes)

##sort list lowest to highest
palindromes.sort()

##Print out last value in list
print(palindromes[len(palindromes) - 1])
