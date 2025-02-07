def primes(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

prime_filter = lambda nums: list(filter(primes, nums))

numbers = list(map(int, input().split()))
print(prime_filter(numbers))