# Highly divisible triangular number
# Problem 12

import math

i = 1

while True:
    tri = sum(j for j in range(1, i+1))
    divisors = 0
    for n in range(1, (math.ceil(math.sqrt(tri)) + 1)):
        if tri % n is 0:
            divisors += 2
        if n * n == tri:
            divisors -= 1
    if divisors > 500:
        print(tri)
        break
    i += 1


