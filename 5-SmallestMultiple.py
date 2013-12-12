"""
2520 is the smallest number that can be divided by each 
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?
"""

import PrimeFactor as pf
import numpy as np
from types import *

def main():
	primeFactorArray = findPrimeFactorArray(2, 21)
	frequencyDict = primeFactorFrequency(primeFactorArray)
	print computeMultiple(frequencyDict)
	

def findPrimeFactorArray(a, b):
	pfa = []
	for x in xrange(a, b):
		factors = (pf.findFactors(2, x))
		pfa.append(factors)
	return pfa

def primeFactorFrequency(pfa):
	frequencyDict = dict.fromkeys([x for x in xrange(0 ,21)])
	for factorization in pfa:
		current = 0
		counter = 0
		for x in sorted(factorization):
			if (x != current):
				frequencyDict = checkFrequency(frequencyDict, current, counter)
				current = x
				counter = 1
			else:
				counter	+= 1
		frequencyDict = checkFrequency(frequencyDict, current, counter)
	return frequencyDict
				

def checkFrequency(theDict, cur, curFreq):
	if (theDict[cur] < curFreq):
		theDict[cur] = curFreq
	return theDict
	
def computeMultiple(frequencyDict):
	print frequencyDict
	multiple = 1
	for key, value in frequencyDict.items():
		if type(value) is IntType:
			localMult = key**value
		else:
			localMult = 1
		if (localMult !=0):
			multiple *= localMult
	return multiple

if __name__ == "__main__":
    main()