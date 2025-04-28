# 25305 커트라인

N, k = map(int, input().split())

arr = sorted(list(map(int, input().split())), reverse=True)

print(arr[k-1])