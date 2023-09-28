from copy import deepcopy
from functools import reduce
import sys
sys.path.append('../')


def toNum(p):
    if type(p) == int:
        return p
    if p == []:
        return 0
    return int(''.join(map(str, p)), 2)


def toPoly(n):
    if type(n) == list:
        return n
    if type(n) == str:
        return list(map(lambda x: int(x), n))
    return list(map(lambda x: int(x), bin(n)[2:]))


def toStr(p):
    p = toPoly(p)
    return ''.join(map(str, p))


def red(p):
    while (len(p) > 1 and p[0] == 0):
        p.pop(0)
    return p


def proxy(func):
    def wrapper(*args):
        args = list(map(lambda x: toPoly(deepcopy(x)), args))
        return func(*args)
    return wrapper


@proxy
def sum_(a, b):
    a.reverse()
    b.reverse()
    if (len(a) < len(b)):
        a, b = b, a
    res = []
    for i in range(len(a)):
        if i >= len(b):
            res.append(a[i])
        else:
            res.append(a[i] + b[i])
    res.reverse()
    return red(list(map(lambda x: x % 2, res)))


@proxy
def prod_(a, b):
    if a == [0] or b == [0]:
        return 0
    a = toPoly(a)
    b = toPoly(b)
    a.reverse()
    results = []
    for i in range(len(a)):
        if a[i] == 1:
            results.append(b + [0] * i)
    res = reduce(lambda x, y: sum_(x, y), results, [])
    return res


@proxy
def div_(a, b):
    if b == [1]:
        return (a, [0])
    quotient = [0]
    while len(a) >= len(b):
        grade = len(a) - len(b)
        multiplicand = [1] + [0] * grade
        p = prod_(b, multiplicand)
        a = sum_(p, a)
        quotient = sum_(quotient, multiplicand)
        red(a)
    return [quotient, a]


@proxy
def bez_(a, b):
    q, r = div_(a, b)
    if r == [0]:
        return (0, 1)
    [u, v] = bez_(b, r)
    m = v
    n = sum_(prod_(q, v), u)
    return [m, n]


@proxy
def prodG_(a, b, g):
    return div_(prod_(a, b), g)[1]


@proxy
def invG_(a, g):
    return bez_(a, g)[0]


def expG_(a, n, g):
    if n == 0:
        return [1]
    if n == 1:
        return a
    if n % 2 == 0:
        return prodG_(expG_(a, n // 2, g), expG_(a, n // 2, g), g)
    else:
        return prodG_(a, expG_(a, n - 1, g), g)


@proxy
def ordG_(a, g):
    i = 1
    while expG_(a, i, g) != [1]:
        i += 1
    return i


def prod(a, b):
    return toNum(prod_(a, b))


def div(a, b):
    return list(map(lambda x: toNum(x), div_(a, b)))


def bez(a, b):
    return list(map(lambda x: toNum(x), bez_(a, b)))


def prodG(a, b, g):
    return toNum(prodG_(a, b, g))


def invG(a, g):
    return toNum(invG_(a, g))


def expG(a, n, g):
    return toNum(expG_(a, n, g))


def ordG(a, g):
    return ordG_(a, g)
