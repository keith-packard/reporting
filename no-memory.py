#!/usr/bin/python

def get_org(filename):
    org = {}
    with open(filename, 'r') as file:
        for line in file.readlines():
            names = line.strip().split(',')
            for report in names[1:]:
                org[report] = names[0]
    ceo = None
    for report in org:
        if org[report] not in org:
            ceo = org[report]
    org[ceo] = None
    return org

def in_chain(org, needle, haystack):
    while haystack:
        if needle == haystack:
            return True
        haystack = org[haystack]
    return False

def find_common(org, a, b):
    while a:
        if in_chain(org, a, b):
            return a
        a = org[a]

def get_common(filename, org):
    with open(filename, 'r') as file:
        for line in file.readlines():
            pair = line.strip().split(',')
            print("%s is common for %s,%s" % (find_common(org, pair[0], pair[1]), pair[0], pair[1]))

org = get_org('reports')
get_common('pairs', org)
