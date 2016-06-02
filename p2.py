# -*- coding: utf-8 -*-
# @Author: ShawnFiend
# @Date:   2016-06-03 00:58:13
# @Last Modified by:   ShawnFiend
# @Last Modified time: 2016-06-03 01:37:51

def fib(max):
	n, a, b =0, 1, 2
	L = []
	while n < max and a < 4000000:
		a, b = b, a + b
		n = n + 1
		if a % 2 == 0:
			L.append(a)
	return L

print(sum(fib(200)))

# =================BETTER SOLUTION======================
# This may be a small improvement.  The Fibonacci series is:

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...

# Now, replacing an odd number with O and an even with E, we get:

# O, O, E, O, O, E, O, O, E, O, O, E, O, O, E...

# And so each third number is even.  We don't need to calculate the odd numbers.  Starting from an two odd terms x, y, the series is:

# x, y, x + y, x + 2y, 2x + 3y, 3x + 5y

# And in Python, my solution is:

def calcE():
	x = y = 1
	sum = 0
	while (sum < 1000000):
		sum += (x + y)
		x, y = x + 2 * y, 2 * x + 3 * y
	return sum

