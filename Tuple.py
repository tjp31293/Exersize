#1. Write a Python program to find the length of a tuple.
t = (1,2,3,4,5,6,7,8)
len_t = len(t)
print("length of tuple is",len_t)
print("----------------------------------")

#2. Write a Python program to concatenate two tuples.
tuple1 = (1,2,3,4,5,6,7,8)
tuple2 = (2,4,6,8,10)
result = tuple1 + tuple2
print(result)
print("----------------------------------")


#3. Write a Python program to convert a tuple to a list.
tuple1 = (23,45,67,89,11,54)
my_list = list(tuple1)
print(my_list)
print("-----------------------------------")

#4. Write a Python program to find the index of an element in a tuple.
a = (23,45,67,89,90,34,56)
print("Index Number :",a.index(89))
print("-----------------------------------")

#5. Write a Python program to check if an element exists in a tuple.
a = (23,45,67,89,90,34,56)
n = 67
if n in a:
    print("Element is present in tuple")
else:
    print("Element is not present")
print("-----------------------------------")


#6. Write a Python program to count the number of occurrences of an element in a tuple.
t = ('a','E','i','o','u','e')
result = t.count('e')
print(result)
print("---------------------------------")

#7. Write a Python program to find the maximum and minimum elements in a tuple.
t = (300,400,20,600,880,220)
print("Maximum number is :=>", max(t))
print("Minimum number is :=>", min(t))
print("---------------------------------")

#8. Write a Python program to reverse a tuple.
my_tuple = (1,4,6,3,'hello','hi')
my_tuple = my_tuple[::-1]
print(my_tuple)
print("----------------------------------")

#9. Write a Python program to check if all elements in a tuple are the same.
#l = ('apple','apple','apple','apple')
l = (20,21,22,23,24)
r_l = l[::-1]
if l == r_l:
    print("Elements are same")
else:
    print("Elements are not same")
print("--------------------------------")

#10. Write a Python program to create a new tuple with the elements from two existing tuples.
l = ('apple','apple','apple','apple')
l1 = (20,21,22,23,24)
new_t = l + l1
print(new_t)
print("--------------------------------")

##11 Get input from user (tuple list set)
'''values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
set = set(list)
print('List : ',list)
print('Tuple : ',tuple)
print('Set : ',set)'''