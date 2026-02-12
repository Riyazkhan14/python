'''
Python frozenset
frozenset is an immutable version of a set.

Like sets, it contains unique, unordered, unchangeable elements.

Unlike sets, elements cannot be added or removed from a frozenset.

Creating a frozenset
Use the frozenset() constructor to create a frozenset from any iterable.'''

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

cp = x.copy()
print(cp)

a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.difference(b))
print(a - b)
