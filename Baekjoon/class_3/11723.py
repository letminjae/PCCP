# 11723 집합

import sys
input = sys.stdin.readline

N = int(input())
S = set()

for _ in range(N):
    arr = input().split()
    command = arr[0]

    if command == 'add':
        S.add(int(arr[1]))
    elif command == 'remove':
        S.discard(int(arr[1]))
    elif command == 'check':
        print(1 if int(arr[1]) in S else 0)
    elif command == 'toggle':
        num = int(arr[1])
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif command == 'all':
        S = set(range(1, 21))
    elif command == 'empty':
        S = set()