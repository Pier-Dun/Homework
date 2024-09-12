import random


n = random.choice(range(3, 21))
result = ''

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if n % (i + j) == 0 and i < j:
            result += str(i) + str(j)


print(n, '-', result)