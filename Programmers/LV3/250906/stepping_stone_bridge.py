# 프로그래머스 LV3 - 징검다리 건너기 (카카오 인턴)
# 이분탐색 문제

'''
문제 : 최대 몇 사람까지 징검다리를 건널수 있을까?
stone : 징검다리 배열
k : 한 번에 뛸 수 있는 최대 칸
'''

def is_possible(mid, stones, k):
    count = 0
    
    for stone in stones:
        # 만약 mid명의 사람이 건너서 다리의 내구도가 0이되면 count 증가
        if stone - mid <= 0:
            count += 1
        else:
            count = 0
        
        if count >= k:
            return False
            
    return True

def solution(stones, k):
    answer = 0
    start = 1
    end = max(stones) # 5
    
    while start <= end:
        mid = (start + end) // 2
        
        if is_possible(mid, stones, k):
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
            
    return answer

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)