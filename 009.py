# Special Pythagorean triplet
# Problem 9

# Brute force, but works...

result = 0

for c in range(100, 500):
    for b in range(100, c):
        for a in range(100, b):
            if a**2 + b**2 == c**2:
                if a + b + c == 1000:
                    result = a * b * c
                    break
        else:
            continue
        break
    else:
        continue
    break

print(result)
