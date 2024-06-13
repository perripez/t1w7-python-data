def greet(fname, lname):
    print(f"Hello, {fname} {lname}!!")

greet("Max", "Brenner")

# Using Keyword Args
greet(fname="Max", lname="Brenner")

greet(lname  = "Brenner", fname = "Max")

def describe_pet(pet_name, animal_type="dog"): # animal_type has a default value
    print(f"I have a {animal_type} named {pet_name}")

# Positional argument
describe_pet("Barney")

# Positional and default argument
describe_pet("Frankie", "cat")

# Keyword arguments
describe_pet(animal_type="cat", pet_name="Frankie")
