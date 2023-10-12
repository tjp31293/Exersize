#1. Write a Python program to print all the even numbers between 1 and 20 except for the number 10 using a for loop and continue statement.
for i in range(21):
    if i%2==0:
        if i ==10:
            continue
        print(i)
print('---------------------------------------')

#2. Write a Python program to print the elements of a list skipping the negative numbers using a while loop and continue statement.
l = [10,20,-30,40,-50,0,-60,70,80,90]
x = 0
while x < len(l):
  if l[x] < 0:
    l.remove(l[x])
    continue
  x += 1
print(l)
print('---------------------------------------')

#3. Write a Python program to print the first 10 multiples of 3 except for the number 9 using a for loop and continue statement.
for i in range(31):
    if i%3==0:
        if i == 9:
            continue
        print(i)
print('-------------------------------------')

#4. Write a Python program to iterate over a string and print only the consonants using a for loop and continue statement.
l = ['a','e','i','o','u','A','E','I','O','U']
str_name = "Apple"
con_l =[]
for i in str_name:
        for j in l:
            if i in j:
                con_l.append(i)
                continue
print(con_l)
print('----------------------------------')

#5. Write a Python program to print the elements of a list skipping the even numbers using a while loop and continue statement.
no = [1,2,3,4,5,6,7,8,9,10,13,16,15]
i = 0
while i<len(no):
    if no[i]%2==0:
        no.remove(no[i])
        continue
    i=i+1
print(no)
print('-----------------')

#6. Write a Python program to find the sum of all numbers between 1 and 100, excluding the multiples of 5 using a for loop and continue statement.
for i in range(100):
    if i%5==0:
        continue
    print(i, end=" ")
print('-----------------')

#7. Write a Python program to print the uppercase letters in a string using a while loop and continue statement.
i = 0
while i < len(str_name):
     is_lower = str_name[i].islower()
     if (is_lower):
         i = i + 1
         continue
     print(str_name[i],end=" ")
     i = i+1
print('------------------------')
#8. Write a Python program to print the elements of a list skipping the elements divisible by 3 using a for loop and continue statement.
no = [1,2,3,4,5,6,7,8,9,10,13,16,15]
i = 0
while i<len(no):
    if no[i]%3==0:
        no.remove(no[i])
        continue
    i=i+1
print(no,end="")
print('-------------------------------')

#9. Write a Python program to iterate over a list of tuples and print only the tuples with a specific condition using a while loop and continue statement.
#10. Write a Python program to print the numbers from 1 to 50, skipping the multiples of 7 using a for loop and continue statement.
no = [1,28,3,4,5,6,7,8,9,10,14,16,15,21]

i = 0
while i<len(no):
    if no[i]%7==0:
        no.remove(no[i])
        continue
    i=i+1
print(no,end="")
print()