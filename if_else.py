#If-Else Loop Exercises:50
#1. Write a Python program to check if a number is positive, negative, or zero.
num = 4
if num>0:
    print("Number is positive")
elif num==0:
    print("Number is Zero")
else:
    print("Number is negative")
print("-----------------------------------------------")

#2. Write a Python program to check if a number is even or odd.
num = 5
if num%2==0:
    print("number is Even")
else:
    print("number is Odd")
print("-----------------------------------------------")

#3. Write a Python program to check if a year is a leap year or not.
year = 2018
if((year % 400 == 0) or (year % 100 != 0) and  (year % 4 == 0)):
    print("Given year is leap year")
else:
    print("Not leap year")
print("-----------------------------------------------")

#4. Write a Python program to find the maximum of three numbers using if-else.
num1 = 12
num2 = 6
num3 = 9
if num1>=num2 and num1>=num3:
    print("First number is greater:=>",num1)
elif num2>=num1 and num2>=num3:
    print("Second number is greater:=>",num2)
else:
    print("Third number is greater:=>",num3)
print("-----------------------------------------------")

#5. Write a Python program to check if a number is prime.
num = 17
flag = False
if num==1:
    print("Not prime number")
elif num>1:
    for i in range(2,num):
        if (num%i)==0:
            flag = True
            break
    if flag:
        print("Number is not prime number")
    else:
        print("Number is Prime")
print("-----------------------------------------------")

#6. Write a Python program to check if a number is divisible by both 3 and 5.
num = 15
if (num%3==0) and (num%5==0):
    print("number is divisible by both 3 & 5")
else:
    print("Number is not divisible by 3 & 5")
print("-----------------------------------------------")

#7. Write a Python program to check if a character is a vowel or consonant.
vowels = "aeiouAEIOU"
char = 'A'
if vowels.find(char)==-1:
    print("The character",char," is Not vowels")
else:
    print("The character", char, "is vowels")
print("-----------------------------------------------")

#8. Write a Python program to check if a given string is a palindrome using if-else.
str_name = 'ABCcba'
str1 = str_name.lower()
if str1 == str1[::-1]:
    print("The string", str_name, " is palindrom")
else:
    print("The string is not palindrom")
print("-----------------------------------------------")

#9. Write a Python program to determine the largest among three numbers using nested if-else.
a=10
b=34
c=50
if a>b:
    if a>c:
        greater=a
    else:
        greater=c
else:
    if b>c:
        greater = b
    else:
        greater = c
print("Greater :=>",greater)
print("-----------------------------------------------")

#10. Write a Python program to check if a triangle is equilateral, isosceles, or scalene based on its side lengths using if-else.
x=10
y=10
z=10
if x+y>=z and y+z>=x and z+x>=y:
    if x == y == z:
        print("Equivalent Triangle")
    elif x==y or y==z or z==x:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Triangle is not possible")

print("-----------------------------------------------")