#!/usr/bin/env python3
def fb(n):
    for i in range(1,n+1):
        if (i %3==0 and i%5==0):
            print("fb")
        elif i % 3 == 0:
            print("f")
        elif i % 5 == 0:
            print("b")
        else:
            print(i)
        
print("gimme a number, son:")
n = input()

fb(int(n))
