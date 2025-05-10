# 방문길이

def solution(dirs):
    sets = set()
    x = y = 0
    dic = {
        "U": (1,0),
        "D": (-1,0),
        "L": (0,-1),
        "R": (0,1)
    }
    for d in dirs:
        # 이동할 거리
        dy, dx = dic[d]
        # 현재 위치
        ny = y + dy
        nx = x + dx
        print(f'dy={dy},dx={dx},ny={ny},nx={nx}')
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            sets.add(((y, x), (ny, nx)))
            sets.add(((ny, nx), (y, x)))
            y = ny
            x = nx
        print(f'sets={sets}')
    return len(sets) // 2

print(solution("ULURRDLLU"))