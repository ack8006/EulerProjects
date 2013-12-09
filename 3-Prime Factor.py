"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

search for primes, if prime is found check it against the number,
yes add and recheck for some number, if not then continue search
for prime number.  Stop when number is completely factored (i.e.
when prime numbers multiply up to the full).
"""

"""
def generatePrimeArray(maxPrime):
    x = 2
    while (x<=maxPrime):
        if (toFactor % x ==0):
            checkPrime(x)

"""
#primeNumbers = []
toFactor = 600851475143

def findFactors():
    factor = True
    prime = False
    allPrimes = []
    primeFactors = []
    x = 2
    while (factor):
        prime = isItPrime(x, allPrimes)
        if (prime):
            allPrimes.append(x)
            #I am here
    
    
def isItPrime(x, allPrimes):
    for primeNum in allPrimes:
        if (x % primeNum == 0):
            return False
    return True 
        


#generatePrimeArray(toFactor/2)
