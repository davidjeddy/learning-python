import random
import sys
import os

# are values w/ a unique key
# can not join dictionaries together
super_villains = {'Fiddler': 'Isaac Bowin',
                  'Captain Cold': 'Leonard Snart',
                  'Weather Wizard': 'MArk Mardon',
                  'Mirror Master': 'Sam Scuddar',
                  'Pied Piper': 'Thomas Peterson'}

print(super_villains['Captain Cold'])

del super_villains['Fiddler']

super_villains['Pied Piper'] = 'Hartley Rathaway'

print(len(super_villains))

print(super_villains.get('Pied Piper'))

print(super_villains.keys())

print(super_villains.values())