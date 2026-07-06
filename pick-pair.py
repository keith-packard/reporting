#!/usr/bin/python

import random

def get_names(filename):
    with open(filename, 'r') as file:
        l = map(str.strip, file.readlines());
        return list(l)

names = get_names('names')

def random_name(names):
    return names[random.randrange(len(names))]

for pair in range(100):
    print(f"{random_name(names)},{random_name(names)}")
