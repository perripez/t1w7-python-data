my_set = {1, 2, 3, 4}

print(my_set)

# Adding an element
my_set.add(5)
print(my_set)

# Remove an element
my_set.remove(2)
print(my_set)

# Membership testing
print(3 in my_set)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_value = set_a.union(set_b)
print(union_value)
# = 1, 2, 3, 4, 5

# Intersection
intersection_value = set_a.intersection(set_b)
print(intersection_value)
# = 3

# Difference
difference_value_a = set_a.difference(set_b)
difference_value_b = set_b.difference(set_a)

print(difference_value_a) # = 1, 2 
print(difference_value_b) # = 4, 5

# will change depending on variable order