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

# n = int(input("Tell me the number"))
# even = 0
# odd = 0

# for i in range(1 , n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i 
            
#     print(f"your even and odd sum are {even}, {odd}")

# Q7 - Print all the factors of a number 

# n = int(input("Tell me the number"))
# for i in range(1 , n+1):
#     if n%i == 0:
#         print(i)

#  Q 8 -- Accept a number and check if it a perfect number or not.

#  A number whose sum of factors is equal to the number itself
#  Ex - 6 = 1, 2, 3 = 6 

# n = int(input("Check your number is perfect or not"))
# sum = 0
# for i in range(1 , n):
#     if n%i == 0:
#         sum = sum + i

# if sum == 0:
#     print("your number is perfect")
# else:
#   print("Not a perfect number")

# Q9 - Check wether the number is prime or not 

# n = int(input("Check your number is prime or not"))
# count = 0
# for i in range(1 , n+1):
#     if n%i == 0:
#         count = count + 1

# if count == 2:
#     print ("Your numbe is prime")
# else:
#     print ("Your numbe is not prime")

# For Loop for strings

# String concatination
# Q1 - Reverse a string without using in build functions.

# a = "USAMA"
# b = ""
# for i in range(len(a)-1 , -1 , -1):
     
#      b = b + a[i]

# print(b)

# Q2 - Check string is Pallindrome or not 

# a = "MADAM"
# b = ""
# print(len(a))

# for i in range(len(a)-1 , -1 , -1):
     
#      b = b + a[i]

# if b == a:
#      print("Your number is palindrom")
# else:
#      print("Your number is not palindrom")

# Q3 - Count all letters, digits, and special symbols from a given
# string

#  Given: str1 = "P@#yn26at^&i5ve"

#  Expected Outcome:

#  Total counts of chars, digits, and symbols

#  Chars = 8

#  Digits = 3

#  Symbol = 4

# a = "sskrinf1223n5@^&^!"
# char = 0
# digit = 0
# specialchr = 0


# for i in a:
#     if i.isalpha():
#        char += 1
#     elif i.isdigit():
#         digit += 1
#     else:
#         specialchr += 1
# print(f"your character is {char}\n your digit are {digit}\n your specialcharacter is {specialchr}")

        # While Loops Learning Start

# Q1 - Separate each digit of a number and print it on the new line

# n = int(input("Tel your number"))

# while n > 0:
#     print (n % 10)
#     n = n// 10

#  Q2- Accept a number and print its reverse

# a = int(input("Tel your number"))
# rev = 0
# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a//10

# print (rev)

# Q3 - Accept a number and check if it is a pallindromic number (If
# number and its reverse are equal?

# a = int(input("Tel your number"))
# copy = a
# rev = 0
# while a > 0:
#  rev = rev * 10 +  a % 10
#  a = a // 10

# if copy == rev:
#  print("This is your Palindromic number")
# else:
#   print("This is not your Palindromic number") 
 

# import random


# num = random.randint(1 , 10)
# tries = 0

# while True:
#     guess = int(input("Please guess your number between 1 to 10 :-"))

#     if num == guess:
#         tries += 1
#         print (f"you are right you guessed the number is {tries} tries")
#         break
#     elif num < guess:
#         tries += 1 
#         print ("Go a little lower")
#     elif num > guess:
#         tries += 1 
#         print ("Go a little higher")
#     else:
#         tries += 1
#         print ("sorry you are wrong")





def palindrom(st):
        revers = ""
        for i in range(len(st) -1 , -1, -1):
            revers = revers+ st[i]

        if revers == st:
                print("Palindrom")
        else:
                print("Not a Palindrom")
palindrom("NAMAN")   
palindrom("USAMA")                     