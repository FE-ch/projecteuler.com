# -*- coding: utf-8 -*-
# @Author: root
# @Date:   2016-06-02 18:16:26
# @Last Modified by:   root
# @Last Modified time: 2016-06-02 20:25:19

from functools import reduce

def func(x):
	if x % 3 == 0 or x % 5 == 0:
		return x
L = list(range(1, 1000))

# nL = reduce(lambda x, y: x + y, list(map(func, L)))

L1 = list(map(func, L))

while None in L1:
	L1.remove(None)

print(sum(L1))

# ====================BEST SOLUTION===========================
s = sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])
print(s)