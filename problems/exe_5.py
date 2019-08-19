# This problem was asked by Jane Street.
#
# cons(a, b) constructs a pair, and car(pair) and cdr(pair)
# returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3,
# and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
#
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(fun):
    a = lambda x,y: x
    return fun(a)


print(cons(3, 4)(lambda x,y: x))
print(car(cons(3, 4)))


def cdr(fun):
    a = lambda x,y: y
    return fun(a)


print(cons(3, 4)(lambda x,y: y))
print(cdr(cons(3, 4)))


# closure

