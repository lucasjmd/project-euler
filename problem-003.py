from math import sqrt, floor
from time import time

def find_primes_under_num(num):
    # Sieve of Eratosthenes
    p = 2
    primes_bool_array = [True for x in range(floor(sqrt(num))+1)]
    primes_bool_array[0] = False
    primes_bool_array[1] = False

    num = floor(sqrt(num))

    for i in range(2,len(primes_bool_array)):
        if primes_bool_array[i] == True:
            for num in range(2*i,num+1,i):
                primes_bool_array[num] = False

    primes_set = set()

    for i in range(len(primes_bool_array)):
        if primes_bool_array[i] == True:
            primes_set.add(i)

    return primes_set

def find_max_prime_factor(num):

    primes_under_number = find_primes_under_num(num)

    factors = []
    for prime in primes_under_number:

        while num % prime == 0:
            factors.append(prime)
            num /= prime

    return max(factors)

print(find_max_prime_factor(14))

# Works but can use some bug fixes for certains nums being passed (e.g. 14)