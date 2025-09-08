# 프로그래머스 LV3 - 연속 펄스 부분 수열의 합 (pulse.py)
# 동적 계획법 - 펄스 * 배열의 누적합 

def find_max(seq):
    current_max = seq[0]
    max_far = seq[0]
    
    for i in range(1, len(seq)):
        current_max = max(seq[i], seq[i]+current_max)
        max_far = max(max_far, current_max)
    
    return max_far

def solution(sequence):
    N = len(sequence)
    
    # 1부터 시작하는 경우
    seq1 = [1] * N
    for i in range(1, N, 2):
        seq1[i] = -seq1[i]
    for i in range(N):
        seq1[i] = seq1[i] * sequence[i]
    
    # -1부터 시작하는 경우
    seq2 = [1] * N
    for i in range(0, N, 2):
        seq2[i] = -seq2[i]
    for i in range(N):
        seq2[i] = seq2[i] * sequence[i]
    
    max1 = find_max(seq1)
    max2 = find_max(seq2)
    
    return max(max1, max2)

solution([2, 3, -6, 1, 3, -1, 2, 4])