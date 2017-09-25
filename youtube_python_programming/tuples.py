import random
import sys
import os

# Tuples, unlike lists, can not be changes after creation; mainly a memory assignment difference.

# Can change tuple to list and back very easily
pi_tuple = (3,1,4,1,5,9)
new_list = list(pi_tuple)
new_list = tuple(new_list)

# list / array operations work on tuples
print(len(pi_tuple))
print(min(pi_tuple))
print(max(pi_tuple))