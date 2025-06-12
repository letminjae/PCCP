# 25501 재귀의 귀재

import sys
input = sys.stdin.readline

N = int(input())

def recursion(str, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif str[l] != str[r]:
        return 0
    else:
        return recursion(str, l+1, r-1)

def isPalindrome(str):
    return recursion(str, 0, len(str)-1)

for _ in range(N):
    cnt = 0
    str = input().strip()
    print(isPalindrome(str), cnt)