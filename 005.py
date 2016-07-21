# Smallest multiple
# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

i = 20

while True:
    even = True
    for j in range(1, 21):
        if i % j is not 0:
            even = False
            break
    if even is True:
        break
    i += 20
print(i)
