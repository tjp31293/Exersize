#1. Write a Python program to find the sum of all elements in a list.
x = [100,200,300,400,500]
sum_no = 0
for i in x:
    sum_no = sum_no+i
print(sum_no)
print("-----------------------------------")

#2. Write a Python program to find the maximum and minimum elements in a list.
x = [100,200,300,400,500]
max_x = max(x)
min_x = min(x)
print(max_x)
print(min_x)
print("-----------------------------------")

#3. Write a Python program to remove duplicates from a list.
x = [100,200,300,500,400,100,50,10,1000,200]
x_set = set(x)
print(list(x_set))
print("-----------------------------------")

#4. Write a Python program to check if a list is sorted in ascending order.
x = [11,76,45,89,56,15,80,14,20,99]
x_copy = sorted(x)
print(x)
print(x_copy)
if x==x_copy:
    print("Sorted")
else:
    print("Not Sorted")
print("-----------------------------------")

#5. Write a Python program to find the second largest element in a list.
x = [100,200,300,400,5000,50,10,1000]
x.sort()
print(x)
s_largest = x[-2]
print("maximum element in list :=>", s_largest)
print("-----------------------------------")

#6. Write a Python program to sort a list of strings in alphabetical order.
str = ['dfg','abc','Abc','gty','zza']
sorted_list = sorted(str)
print(sorted_list)
print("-----------------------------------")

#7. Write a Python program to find the common elements between two lists.
x = [10,50,30,20,400,330,40]
x1 = [40,70,80,90,100,400,10]
set_x = set(x)
set_x1 = set(x1)
res = set_x.intersection(set_x1)
print(list(res))
print("-----------------------------------")

#8. Write a Python program to remove the nth occurrence of an element from a list.
x = [40,70,80,90,100,400,10]
n = 3
del(x[n])
print(x)
print("-----------------------------------")

#9. Write a Python program to find the difference between two lists.
first_list = [4, 9, 2, 3]
second_list = [4, 0, 1]
set1 = set(first_list)
set2 = set(second_list)
diff_bet = set1.difference(set2)
print(list(diff_bet))
print("-----------------------------------")

#10. Write a Python program to remove the elements of a list that are divisible by 3.
li = [6,3,6,1,9,8]
ele = lambda num:num%3!=0
print(list(filter(ele,li)))
print("-----------------------------------")