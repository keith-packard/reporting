#!/usr/bin/python

def get_org(filename):
    org = {}
    with open(filename, 'r') as file:
        for line in file.readlines():
            names = line.strip().split(',')
            for report in names[1:]:
                org[report] = names[0]
    return org

def reporting(org, report):
    chain = [report]
    while report in org:
        report = org[report]
        chain = [report] + chain
    return chain

def find_common(org, a, b):
    a_chain = reporting(org, a) 
    b_chain = reporting(org, b)
    common = a_chain[0]
    for i in range(min(len(a_chain), len(b_chain))):
        if a_chain[i] != b_chain[i]:
            break
        common = a_chain[i]
    return common

def get_common(filename, org):
    with open(filename, 'r') as file:
        for line in file.readlines():
            pair = line.strip().split(',')
            print("%s is common for %s,%s" % (find_common(org, pair[0], pair[1]), pair[0], pair[1]))

org = get_org('reports')
get_common('pairs', org)
