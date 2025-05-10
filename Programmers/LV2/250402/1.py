# 기지국 설치

import math

def solution(n, stations, w):
    answer = 0
    r = w*2+1
    start = 1

    for station in stations:
        r1, r2 = station-w, station+w
        if r1 < 1:
            r1 = 1
        if r2 > n:
            r2 = n
        answer += math.ceil((r1 - start) / r)
        start = r2 + 1

    answer += math.ceil((n-start+1) / r)
    
    return answer

solution(11,[4, 11],1)