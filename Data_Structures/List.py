
# a = [1,2,3,4,5]
# # List are Mutable , Orderd , Duplicate and Heterogenous
# for i in range(len(a)):
#     print(a[i])


#b = [1 ,2, 3]
# b.insert(1, 10) => [1, 10, 2, 3]
# b.append(5) => [1, 2, 3, 5]
# b.extend([5 , 30 , 60]) => [1, 2, 3, 5, 30, 60]

#print (b)

# Q1 -  Print positive and negative elements of an List?

# l = [1,2,-3,4,5, -1 ,-4 -3 ]
# print("pPrint Positive Numbers")

# for i in l:
#     if i >= 0:
#         print(i)

# print("Print Negative Numbers")
# for i in l:
#     if i < 0:
#         print(i)


l = [12,2,43,56]
sum = 0
for i in l:
    sum = sum + i

print(sum/len(l))

