# TLE

k = int(input())


def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0: 
            return False
    return True

def list_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

if is_prime(k):
    print(k)
else:
    primes = list_primes(k)
    divide_primses = []

    index = 0
    while k not in primes:
        if k % primes[index] > 0:
            index += 1
            continue
        k = k // primes[index]
        divide_primses.append(primes[index])
    divide_primses.append(k)
    print(divide_primses[-1])
        

