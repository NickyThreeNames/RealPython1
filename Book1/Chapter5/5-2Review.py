weight = 0.2
animal = "newt"

# Concatenate a number and a string in one print statement
print( str(weight) + " kg is the weight of the newt.")

# Use format() to print a number and a string inside of another string
print ("{} kg is the weight of the newt {}.".format(weight, animal))
# Use format() to add objects inside a string using index numbers
print("{0} kg is the weight of the newt {1}.".format(weight, animal))

# Use format() to print new objects inside a string
print("{0} kg is the weight of the {1}.".format("5", "dog"))

#Pulled this from the repo, it is not in my version of the book