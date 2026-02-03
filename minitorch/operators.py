"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(x, y):
    return x * y
    # raise NotImplementedError

def id(x):
    return x
    # raise NotImplementedError

def add(x, y):
    return x + y
    # raise NotImplementedError

def neg(x):
    return -x;
    # raise NotImplementedError

def lt(x, y):
    return x < y
    # raise NotImplementedError

def eq(x, y):
    return x == y
    # raise NotImplementedError

def max(x, y):
    # return x if x > y else y
    if x > y:
        return x
    else:
        return y
    # raise NotImplementedError

def is_close(x, y):
    return abs(x - y) < 1e-2
    # raise NotImplementedError

def sigmoid(x):
    if x >= 0:
        return 1.0/(1.0 + math.exp(-x))
    else:
        return math.exp(x)/(1 + math.exp(x))
    # raise NotImplementedError

def relu(x):
    return max(0, x)
    # raise NotImplementedError

def log(x):
    return math.log(x)
    # raise NotImplementedError

def exp(x):
    return math.exp(x)
    # raise NotImplementedError

def log_back(x, k):
    return k/x
    # raise NotImplementedError

def inv(x):
    return 1/x
    # raise NotImplementedError

def inv_back(x, k):
    return k / (x**2)
    # raise NotImplementedError

def relu_back(x, d):
    return d if x > 0 else 0
    # raise NotImplementedError

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
def map(fn: Callable[[float], float], x: Iterable[float]) -> Iterable[float]:
# def map(fn: Callable[[float], float], x: Iterable[float]):
    return [fn(a) for a in x]
    # raise NotImplementedError

def zipWith(fn: Callable[[float, float], float], x: Iterable[float], y: Iterable[float]) -> Iterable[float]:
    return [fn(a, b) for a, b in zip(x, y)]
    # raise NotImplementedError

def reduce(fn: Callable[[float, float], float], start: float, x: Iterable) -> float:
    acc = start
    for a in x:
        acc = fn(acc, a)
    return acc
    # raise NotImplementedError

def negList(ls: Iterable[float]) -> Iterable[float]:
    return map(neg, ls)
    # raise NotImplementedError

def addLists(ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
    return zipWith(add, ls1, ls2)
    # raise NotImplementedError

def sum(ls: Iterable[float]) -> float:
    return reduce(add, 0, ls)
    # raise NotImplementedError

def prod(ls: Iterable[float]) -> float:
    return reduce(mul, 1.0, ls)
    # raise NotImplementedError