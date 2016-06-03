# -*- coding: utf-8 -*-
# @Author: ShawnFiend
# @Date:   2016-06-03 14:36:18
# @Last Modified by:   ShawnFiend
# @Last Modified time: 2016-06-03 16:01:55

# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

N = 600851475143


# def find_prim(max):
# 	L = []
# 	x = 2
# 	for i in range(3, max, 2):
# 		if N % i == 0:
# 			L.append(i)
# 		# i += 1
# 	return L[len(L) - 1]

# print(find_prim(1000))

# =======================BEST SOLUTION========================
d = 2
while d < N/d:
	if N % d == 0:
		N /= d
	else:
		d += 1

print(N)