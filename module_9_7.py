def is_prime(func):
    def wrapper(*args):
        if not(func(*args) % 2) or not(func(*args) % 3):
            print('Составное')
        else:
            print('Простое')
        return func(*args)
    return wrapper

@is_prime
def sum_three(*args):
    sum_ = sum(args)
    return sum_

result = sum_three(2, 3, 6)
print(result)
