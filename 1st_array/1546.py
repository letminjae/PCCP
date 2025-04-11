# 1546. 평균

N = int(input())
arr = list(map(int, input().split()))

M = max(arr)

newAverage = [num/M * 100 for num in arr]
newAverage = sum(newAverage) / N
print(newAverage)