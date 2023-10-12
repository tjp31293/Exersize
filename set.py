#1. Write a Python program to find the union of two sets.
first_set = {4, 9, 2, 3,1}
second_set = {4, 0, 1}
print(first_set.union(second_set))
print("------------------------------------------")

#2. Write a Python program to find the intersection of two sets.
first_set = {4, 9, 2, 3,1}
second_set = {4, 0, 1}
print(first_set.intersection(second_set))
print("------------------------------------------")

#3. Write a Python program to check if a set is a subset of another set.
first_set = {4, 9, 2, 3,1}
second_set = {4,1}
print(second_set.issubset(first_set))
print("------------------------------------------")

#4. Write a Python program to remove duplicate elements from a set.
set1 = {22,34,23,56,75,22,78,34}
print(set1)
print("------------------------------------------")

#5. Write a Python program to add an element to a set.
set1 = {34, 22, 23, 56, 75, 78}
set1.add(44)
print(set1)
print("------------------------------------------")

#6. Write a Python program to remove an element from a set.
set1 = {34, 22, 23, 56, 75, 44, 78}
set1.remove(44)
print(set1)
set1.pop()
print(set1)
print("---------------------------------------")

#7. Write a Python program to find the difference between two sets.
set1 = {34, 22, 23, 56, 75, 44, 78}
set2 = {22, 23, 56, 75, 78}
print(set1.difference(set2))
print("---------------------------------------")

#8. Write a Python program to check if two sets are disjoint.
set1 = {34, 22, 23, 56, 75, 44, 78}
set2 = {10,11,12,13,14}
print(set1.isdisjoint(set2))
print("---------------------------------------")

#9. Write a Python program to find the symmetric difference between two sets.
set1 = {34, 22, 23, 56, 75, 44, 78}
set2 = {22, 23, 56, 75, 78}
print(set1.symmetric_difference(set2))
print("---------------------------------------")

#10. Write a Python program to check if a set is empty.
a = {}
l = len(a)
if l == 0:
    print("Set is Empty")
else:
    print("Set is Not Empty")