# 1269 대칭 차집합

A, B = map(int, input().split())
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

print(len(setA - setB) + len(setB - setA))