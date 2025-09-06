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

a =[1,2,3,4]

b = a
b[0] = 100
print (b) 
