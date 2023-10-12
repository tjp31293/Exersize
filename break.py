#1. Write a Python program to find the first occurrence of a number in a list using a for loop and break statement.
l = [100,200,300,400,500]
for i in l:
    x = l[0]
    break
print(x)
print('-----------------------------------')

#2. Write a Python program to search for a specific element in a list using a while loop and break statement.
l = [100,200,300,400,500]
l_len = len(l)
i = 0
while i<l_len:
    if l[i]==200:
        print(l[i])
        break
    i=i+1
print("-----------------------")

#3. Write a Python program to find the prime numbers between 1 and 100 using a for loop and break statement.
prime_list = []
for i in range(1, 101):
    if i == 0 or i == 1:
        continue
    else:
        for j in range(2, int(i/2)+1):
            if i % j == 0:
                break
        else:
            prime_list.append(i)

print(prime_list)
print("-----------------------")

#4. Write a Python program to check if a number is present in a list using a while loop and break statement.
l = [100,200,300,400,500]
s_ele = 300
i=0
while i<len(l):
    if s_ele == l[i]:
        print(s_ele)
        break
    i=i+1
print('-------------------------------')

#5. Write a Python program to find the largest palindrome number in a given range using a for loop and break statement.
def ispalindrome(num):
    return str(num) == str(num)[::-1]

for i in range(200,0,-1):
    if ispalindrome(i):
        largest = i
        print(largest)
        break
print('-------------------------------')

#6. Write a Python program to find the first negative number in a list using a while loop and break statement.
ele = [33,34,-20,45,-60,32,-12]
i=0
while i<len(ele):
    if ele[i]<0:
        print(ele[i])
        break
    i = i+1
print("--------------------------")

#7. Write a Python program to print the elements of a list until a specific condition is met using a for loop and break statement.
test_list = [1, 4, 6, 8, 9, 10, 7]
n=8
for i in test_list:
    print(i)
    if i==8:
        break
print('--------------------------------------')

#8. Write a Python program to search for a specific character in a string using a while loop and break statement.
str_name = 'Tejashree'
i = 0
search_ele = 'a'
while i <len(str_name):
    if search_ele in str_name[i]:
        print(search_ele)
        break
    i = i+1
print('--------------------------------------')

#9. Write a Python program to find the first occurrence of a vowel in a string using a for loop and break statement.
vowels =['a','e','i','o','u','A','E','I','O','U']
result = ""
input_string='apple'
for char in input_string:
    if char in vowels:
        result = str(char)
        break
print(result)
print('--------------------------------------')

#10. Write a Python program to find the index of the first occurrence of a substring in a string using a while loop and break statement.
