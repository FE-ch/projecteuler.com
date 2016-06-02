# -*- coding: utf-8 -*-
# @Author: ShawnFiend
# @Date:   2016-06-03 00:58:13
# @Last Modified by:   ShawnFiend
# @Last Modified time: 2016-06-03 01:18:45

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

