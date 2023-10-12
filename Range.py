#Range Exercises
#1. Write a Python program to iterate over a range of numbers and print them.
for i in range(6):
    print(i)
print('------------------------------------')

#2. Write a Python program to find the sum of all numbers in a range.
sum=0
for i in range(6):
    sum = sum+i
print(sum)
print('------------------------------------')

#3. Write a Python program to print all even numbers in a given range.
for i in range(20):
    if i%2==0:
        print(i)
print('------------------------------------')

#4. Write a Python program to print all odd numbers in a given range.
for i in range(20):
    if i%2!=0:
        print(i)
print('------------------------------------')

#5. Write a Python program to find the average of all numbers in a range.
sum=0
n=10
for i in range(n+1):
    sum = sum+i
avg = sum/n
print(avg)
print("-------------------")

#6. Write a Python program to check if a number is present in a given range.
n =5
if n in range(11):
    print("Element is Present")
else:
    print("Not Present")
print("-------------------")

#7. Write a Python program to reverse a range of numbers and print them.
for i in reversed(range(11)):
    print(i)
print("-------------------------------")

#8. Write a Python program to find the product of all numbers in a range.
total = 1
for i in range(1,10):
    total = total * i
    print(total)
print("-------------------------------")

#9. Write a Python program to print the squares of all numbers in a range.
for i in range(1,10):
    n = i * i
    print(n)
print("-------------------------------")

#10. Write a Python program to print the cube of all numbers in a range.
for i in range(1,10):
    n = i * i * i
    print(n)
print("-------------------------------")