# 11723 집합

import sys
input = sys.stdin.readline

N = int(input())
S = set()

for _ in range(N):
  arr = list(input().split())
  first = arr[0]
  
  if first == 'add':
    first.add(int(arr[1]))
  elif first == 'remove':
    try:
      S.remove(int(arr[1]))
    except:
      pass
  elif first == 'check':
    if int(arr[1]) in S:
        print(1)
    else:
      print(0)
  elif first == 'toggle':
    if int(arr[1]) in S:
      S.remove(int(arr[1]))
    else:
      S.add(int(arr[1]))
  elif first == 'all':
    S = set([i for i in range(1, 21)])
  else:
    S = set()
