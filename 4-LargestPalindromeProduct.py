"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit 
numbers is 9009 = 91 x 99.
"""

maxA = 99
maxB = 99

def isPalendrome(x):
	if (str(x) == str(x)[::-1]):
		print "here"
		return True
	else:
		return False

def multiplier(a, b):
	maxPal = 0
	while (a<999):
		while (b<999):
			currentMult = a*b
			if (isPalendrome(currentMult) and currentMult>maxPal):
				maxPal = currentMult
			else:
				b+=1
		a+=1
		b=100
	print a 
	print b
	return maxPal

print "maxPal = " + str(multiplier(100,100))
