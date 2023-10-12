#For Loop Exercises:
#1. Write a Python program to print the numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)
print("---------------------------------------")

#2. Write a Python program to calculate the sum of all numbers in a list using a for loop.
x = [10,20,30,40,50]
sum = 0
for i in x:
        sum = sum  + i
print("Sum of numbers",sum)
print("-------------------")


#3. Write a Python program to find the factorial of a number using a for loop.
no=5
if(no == 0):
    print("factorial of 0 is 1")
elif (no < 0):
    print("Sorry factorial not exist for negative value")
factorial = 1
for i in range(1,no+1):
    factorial = factorial * i
print("factorial of",no,"is",factorial)
print("----------------------------")

#4. Write a Python program to print all the even numbers between 1 and 50 using a for loop.
for i in range(1,51):
    if i%2==0:
        print(i)
print('------------------------------------------')

#5. Write a Python program to iterate over a string and print each character using a for loop.
str_name ="hello good morning"
for val in str_name:
    print(val)
print('-------------------------------------------')
#6. Write a Python program to iterate over a list of tuples and print each element using a for loop.
l = [(1,2,3),(4,5),(6,7,8,9)]
for x in l:
    for y in x:
        print(y)
print("----------------------------------------")

#7. Write a Python program to find the largest element in a list using a for loop.
x = [2000,200,300,400,5000,50,10,1000]
max_x = x[0]
for i in x:
    if i>=max_x:
        print("max no is",i)
print("----------------------------------------")

#8. Write a Python program to check if all elements in a list are even using a for loop.
l_ele = [2,4,10,6,12,8,18,7]
new_l = []
for i in l_ele:
    if i%2==0:
        new_l.append(i)
print(new_l)
if len(new_l) == len(l_ele):
    print("all elements in a list are even")
else:
    print("all elements in a list are Not even")
print("----------------------------------------")

#9. Write a Python program to   find the common elements between two lists using a for loop.
list1 = [1,2,3,4,5]
list2 = [2,5,6,7,8,9]
result=[]
for ele in list1:
    if ele in list2:
        result.append(ele)
print(result)
print("----------------------------------------")

#10. Write a Python program to calculate the sum of the digits of a number using a for loop.
number = 12345
sum = 0
for digit in str(number):
    sum = sum + int(digit)

print(sum)