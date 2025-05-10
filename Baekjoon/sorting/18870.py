# 18870 좌표압축
# 좌표 압축 : dict로 정렬한 독립원소를 index 순서를 매겨 print

N = int(input())
arr = list(map(int, input().split()))

sorted_unique = sorted(set(arr))
dict = {num: i for i, num in enumerate(sorted_unique)}

answer = [dict[num] for num in arr]
print(' '.join(map(str, answer)))