# 정수를 나선형으로 배치하기

def solution(n):
    arr = [[0]*n for i in range(n)]
    mode = 1
    x = 0
    y = 0
    
    if n == 1:
        return [[1]]
    for i in range(n*n):
        arr[x][y] = i + 1
        if mode%4 == 1:
            y+=1
            if y == n-1 or arr[x][y+1] != 0:
                mode+=1
        elif mode%4 == 2:
            x+=1
            if x == n-1 or arr[x+1][y] != 0:
                mode+=1
        elif mode%4 == 3:
            y-=1
            if y == n-1 or arr[x][y-1] != 0:
                mode+=1
        elif mode%4 == 0:
            x-=1
            if x == n-1 or arr[x-1][y] != 0:
                mode+=1
    return arr

print(solution(4))