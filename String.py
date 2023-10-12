#1. Write a Python program to count the number of characters in a string.
str_name = 'Good Morning'
print("length of character:->",len(str_name))
print("---------------------------------------")
#=====================================================

#2. Write a Python program to reverse a string.
str_name = 'Good Morning'
rev_str = str_name[::-1]
print(rev_str)
print("---------------------------------------")
'''str_name = 'Good Morning'
rev_str = ''
x = len(str_name)
for char in range(-x,-1,-1):
    rev_str = rev_str + str_name[char]
print(rev_str)'''

#3) Write a Python program to check if a string is a palindrome.
str_name = 'AbCdcBa'
l_str = str_name.lower()
if l_str == l_str[::-1]:
    print("String is palindrome")
else:
    print("String is not Palindrome")
print("---------------------------------------")

#4) Write a Python program to remove all the vowels from a string.
demo_str = 'minImum'
list1 = ['a','e','i','o','u']
demo_str1 = demo_str.lower()
res = ''
for char in demo_str1:
    if char not in list1:
        res = res + char
print(res)
print("---------------------------------------")

#5). Write a Python program to find the first non-repeating character in a string.
input_string = 'minimum'
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] = char_count[char]+1
    else:
        char_count[char] = 1

key = [k for k, v in char_count.items() if v == 1][0]
print(key)
print("---------------------------------------")

#6. Write a Python program to capitalize the first letter of each word in a string.
str1 = "my name is jhon"
res = str1.title()
print(res)
print("---------------------------------------")


#7. Write a Python program to check if a string is an anagram of another string.
str1 = 'ABcd'
str2 = 'CdAb'
if len(str1) == len(str2):
    str1 = str1.lower()
    str2 = str2.lower()
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    if sorted_str1 == sorted_str2:
        print("String Anagram")
    else:
        print("String Not Anagram")
else:
    print("String not Anagram")
print("---------------------------------------")

#8. Write a Python program to find the most frequent character in a string.
input_string = 'minimum'
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] = char_count[char]+1
    else:
        char_count[char] = 1

res = max(char_count, key = char_count.get)
print(res)
print("---------------------------------------")

#9. Write a Python program to check if a string is a valid email address.
import re
def chk_email(s):
    pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    match = pattern.search(s)
    return match

s = 'abc@gmail.com'
match = chk_email(s)
if match:
    print("valid email id")
else:
    print("Invalid email id")
print("---------------------------------------")

#10. Write a Python program to find the length of the longest substring without repeating characters.
input_string = "geeksforgeeks"
a = set()
for i in input_string:
    a.add(i)
print(a)
a_len = len(a)
print("The length of the longest substring:=>",a_len)
print("---------------------------------------")

