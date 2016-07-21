# Summation of primes
# Problem 10

import math

n = 2000000
A = [True] * n
A[1] = False

for i in range(2, int(math.sqrt(n))):
    if A[i] is True:
        for k in range(n):
            j = i**2 + (k * i)
            if j >= n:
                break
            A[j] = False

result = [i for i in range(n) if A[i]]
print(sum(result))


