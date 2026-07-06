#!/usr/bin/python3

import random

random.seed(0)

def get_names(filename):
    with open(filename, 'r') as file:
        l = map(str.strip, file.readlines());
        return list(l)

max_reports = 10

def nreports(remain):
    return random.randint(0, min(max_reports, remain))

def make_org(names):
    org = {}
    me = 0
    them = 1
    nnames = len(names)
    for me in range(nnames):
        n = nreports(nnames - them)
        reports = names[them:them+n]
#        print(f"me {me} n {n} name {names[me]}, reports {reports}")
        them = them + n
        org[names[me]] = reports
    return org

def dump_org(org):
    for me in org:
        if org[me]:
            print(f"{','.join([me] + org[me])}")

names = get_names('names')

org = make_org(names)

dump_org(org)
