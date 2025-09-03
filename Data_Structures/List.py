
# a = [1,2,3,4,5]
# # List are Mutable , Orderd , Duplicate and Heterogenous
# for i in range(len(a)):
#     print(a[i])


b = [1 ,2, 3]
# b.insert(1, 10) => [1, 10, 2, 3]
# b.append(5) => [1, 2, 3, 5]
b.extend([5 , 30 , 60])


print (b)