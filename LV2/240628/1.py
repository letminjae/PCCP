# 연속 부분 수열 합의 개수

def solution(elements):
    result = set()
    
    l = len(elements)
    # [7, 9, 1, 1, 4, 7, 9, 1, 1, 4]
    elements = elements * 2
    
    for i in range(l):
        for j in range(l):
            print(i, j, elements[j:j+i+1])
            result.add(sum(elements[j:j+i+1]))
    return len(result)

print(solution([7,9,1,1,4]))