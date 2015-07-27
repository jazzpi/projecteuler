#!/usr/bin/env python3
import math

n = 600851475143
sqrt = math.floor(math.sqrt(n))
primes = list(range(sqrt))
factor = 1
i = 2
while len(primes) > i:
    p = primes[i]
    i += 1
    if p is None:
        continue
    if n % p == 0:
        factor = p
    for j in range(p * 2, sqrt, p):
        primes[j] = None
print(factor)
