#!/usr/bin/env python3
board=[
  [1,0,0,0,0,0,0],
  [2,0,0,0,0,0,0],
  [3,2,3,4,5,6,7],
  [4,2,3,4,5,6,7],
  [5,2,3,4,5,6,7],
  [6,2,3,4,5,6,7],
]
i=j=0

for i in range(len(board)):
    row=board[i]
    for j in range(len(row)):
        col=row[j]
        print("i:j(%s:%s) - %s"%(i,j,col))
