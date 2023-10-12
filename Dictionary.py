#1. Write a Python program to iterate over a dictionary and print its keys and values.
dt =  {1:'one',2:'Two',3:'Three'}
for key,value in dt.items():
        print(key,value)
print("-----------------------------")

#2. Write a Python program to check if a key exists in a dictionary.
dt = {'a': 'apple', 'b': 'ball', 'c': 'cat'}
if 'b' in dt.keys():
    print("Key Exist")
print("-----------------------------")

#3. Write a Python program to get the value associated with a key in a dictionary.
dt = {'a': 'apple', 'b': 'ball', 'c': 'cat'}
x = dt.get('a')
print(x)
print("-----------------------------")

#4. Write a Python program to remove a key from a dictionary.
dt = {'a': 'apple', 'b': 'ball', 'c': 'cat'}
del dt['a']
print(dt)
print("-----------------------------")

#5. Write a Python program to sort a dictionary by its values.
a ={1:'one',3:'Two',2:'Three'}
sorted_dict  = sorted(a.values())
print(sorted_dict)
print("-----------------------------")

#6. Write a Python program to merge two dictionaries.
dict_1 ={1:'a',2:'b',3:'c'}
dict_2 ={2:'d',4:'e',5:'f'}
dict_3 = dict_1 | dict_2
print(dict_3)
dict_1.update(dict_2)
print(dict_1)
print("-----------------------------")

#7. Write a Python program to count the frequency of each element in a dictionary.
d = {1:'D',2:'C', 3:'D', 4:'E',5:'C'}
count = {}
for item in d.values():
    if item in count:
        count[item] = count[item]+1
    else:
        count[item] = 1
for keys,value in count.items():
    print(keys,"->",value)
print("-----------------------------")

#8. Write a Python program to find the length of a dictionary.
d = {1:'D',2:'C',3:'D', 4:'E',5:'C'}
print(len(d))
print("-----------------------------")

#9. Write a Python program to check if a dictionary is empty.
d = {}
a_len = len(d)
if a_len == 0:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")
print("-----------------------------")

#10. Write a Python program to find the keys with the maximum and minimum values in a dictionary.
d = {1:'D',2:'C',3:'D',4:'E',5:'C',6:'a',7:'p'}
v = d.values()
max_val = max(v)
min_val = min(v)
print("Maximum value :=>",max_val)
print("Minimum value :=>",min_val)