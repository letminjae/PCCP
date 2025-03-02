# 두 큐의 값 같게 만들기

from collections import deque

def solution(queue1, queue2):
    count = 0
    deque1, deque2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(deque1), sum(deque2)
    # 탐색 제한 범위 : 1이 2로 모두 이동, 2가 1로 모두 이동, 모두 이동한 1의 반을 2로 이동, 총 3번 이동
    break_point = len(deque1 * 3)
   
    while sum1 != sum2:
        if sum1 > sum2 :
            temp = deque1.popleft()
            deque2.append(temp)
            sum1 -= temp
            sum2 += temp
        elif sum1 < sum2 :
            temp = deque2.popleft()
            deque1.append(temp)
            sum1 += temp
            sum2 -= temp
        count += 1
   
        if count == break_point:
            return -1

    return count