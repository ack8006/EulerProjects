"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def main():
	allPrimes = []
	current = 2
	while (len(allPrimes) < 10001) :
		if (isItPrime(current, allPrimes)):
			allPrimes.append(current)
		current +=1
	print "lastPrime = " + str(current-1)
	print len(allPrimes)


def isItPrime(x, allPrimes):
    for primeNum in allPrimes:
        if (x % primeNum == 0):
            print "isItPrime " + str(x) + " " + str(primeNum)
            return False
    return True 

if __name__ == "__main__":
    main()