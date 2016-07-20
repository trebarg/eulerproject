import math

primeCount = 0
primeCountTarget = 10001

def isPrime(n):
	n = abs(int(n))
	
	if n < 2:
		return False
	if n == 2:
		return True
	if not n & 1:
		return False
	for x in range(3, int(n**0.5)+1,2):
		if n % x == 0:
			return False
	return True


i = 1
primeList = []

while True:
        if primeCount == primeCountTarget:
                break
        if isPrime(i):
                primeCount += 1
                primeList.append(i)
        i += 1

print(primeCount)
print(primeList)                
