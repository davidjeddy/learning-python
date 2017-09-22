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

# Arithmetic Operators
# + - * / % ** //
# add subtract multiply divide, modulus, exponent, floor

print("5 + 2 = ", 5+2)
print("5 - 2 = ", 5-2)
print("5 * 2 = ", 5*2)
print("5 / 2 = ", 5/2)
print("5 % 2 = ", 5%2)
print("5 ** 2 = ", 5**2)
print("5 // 2 = ", 5//2)

# Arithmetic order of operation is NOT adhered to.
# You MUST use parentheses
print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 =", (1 + 2 - 3) * 2)

# escaping special characters
quote = "Always remember, \"You are unique\"."

multi_line_quote = '''Also,
Git Gud.'''

new_string = quote + multi_line_quote
print(new_string)

# function argument substitution
print("%s %s %s" % ('I like the quote:', quote, multi_line_quote))