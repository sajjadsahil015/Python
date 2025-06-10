my_set:set = {1,2,3}
my_set1 = set([1,2,3,"a",True,4])
# 1. add(): Adds an element to the set.
# my_set.add(5)
# print(my_set)

# 13. remove(): Removes the specified element. Raises an error if the element is not present.
# my_set.remove(5)
# print(my_set)

# 17. update(): Update the set with the union of this set and others
# my_set.update([4,5,6])
# print(my_set)

# 5. difference_update(): Removes the items in this set that are also included in another, specified set.
# my_set.difference_update([4,5,6])
# print(my_set)

# 16. union(): Returns a set containing the union of sets.
# my_set2 = my_set.union(my_set1)
# print(my_set2)
# my_set3 = my_set1 | my_set2
# print(my_set3)

# 12. pop(): Removes a random element from the set
# my_set3.pop()
# print(my_set3)

# 13. remove(): Removes the specified element. Raises an error if the element is not present.
# my_set3.remove(3)
# print(my_set3)


# 6. discard(): Remove the specified item.
# my_set3.discard(8)

# 3. copy(): Returns a copy of the set.
# set4 = my_set.copy()
# print(set4)

# 4. difference(): Returns a set containing the difference between two or more sets.
print(my_set1.difference(my_set))

# 7. intersection(): Returns a set, that is the intersection of two other sets.
print(my_set.intersection(my_set1))

# 9. isdisjoint(): Returns whether two sets have a intersection or not.
print(my_set.isdisjoint(my_set1))

# 10. issubset(): Returns whether another set contains this set or not.
print(my_set.issubset(my_set1))

# 11. issuperset(): Returns whether this set contains another set or not.
print(my_set1.issuperset(my_set))

