#While Loop Exercises:
#1. Write a Python program to print the numbers from 1 to 10 using a while loop.
i = 1
while i<=10:
    print(i)
    i = i+1
print('=====================================')

#2. Write a Python program to calculate the sum of all numbers from 1 to 100 using a while loop.
i =1
sum = 0
while i <=100:
    sum = sum +i
    i = i+1
print(sum)
print('-------------------------------------')

#3. Write a Python program to find the factorial of a number using a while loop.
num =5
fact = 1
i =1
while i<=num:
    fact = fact*i
    i = i+1
print("Factorial of",num, "is =>",fact)
print('---------------------------------------')

#4. Write a Python program to print all the even numbers between 1 and 50 using a while loop.
i = 1
while i<=50:
    if i%2==0:
        print(i)
    i = i+1
print('--------------------------------------')

#5. Write a Python program to iterate over a string and print each character using a while loop.
str_name = 'hello good morning'
str_len = len(str_name)
i = 0
while i<str_len:
    letter = str_name[i]
    print(letter)
    i = i+1
print('------------------------------------------')

#6. Write a Python program to iterate over a list of tuples and print each element using a while loop.
l_name = [(1,2,3),(4,5),(6,7,8,9)]
i = 0
x=0
l_length = len(l_name)
while i<l_length:
        t1 = l_name[i]
        for x in t1:
            print(x)
        i=i+1
print('----------------------------------')

#7. Write a Python program to find the largest element in a list using a while loop.
myList = [2,4,6,8,10,12,14,16,18]
demo_max  = myList[0]
i= 0
while i < len(myList):
    print(max(myList))
    i = i+1
    break
print('--------------------------------')

#8. Write a Python program to check if all elements in a list are even using a while loop.
myList = [2,4,6,8,10,12,14,16,18]
flag = 0
index = 0
while index < len(myList):
    element = myList[index]
    if element % 2 != 0:
        flag = 1
        break
    index += 1
if(flag == 1):
    print("Not Even List")
else:
    print("Even List")
print('-----------------------------')

#9. Write a Python program to find the common elements between two lists using a while loop.
x = [1,2,3,4,5]
y = [2,5,6,7,8,9]
i = 0
result = []
while i < len(x):

  j = 0
  while j < len(y):
    if x[i] == y[j]:
        result.append(x[i])
    j = j + 1
  i = i + 1
print(result)
print('-----------------------------')

#10. Write a Python program to calculate the sum of the digits of a number using a while loop.
number = 12345
sum = 0
while number>0:
    reminder  = number%10
    sum = sum +reminder
    number = number//10
print(sum)