# 10001st prime
# Problem 7

import math

# Sieve of Eratosthenes

n = 10001 
#lower_bound = int(n * math.log(n) + (n * (math.log(math.log(n)) - 1)))
upper_bound = int(n * math.log(n) + (n * math.log(math.log(n))))

A = [True] * upper_bound

for i in range(3, upper_bound):
    if A[i] is True:
        A[i*i::2*i] = [False] * int(((upper_bound - (i * i) - 1) / (2 * i) + 1))

primes = [2] + [i for i in range(3, upper_bound, 2) if A[i]]
print(primes[n - 1])

