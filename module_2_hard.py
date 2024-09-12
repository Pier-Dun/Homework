import random


n = random.choice(range(3, 21))
result = ''

for i in range(1, n // 2 + n % 2):
    for j in range(i+1, n):
        if n % (i + j) == 0:
            result += str(i) + str(j)


print(n, '-', result)
