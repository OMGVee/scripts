#!/usr/bin/env python3
string='Practice makes perfect.'
dictionary=['makes','practice','perfect']
def match(s, dct):
    s = s[0:-1].lower().split()
    print(s)
    missing=False
    for word in s:
        if word not in dct:
            print("Missing word:{}".format(word))
            missing=True
    if missing:
        print("nay")
        return False
    else:
        print("yay")
        return True

assert match("pr@actice makes perfect.", dictionary)==False
assert match("practice makes perfect.", dictionary)==True
