from math import sqrt, floor

def find_primes_under_num(num):
    # Sieve of Eratosthenes
    p = 2
    primes_set = set()
    marked_set = set()

    num = floor(sqrt(num))

    while p <= num:
        primes_set.add(p)
        for i in range(p,num+1,p):
            if i not in marked_set:
                marked_set.add(i)

        for j in range(p,num+1):
            if j not in marked_set:
                p = j
                break
            else:
                p += 1

    return primes_set

def find_max_prime_factor(num):

    primes_under_number = find_primes_under_num(num)

    factors = []
    for prime in primes_under_number:

        while num % prime == 0:
            factors.append(prime)
            num /= prime

    return max(factors)

print(find_max_prime_factor(600851475143))

# Low performance, requires optimising.