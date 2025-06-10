my_fr_set : frozenset = frozenset([1,2,3,4])
my_fr_set1: frozenset = frozenset([1,2,3,4,5,6,7])

# 1. difference(): Returns a new frozenset with elements present in the first frozenset but not in the second.
print(my_fr_set.difference(my_fr_set1))


# 2. intersection(): Returns a new frozenset containing only elements common to both frozensets.
print(my_fr_set1.intersection(my_fr_set))

# 3. union(): Returns a new frozenset containing all unique elements from both frozensets.
print(my_fr_set.union(my_fr_set1))

# 4. symmetric_difference(): Returns a new frozenset with elements that are in either of the sets but not in both.
print(my_fr_set.symmetric_difference(my_fr_set1))

# 5. isdisjoint(): Returns True if the two frozensets have no elements in common; otherwise, False.
print(my_fr_set.isdisjoint(my_fr_set1))

# 6. issubset(): Returns True if all elements of the first frozenset are present in the second frozenset.
print(my_fr_set.issubset(my_fr_set1))

# 7. issuperset(): Returns True if all elements of the second frozenset are present in the first frozenset.
print(my_fr_set1.issuperset(my_fr_set))

# 8. copy(): Returns a new frozenset that is a shallow copy of the original.
print(my_fr_set.copy())