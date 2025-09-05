
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

# Q2 - Mean of List elements?

# l = [12,2,43,56]
# sum = 0
# for i in l:
#     sum = sum + i

# print(sum/len(l))


# Q3  - Find the greatest element and print its index too?

# l = [12,2,43,56,25 , 931]

# largest = l[0]
# index = 0
# for i in range(len(l)):
#     if l[i] > largest:
#       largest = l[i]
#       index = i

# print(f"your largest number is {largest} at the index {index}")   


# Q4 Find the second greatest element?

# l = [12,2,43,56,25,931]

# largest = l[0]
# sec_largest = l[0] 

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i 
# print(f"Your largest value is {largest} and second {sec_largest}")

# Q5 Check if List is sorted or not.



# a = [12,2,43,56,25,931]
a = [1 ,2 ,3,4 ,5]
for i in range(len(a)-1):
    if a[i] < a[i+1]:
        continue
    else:
        print("your number is not sorted")
        break
else:
    print("your number is sorted")

