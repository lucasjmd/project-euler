from math import sqrt, floor

def find_primes_under_num(num):
    # Sieve of Eratosthenes
    p = 2
    primes = []
    marked = []

    while p <= num:
        primes.append(p)
        for i in range(p,num+1,p):
            if i not in marked:
                marked.append(i)

        for j in range(p,num+1):
            if j not in marked:
                p = j
                break
            else:
                p += 1

    return primes













