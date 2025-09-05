# Tuples are mutable ,No Duplicate, Unorderd, Semi hetrogenous(Not stor everything ) nature 
# we cannot access the index values 

# syntax
# s = {1,2,3,4}
# print(type(s))


# b = hash("Hello")
# print(b)

# c = hash((1,2,3))
# print(c)


# Method
# s = {1,2,3,4}
# s.add(5)
# s.remove(5)
# s.discard(5)
# s.pop()
# s.clear()

# print(s)


a = {1,2,3,4,5}
b = {4,7,8,9}

# s = a.union(b)
# s = a|b

# s = a.intersection(b)
# s = a & b

# s = a.difference(b)  
# s = b - a 

# s = a.symmetric_difference(b)
# s = a ^ b  

# compound operations
b -= a
print(b)