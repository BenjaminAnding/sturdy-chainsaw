# Burnside's lemma
# 2x2xn = 1/4(s**4 + 3s**2)

from math import factorial
from collections import Counter
from fractions import gcd


def cycle_count(c, n):
    count=factorial(n)
    for a, b in Counter(c).items():
        count//=(a**b)*factorial(b)
    return count        


def partitions(n, i=1):
    yield [n]
    for i in range(i, n//2 + 1):
        for p in partitions(n-i, i):
            yield [i] + p

            
def solution(w,h,s):
    permutations = factorial(w) * factorial(h)
    total = 0
    for width_partition in partitions(w):
        for height_partition in partitions(h):
            c = cycle_count(width_partition, w)*cycle_count(height_partition, h)
            total += c*(s**sum([sum([gcd(i, j) for i in width_partition]) for j in height_partition]))
    return str(total//permutations)

print(solution(2,2,3))
