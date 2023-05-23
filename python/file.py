#!/usr/bin/env python3

print("working with files - opening self and printing line by line")
f=open("file.py", "r")

for line in f:
    print(line)

print("========== alternative reading by f.read() ============")
f=open("file.py", "r")
print(f.read())

