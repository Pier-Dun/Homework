numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    is_prime = True
    if i == 1:
        continue
    for j in range(2, i):
        is_prime = bool(i % j)
        if is_prime == False:
            not_primes += [i]
            break
    if is_prime == True:
        primes += [i]

print(primes)
print(not_primes)