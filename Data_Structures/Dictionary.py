# Dictionary are mutable , Duplicate , order ,hetrogeneous nature

# Syntax
# a = {1: "hello" , 12:56}
# print(type(a))


# d ={10 : 100 , 20 : 2000 , 30 : 3000}
# d[10] = 1000
# d.update({40 : 4000})

# d[10] = 1000 #updating
# d[50]  = 5000 #creating 
# del d[30] # delete
# print(d)

# Dictonary Traversing

# d = {10 : 100 , 20 : 2000 , 30 : 3000}

# for i in d.values():
#     print(i)


# Deep Copy
# a =[1,2,3,4]

# b = a
# b[0] = 100
# print (b) 

#Shallow copy
# a =[1,2,3,4]

# b = a.copy()
# b[0] = 100
# print (b) 

# Q1 Write a Python script to merge two Python dictionaries

# d1 = {10 : 100 , 20 : 200 , 30 : 300}
# d2 = {40 : 400 , 50 : 500 , 60 : 600}

# for i in d2:
#     d1[i] = d2[i]

#     print (d1)

# Q2 Write a Python program to sum all the values in a dictionary?

# d1 = {10 : 100 , 20 : 200 , 30 : 300} 
# sum = 0
# for i in d1:
#     sum = sum + d1[i]

# print (sum)

# Q4 Count the frequency of list on each element
# d1 = [1,1,1,1,2,2,2,2,3,3,3,4,5,6]
# d = {}
# for i in d1:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print (d)

# Q5 Write a Python program to combine two dictionary by adding
# values for common keys.

d1 = {10 : 100 , 20 : 200 , 40 : 300}
d2 = {40 : 400 , 50 : 500 , 60 : 600}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]

print(d1)