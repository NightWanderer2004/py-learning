# 1.1
# foo = 1
# foo_real = 1.0
# foobar = 10 + 2
# bar = 'example text'
# baz = "text2"
# spam = 1.3
# eggs = 1+2j

# 1.3
# foo = 1
# bar = 2
# print(foo + bar)

# qux = 'Lorem'
# quux = 'ipsum'
# print(qux + ' ' + quux)

# spam = 1j
# eggs = spam ** 2
# print(eggs)

# corge = 'AB'
# grault = corge * 4
# print(grault)

# 1.5
# baz = ['Poniedzialek', 'Wtorek', 'Sroda', 'Czwartek', 'Piatek']
# print(baz)
# print(baz[0])
# print(baz[1])
# print(baz[-2])

# qux = ['Jeden', [1, 2], 3+0j]
# print(qux[1][1])
# print(qux[1])

# 1.7
# foo = [10, 11, 12, 13, 14]
# print(foo[0:2])
# print(foo[:2])
# print(foo[-1])

# bar = foo[1:3]
# print(bar)

# 1.9
# spam = [10, 21, 23, 11, 24]
# spam.append(1)
# print(spam)
# print(spam.count(11))
# print(spam.index(11))
# print(spam.remove(11))
# print(spam)

# spam.sort()
# print(spam)

# spam.reverse()
# print(spam)

# 1.11
# foobar = (1, 'dwa')
# print(foobar)
# print(foobar[0])

# 1.13
# for foo in 'PYTHON':
#     print('%s.' % (foo))
# foobar = []
# for bar in range(5):
#     foobar.append(bar)

# 1.15
# def Pierwiastek(foo, bar):
#     return foo ** (1 / bar)


# def Dodaj(spam, ham):
#     eggs = spam + ham
#     return eggs


# def KodASCII(foobar):
#     return ord(foobar)


# def Dodaj2(foo, bar): return foo + bar


# 2.17
# import numpy as np
# print(np.pi)

# 2.19
import numpy as np


def zeros(size, dtype):
    return np.zeros(size, dtype)


def eye(size):
    return np.eye(size)


Z = zeros((2, 4), 'uint8')
print(Z)

I = eye(3)
print(I)


A = np.arange(9)
print(A)

A.shape = (3, 3)
print(A)

print(A.T)
print(A.min())
print(A.size)
