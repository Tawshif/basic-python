import os
import random
import sys

""" math functions """
# print("hello Python World l")
# name = "anik"
# print(name)
# print("5 + 2 =", 5+2)
# print("5 - 2 =", 5-2)
# print("5 / 2 =", 5/2)
# print("5 * 2 =", 5*2)
# print("5 % 2 =", 5%2)
# print("5 ** 2 =", 5**2)
# print("5 // 2 =", 5//2)
# quote = "\" Always remember you are unique "
# multiline_quote = '''  just
# like every one else '''
# print("%s %s %s " %('i like the quote', quote, multiline_quote))
# print('\n' * 5)
# print("I don't like ", end="")
# print("newlines")

""" Lists """

# grocery_list = ['Juice','Tomatoes','Potatoes','Bananas']

# grocery_list[0] = "Green Juice"
# print("first item", grocery_list[0])
# print(grocery_list[1:3])
# other_events = ['car wash', 'pickup kids', 'cash checks']
# todo_list = [other_events, grocery_list]

# print(todo_list)
# print((todo_list[1][1]))
# grocery_list.append('onions')
# print(todo_list)
# grocery_list.insert(1, 'Alu')
# print(grocery_list)
# grocery_list.remove('Alu')
# print(grocery_list)
# grocery_list.sort()
# print(grocery_list)
# grocery_list.reverse()
# print(grocery_list)
# del grocery_list[4]
# print(grocery_list)
# todo_list2 = other_events + grocery_list
# print(todo_list2)
# print(len(todo_list2))
# print(max(todo_list2))
# print(min(todo_list2))

""" tuples """

pi_tuple = (3, 1, 4, 5, 6, 9)

"""
tuples are sarrounded by () and created normally for values that are generally not changed
to change tuples the below process is applied.
convert a tuple into list and hange the data
then change the list into tuple
"""
# new_tuple = list(pi_tuple)
# print(new_tuple)
# new_tuple.append(11)
# new_tuple.extend([12,13,14])
# print(new_tuple)
# new_list = tuple(new_tuple)
# print(new_list)
# print(len(new_list))
# print(min(new_list))
# print(max(new_list))

# DICTIONARY or MAP -------------
# Made up of values with a unique key for each value
# Similar to lists, but you can't join dicts with a +

super_villains = {'Fiddler': 'Isaac Bowin',
                  'Captain Cold': 'Leonard Snart',
                  'Weather Wizard': 'Mark Mardon',
                  'Mirror Master': 'Sam Scudder',
                  'Pied Piper': 'Thomas Peterson'}

print(super_villains['Captain Cold'])

del super_villains['Fiddler']
print(super_villains)

super_villains['Pied Piper'] = 'Hartley Rathaway'

print(len(super_villains))

print(super_villains.get("Pied Piper"))

print(super_villains.keys())

print(super_villains.values())
