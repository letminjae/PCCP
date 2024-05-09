# 안전지대

def solution(board):
    N = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    # 지뢰 위치
    bomb = []
    for i in range(len(board)):
        for j in range(len(board)):
            print(f"i = {i}, j = {j}, board[i][j] = {board[i][j]}")
            if board[i][j] == 1:
                bomb.append((i,j))

    # 위험 지역
    for x, y in bomb:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] = 1

    # 안전 지역
    safe = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                safe += 1
    return safe

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))