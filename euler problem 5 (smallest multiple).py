
eulerNumber = 500000000

i = 22


while i <= eulerNumber:
##        print(i)
        n = 11
        modTest = 0

        while n <= 20:
               
                testNumber = i % n
                modTest += testNumber
                n += 1
        i += 2
        if modTest == 0:
                print(i-1)
print("DONE")

