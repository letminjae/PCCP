# 배열 조각하기

def solution(arr, query):
    for i, v in enumerate(query):
        if i % 2 == 0:
            arr = arr[:v+1]
        else:
            arr = arr[v:]
    return arr