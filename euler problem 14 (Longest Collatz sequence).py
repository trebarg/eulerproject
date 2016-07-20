import time
start_time = time.time()

i = 1
loopLimit = 1000000
eulerNumber = i
collatzChain = []
largestChain = 0
startingNumber = 0



while i <= loopLimit:
    ##print("Euler Number: " + str(int(eulerNumber)))
    collatzChain.append(int(eulerNumber))

    if  eulerNumber == 1:
        ##collatzChain.append(eulerNumber)
        x = 1
        
        if len(collatzChain) > largestChain:
            largestChain = len(collatzChain)
            startingNumber = eulerNumber
            print(str(i) + " " + str(largestChain))
        i += 1
        eulerNumber = i    
        #print(collatzChain)
        #print(len(collatzChain))
        
        collatzChain = []

    elif eulerNumber % 2 == 0:
        eulerNumber = eulerNumber / 2
        
    else:
        eulerNumber = (3 * eulerNumber) + 1
        
print(time.time() - start_time, "seconds")


        
        












