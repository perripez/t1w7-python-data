# Creating a tuple
my_tuple = (1, 2, 3, 'a', 'happy')

# Accessing elements
print(my_tuple[3])
print(my_tuple[0])

# Attempting to chnge an element  (will rise an error)
# my_tuple[0] = 10

# Tupels can be unpacked
a, b, c, d, e = my_tuple
print(e, a)

# Tuples can contain other tuples (nested tuples)
nested_tuple = (1, (2,3), (4,5), (0,0))
print(nested_tuple[1][1])


