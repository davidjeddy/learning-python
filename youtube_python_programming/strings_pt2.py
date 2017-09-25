import random
import sys
import os

long_string = "I'll catch you in you fall - The Floor"

print(long_string[0:4])

print(long_string[-5:])

print(long_string[:-5])

print(long_string[:4] + " be there")

print("%c is my %s letter and number %d is number is %.5f" % ("X", "favorite", 1, .14))

print(long_string.capitalize())

print(long_string.find("floor"))

print(long_string.isalpha())

print(long_string.isnumeric())

print(len(long_string))

print(long_string.replace("Floor", "Ground"))

print(long_string.strip())

print(long_string.split(" "))