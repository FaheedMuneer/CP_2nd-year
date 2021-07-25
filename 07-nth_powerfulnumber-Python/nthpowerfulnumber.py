# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import math
def power(x):
	while(x%2==0):
		c = 0
		while(x%2==0):
			x//=2
			c += 1
		if (c == 1):
			return False
	
	for i in range(3,int(math.sqrt(x))+1,2):
		c = 0
		while(x%i==0):
			x//=i
			c += 1
		if (c==1):
			return False
	return x == 1
def nthpowerfulnumber(n):
	# Your code goes here
	f = 0
	g = 0
	while(f<=n):
		g += 1
		if(power(g)):
			f += 1
	return g
