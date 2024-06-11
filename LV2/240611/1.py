# 최댓값과 최솟값

# map 메소드 사용하기
def solution(s):
    s = sorted(list(map(int,s.split())))
    return f'{s[0]} {s[-1]}'