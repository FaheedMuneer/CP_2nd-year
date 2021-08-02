# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def ok(n,s=0):
	if n == 0:
		return s
	else:
		return ok(n//10,s = s*10 + n%10)

def hmm(n,s=0):
	if n == 0:
		return s
	else:
		if (n%10)%2 == 0:
			return hmm(n//10,s = s*10 + n%10)
		else:
			return hmm(n//10,s)

def evenL(l,i):
	if len(l) == i:
		return l
	else:
		a = l[i]
		l[i] = ok(hmm(a))
		return evenL(l, i + 1)
def fun_recursion_onlyevendigits(l): 
		if len(l) == 0:
			return []
		else:
			return evenL(l,0)
	