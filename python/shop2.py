#!/usr/bin/env python3
string='Practicemakesperfect'
dictionary=['makes','practice','perfect']
def match(s, dct):
    s=s.lower()
    for word in dct:
        if word in s:
            s=s.replace(word,"")
    if len(s)>0:
        return False
    else:
        return True

assert match("pr@acticeMakesperfect", dictionary)==False
assert match("practicemakesPerfect", dictionary)==True
