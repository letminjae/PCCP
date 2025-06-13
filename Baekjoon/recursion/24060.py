# 24060 알고리즘 수업 - 병합 정렬 1

def merge_sort(arr):
    if len(arr) <= 1 :
        return arr
    mid = (len(arr)+1) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    
    sorted_arr = []
    l = 0
    h = 0
    
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] <= high_arr[h] :
            sorted_arr.append(low_arr[l])
            answer.append(low_arr[l])
            l += 1
        else :
            sorted_arr.append(high_arr[h])
            answer.append(high_arr[h])
            h += 1
            
    while l < len(low_arr) :
        sorted_arr.append(low_arr[l])
        answer.append(low_arr[l])
        l += 1
    
    while h < len(high_arr):
        sorted_arr.append(high_arr[h])
        answer.append(high_arr[h])
        h += 1
        
    return sorted_arr

answer = []
N,K = map(int,input().split())
merge_sort(list(map(int, input().split())))
print(answer[K-1] if K <= len(answer) else -1)