#!/usr/bin/env python3

print("first name please:")
fn = input()
fn_split = list(fn)
fn = fn_split[0] + fn_split[1]

print("last name please:")
ln = input()
ln_split = list(ln)
ln = ln_split[0] + ln_split[1]

print("date of hire please, in YYYYMMDD:")
hd = input()
hd_split = list(hd)
cnt=1
sum_even=0
sum_odd=0

print("card code please:")
code = input()

for i in hd_split:
    if cnt % 2 == 0:
        sum_even += int(i)
    else:
        sum_odd += int(i)
    cnt += 1

diff = sum_even - sum_odd

if diff < 0:
    diff = -diff
elif diff > 9:
    diff = diff % 10

print("=====ta-daaaaa=======")
correct=ln+fn+hd+str(diff)
if code != correct:
    print("INVESTIGATE")
else:
    print("PASS")
