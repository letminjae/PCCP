# 17219 비밀번호 찾기

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

url_dict = dict()

for _ in range(N):
    url, password = input().split()
    url_dict[url] = password

for _ in range(M):
    url = str(input().strip())
    print(url_dict[url])