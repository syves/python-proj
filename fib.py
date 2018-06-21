#!/usr/bin/python
import itertools

def fib():
    m = 0
    n = 1
    yield  m
    yield n

    while True:
        o = m + n
        yield o
        m,n = n, o

print(list(itertools.islice(fib(), 500)))
