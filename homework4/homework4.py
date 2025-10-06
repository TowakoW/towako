# Lists
# list operations
foods = ['cake', 'cookie', 'toast', 'pear', 'chocolate']
print(foods[1])
print(foods[-1])
foods.append('cracker')
print(foods)
foods.insert(0, 'apple')
print(foods)
# foods.remove(2)
#Traceback (most recent call last):       
#   File "<stdin>", line 1, in <module>    
#     import platform
# ValueError: list.remove(x): x not in list
del(foods[2])
foods
# used a different simplet approach
len(foods)
for food in foods:
    caps = food[0].upper()
    rest = food[1:]
    print(caps + rest)
# File "<stdin>-15", line 2
#     return food.upper()
#     ^^^^^^^^^^^^^^^^^^^
# SyntaxError: 'return' outside function
# printing all as caps - slicing and adding
foods[0:5:4]
def potatoes(foods):
    if 'potato' in foods:
        print('A potato!')
    else:
        print('No potato!')
potatoes(foods)

# 3.2 slicing and striding
import numpy as np
import copy
numbers = np.arange(0,21)
numbers

#1
def get_first_15(numbers):
    return numbers[0:16]
get_first_15(numbers)
fifteen_eyy = get_first_15(numbers)
#2
def get_every_5th(fifteen_eyy):
    return fifteen_eyy[::5]
fifths = get_every_5th(fifteen_eyy)
# >>> def get_every_5th(fifteen_eyy):
# ...     print(fifteen_eyy[0:15:5])
# ...
# >>> fifths = get_every_5th(fifteen_eyy)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#              ^^^^^^
#   File "<stdin>", line 2, in get_every_5th
#     import sys

# TypeError: 'NoneType' object is not subscriptable
# use 'return' instead of 'print'
fifths
# 3
def reverse_and_stride(fifths):
    return fifths[::-3]
final = reverse_and_stride(fifths)
final

# 3.3 nested lists
# 3.3.1 nested list operations
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
numberss = [list_1, list_2, list_3]
numberss
#1 
print(numberss[2])
#2
print(numberss[1][1])
#3
numberss.append([10, 11, 12])
numberss
#4
def sum_nested(numberss):
    nest_rows = []
    for row in numberss:
        nest_rows.append(sum(row))
    return np.array(nest_rows)
sum_nested(numberss)

# 3.4 create a 5x5 list
def fivefunction():
    fivefive = []
    value = 1
    for i in range(5):
        rows = []
        for nums in range(5):
            rows.append(value)
            value += 1
        fivefive.append(rows)
    return fivefive
fivex5list = fivefunction()
fivex5list
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^^
# NameError: name 'fivefive' is not defined
# UnboundLocalError: cannot access local variable 'value' where it is not associated with a value
# >>> fivefunction(1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
# TypeError: fivefunction() takes 0 positional arguments but 1 was given 
# debugging, pain.
# 1
# def questionthree(listy):
#     for i in range(len(listy)):
#       for nums in range(len(listy[i])):
#         if listy[i][nums] % 3 == 0:
#          listy[i][nums] = '?'
#     return listy
# nothrees_allowed = questionthree(fivex5list)

#  File "<stdin>", line 3
#     if fivex5list[1][2][3][4][5] % 3 = 0:
#        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
# >>>             fivex5list = '?'
#   File "<stdin>", line 1
#     fivex5list = '?'
# IndentationError: unexpected indent
# did == instead of =
#   File "<stdin>", line 1
#     fivex5list = '?'
# IndentationError: unexpected indent
# >>> nothrees_allowed = fivex5list
# >>> 
# >>> for i in range(len(fivex5list)):
# ...     for nums in range(len(fivex5list[1][2][3][4][5])):
# ...         if fivex5list[1][2][3][4][5] % 3 == 0:
# ...             fivex5list = '?'
# ...
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
#     import sys

