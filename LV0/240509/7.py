# 주사위 찾기 3

def solution(a, b, c, d):
    answer = 0
    arr = [a, b, c, d]
    set_list = list(set(arr))
    
    if len(set_list) == 4:
        answer = min(set_list)
    elif len(set_list) == 3:
        p = max(arr, key=arr.count)
        tmp = [num for num in set_list if num != p]
        answer = tmp[0] * tmp[1]
    elif len(set_list) == 2:
        if max([arr.count(num) for num in set_list]) > 2:
            p = max(arr, key=arr.count)
            q = min(arr, key=arr.count)
            answer = pow(((10 * p) + q), 2)
        else:
            answer = ((set_list[0] + set_list[1]) * abs(set_list[0] - set_list[1]))  
    elif len(set_list) == 1:
        answer = int(str(set_list[0]) * 4)
    
    return answer

print(solution(4,4,4,4))