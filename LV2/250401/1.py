# 숫자 게임

def solution(A, B):
    A.sort(reverse = True)
    B.sort(reverse = True)
    count = 0
    idx_a = 0
    idx_b = 0

    for i in range(len(A)):
        if A[idx_a] < B[idx_b]:
            count += 1
            idx_a += 1
            idx_b += 1
        else: # 졌으면 제일 작은 B원소 pop, A원소는 다음칸으로 올린다.
            B.pop()
            idx_a += 1
    
    return count

solution([5,1,3,7],[2,2,6,8]) #3