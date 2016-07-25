import math

n = 40 # Number of steps to get to 20x20
k = 20 # Number of steps on a single axis

# k-combination
print(math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))
