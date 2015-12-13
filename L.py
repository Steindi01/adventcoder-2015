import sys
import math


def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0


def magic_new(a, b):
    if a < b:
        a, b = b, a  # swap a and b
    if a == 0 and b == 0:
        return 0
    else:
        return 2**(a - 1) - choose(a - 1, b - 1)

a = long(sys.stdin.readline())  # read integer number a from stdin
b = long(sys.stdin.readline())  # read integer number b from stdin
print magic_new(a, b)
