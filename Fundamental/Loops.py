# In for loops we set some range funcitons which start form 0 then stop then steps (S,S,S) => Start , Stop , Steps

# for i in range (1, 20, 1):
#     print (i)

# n = int(input ("Which Table you want to print"))
# for i in range(n ,(n*10)+1 , n):
#     print (i);

# Strings for Loops
#  if we use string then it's index form zero but if we check lenght then it's start from 1 

# a = "Usama Teaches Programming in university"
# print (len(a))


# for i in range(len(a)):
#     print(a[i])


# Break in statement loops 

# for i in range (1 , 21):
#     if i == 15:
#         # break
#         continue
#     else:
#         print(i)


# Problem Solving 

# Q1 - Accept an integer and Print hello world n times 
# n = int(input("Enter your integar"))

# for i in range (1, n+1 ,1):
#     print("Hello world")

# Q2 - Print natural number up to n 

# n = int(input("Enter the numbers"))

# for i in range (1 , n+1 , 1):
#     print(i)

# Q3 - Reverse for loop. Print n to 1 

# n = int(input("Enter the numbers"))

# for i in range(n, 0 , -1):
#     print (i)

# Q4 - Take a number as input and print its table

# n = int(input("Which table you wnnt to print"))

# for i in range (1 ,11):
#     print (f"{n} * {i}  = {n*i}")

# Q5 - Sum up to n terms 

# n = int(input("Sum all number"))

# sum = 0

# for i in range(1,n+1,1):
#     sum = sum + i

#     print (f"your number is {sum}")

# Q6 - Factorial of a number

# n = int(input("Factorial of all number"))

# fact = 1

# for i in range(1,n+1,1):
#     fact = fact * i

#     print (f"your factorial number is {fact}")

# Q6 - Print the sum of all even & odd numbers in a range separately 

n = int(input("Tell me the number"))
even = 0
odd = 0

for i in range(1 , n+1):
    if i%2 == 0:
        even = even + i
    else:
        odd = odd + i 
            
    print(f"your even and odd sum are {even}, {odd}")

