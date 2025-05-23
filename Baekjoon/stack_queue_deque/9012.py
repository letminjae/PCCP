# 9012 괄호

import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
  question = input()
  stack = []
  
  for q in question:
    if q == "(":
      stack.append(q)
    elif q == ")":
      if stack:
        stack.pop()
      else:
        print("NO")
        break
  else:
    if not stack:
      print("YES")
    else:
      print("NO")