# IF ELSE

# a = 13

# if a > 12 and a < 16:
#     print("I will do this task" )
# else:
#     print ("Run here")

# money = int(input("Please provide me money"))

# if  money == 10:
#     print("I will have choco bar")
# elif money == 20:
#     print("I will have cone")
# else:
#     print ("I will have mango dolly")

    # Questions (Problem Solving)
# Q1. Accept two numbers and print the greatest between them.

# num1 = int(input("Please enter your 1st number"))
# num2 = int(input("Please enter your 2nd number"))

# if num1 > num2:
#     print(f"{num1} is greater then {num2}")
# elif num2 > num1:
#      print(f"{num2} is greater then {num1}")
# else:
#     print("Both are equal numebrs")

#  2 PRoblem Solving 
# Accept the gender from the user as char and print the 
#  respective greeting message
#  Ex - Good Morning Sir (on the basis of gender)

# gender = input("Please tell your gender :-")
# male = "male"
# female = "female"
# if gender == male or gender == 'm':
#     print ("Greeting message for male")
# elif gender == female or gender == 'f':
#     print ("Greeting message for female")
# else:
#   print ("Unknow gender")


#  3 Problem Solving 

#  Accept an integer and check whether it is an even number or odd.

# num= int(input("This is odd number :-"))

# if num%2 == 0:
#     print ("even number")
# else:
#     print("odd number")

# Q4. Accept name and age from the user. Check if the user is a valid voter or not.

# name = input("please enter your name :-")
# age = int(input("Please tell your age"))

# if age >= 18 :
#     print(f"You are valid voter :- {name}")
# elif age <= 17:
#     print(f"You can vote after 1 year {name}")
# else:
#       print(f"you are not valid voter {name}")

# Q5. Accept a year and check if it a leap year or not (google to find out what is a leap year)

# year = int(input("please tell me the years"))

# if year %100 == 0 and year%400 ==0:
#     print("It's leap century year")
# elif year %100 != year %4 ==0:
#     print("Not leap century year")
# else:
#     print("It's normal year")

# Q6 @ You cna also create if elif ladder using multiple conditions of
# elif.j
# @ For understanding solve this questionj
# @ take the input of temperature in celsiusX
# @ Below 0°C → "Freezing Cold b
# @ 0°C to 10°C → "Very Cold b
# @ 10°C to 20°C → "Cold b
# @ 20°C to 30°C → "Pleasant b
# @ 30°C to 40°C → "Hot b
# @ Above 40°C → "Very Hot " 

t = int(input("Please tell your temperature :-"))

if t < 0:
    print("Freezing cold")
elif t >= 0 and t <= 10:
    print("Very Cold")
elif t >= 10 and t <= 20:
    print("Cold")
elif t >= 20 and t <= 30:
    print("Pleasent")
elif t >= 30 and t <= 40:
    print("Hot")
else:
     print("very Hot")



