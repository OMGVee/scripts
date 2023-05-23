#!/usr/bin/env python3

def add(lst):
    lst.append(lst[-1]*2+1)
    lst.append(lst[-1]*3+1)
    return lst
def dbl_linear(n):
    print(n)
    u = [1]
    print(add(u))
    uu = list()
    i = len(u)
    while i<n:
        add(u)
    for i in u:
        if i not in uu:
            uu.append(i)
    print("duplicated:{}".format(sorted(u)))
    print("deduplicat:{}".format(sorted(uu)))
