# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

def ok(a):
	s = 0
	while(a>0):
		r = a%10
		s += r*r
		a //= 10
	return s

def happy(b):
	while(b>=10):
		b = ok(b)
		if(b == 1):
			return True
	return False

def nth_happy_number(n):
	if n == 1:
		return 1
	if n == 2:
		return 7
	x = 2; y = 8
	while (x<=n):
		if happy(y):
			x += 1
		if x == n:
			return y
		y += 1

		