# TypeError: 'int' object is not subscriptable
# >>> nothrees_allowed = fivex5list
# >>> for i in range(len(fivex5list)):
# ...     for nums in range(len(fivex5list[i])):
# ...         if fivex5list[1:5] % 3 == 0:
# ...          fivex5list = '?'
# ...
# Traceback (most recent call last):
#   File "<stdin>", line 3, in <module>
#     if fivex5list[1:5] % 3 == 0:
#        ~~~~~~~~~~~~~~~~^~~
# TypeError: unsupported operand type(s) for %: 'list' and 'int'
# >>> def questionthree(listy):
# ...     for i in range(len(listy)):
# ...       for nums in range(len(listy[i])):
# ...         if listy[i][nums] % 3 == 0:
# ...          listy[i][nums] = '?'
# ...     return listy
# ...
# >>> nothrees_allowed = questionthree(fivex5list)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform

#   File "<stdin>", line 4, in questionthree
#     if sys.platform != "win32":
#                ^^^^^^^^^^^^^^^^
# TypeError: not all arguments converted during string formatting
# debugging?
def questionthree(listy):
    new_list = [row.copy() for row in listy]
    for i in range(len(new_list)):
        for nums in range(len(new_list[i])):
            val = new_list[i][nums]
            # if new_list[i][nums] % 3 == 0:
            if isinstance(val, int) and val %3 ==0:
                new_list[i][nums] = '?'
    return new_list

nothrees_allowed = questionthree(fivex5list)
nothrees_allowed

#2
def questionno(listy):
    # mutate the provided list in-place
    for i in range(len(listy)):
        for nums in range(len(listy[i])):
            val = listy[i][nums]
            # only operate on integers
            if isinstance(val, int) and val % 3 != 0:
                listy[i][nums] = '?'
    return listy

threez = questionno(fivex5list)
threez
# >>> def questionno(listy):
# ...     for i in range(len(listy)):
# ...       for nums in range(len(listy[i])):
# ...         if listy[i][nums] % 3 != 0:
# ...          listy[i][nums] = '?'
# ...     return listy
# ...
# >>> threez = questionno(fivex5list)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#              ^^^^^^
#   File "<stdin>", line 4, in questionno
#     if sys.platform != "win32":
#                ^^^^^^^^^^^^^^^^
# TypeError: not all arguments converted during string formatting
# worked after restarting file, I am assumng #1 and #2 are interfering with eachother.
# further debugging with powershell/copilot assitance in order to submit the homework - doesn't show up on gitbash when called.
# first problem was altering the dataset, changing to make a copy insead of altering it so problem 2 also runs

# 4 dictionaries
ages = {
   'Katie':30,
   'Mariam': 42,
   'Safia': 25,
   'Mira': 48
}
#1
print(ages['Katie'])
ages['Mira'] = 100
print(ages)
# >>> print(ages['Katie'])
# 30
# >>> ages('Mira') = 100
#   File "<stdin>", line 1
#     ages('Mira') = 100
#     ^^^^^^^^^^^^
# SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
# >>>
# >>> ages('Mira') == 100
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^^^^^^
# TypeError: 'dict' object is not callable
#3
ages['Milana'] = 52
print(ages)
# >>> ages.append['Milana':52]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^^^^^
# AttributeError: 'dict' object has no attribute 'append'
# 4
del(ages['Mariam'])
print(ages)
#5
# def nameage(ages):
#     for i in ages:
#       print([ages, i])
# nameage(ages)

for name, age in ages.items():
   print(f"{name}:{age}")
# >>> nameage(ages)
# {'Katie': 30, 'Safia': 25, 'Mira': 100, 'Milana': 52}
# >>>
# >>> def nameage(ages):
# ...     for i in ages:
# ...       print([ages, ages.item[0]])
# ...
# >>> nameage(ages)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^^^^^^^
#   File "<stdin>", line 3, in nameage
#     print([ages, ages.item[0]])
#                  ^^^^^^^^^
# AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'? 
# >>> def nameage(ages):
# ...     for i in ages:
# ...       print([ages, i.item[0]])
# ...
# >>> nameage(ages)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^^^^^^^
#   File "<stdin>", line 3, in nameage
#     print([ages, i.item[0]])
#                  ^^^^^^
# AttributeError: 'str' object has no attribute 'item'
# taking a break, will come back later...or not.
# adding (f"")
