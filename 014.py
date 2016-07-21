# Longest Collatz sequence
# Problem 14

longest = 0
num = 0

for n in range(2, 1000000):
    chain = 0
    i = n
    while i is not 1:
        if i % 2 is 0:
            i = i // 2
        else:
            i = (3 * i) + 1
        chain += 1
    if chain > longest:
        longest = chain
        num = n

print(num)
