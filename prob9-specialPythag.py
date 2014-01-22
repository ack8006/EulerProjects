"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def main():
	afterDerivationByHand()

def afterDerivationByHand():
	b = 1
	while b <= 999:
		a = (500000-(1000*b))/(1000-b)
		c = 1000 - a - b
		if (a+b+c == 1000 and isPythagorean(a,b,c) and a >0 and b >0 and c>0):
			print "a = " + str(a)
			print "b = " + str(b)
			print "c = " + str(c)
			print "product = " + str(a*b*c)
		b += 1


def isPythagorean(a, b, c):
	if ((a**2 + b**2) == c**2):
		return True
	else:
		return False

if __name__ == "__main__":
    main()


