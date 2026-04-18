import random
import sys
import os

grocery_list = ['Juice', 'Tomatoes', 'Potatoes']

print('First item is: ', grocery_list[0])

grocery_list[0] = "Green Juice"

print('First item is: ', grocery_list[0])

# up to but no include last id'd item
print('First item is: ', grocery_list[1:3])

other_events = ['Wash Cart', 'Pick up', 'Get check']

todo = [other_events, grocery_list]

print(todo)

print(todo[1][1])

grocery_list.append("Onion")
print(grocery_list)

grocery_list.insert(1, "Pickle")
print(grocery_list)

grocery_list.remove("Pickle")

grocery_list.sort()
grocery_list.reverse()

del grocery_list[3]
print(grocery_list)

# combine lists together
todo2 = grocery_list + todo
print(len(todo2))

print(max(todo))

print(min(todo))