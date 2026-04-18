import random
import sys
import os

print('Hello World')

# Comment

'''
Data types:
Numbers:
Strings:
Lists:
Tuples:
Dictionaries
'''

# string var
name = ' from David'
print(name)

# escaping special characters
quote = "Always remember, \"You are unique\"."

multi_line_quote = '''Also,
Git Gud.'''

new_string = quote + multi_line_quote
print(new_string)

# function argument substitution
print("%s %s %s" % ('I like the quote:', quote, multi_line_quote))

print('\n' * 5)
print('I dont like this ', end='')
print("second line")


