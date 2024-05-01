# 수열과 구간 쿼리 1

def solution(arr, queries):
    for l, r in queries:
        for i in range(l, r+1):
            arr[i] += 1
    return arr
            
print(solution([0, 1, 2, 3, 4],[[0, 1],[1, 2],[2, 3]]))