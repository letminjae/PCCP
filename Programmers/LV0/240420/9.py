#삼각형의 완성조건

def solution(sides):
    sides.sort()
    if(sides[0]+sides[1] > sides[2]): return 1
    else: return 2

print(solution([199, 72, 222]))